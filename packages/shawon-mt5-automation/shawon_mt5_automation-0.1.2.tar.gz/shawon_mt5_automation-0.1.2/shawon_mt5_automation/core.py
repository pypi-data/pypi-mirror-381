

from flask import Flask, request, jsonify
import MetaTrader5 as mt5
import threading
import time
from datetime import datetime
import json
import os
import logging
from functools import wraps

# Setup basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class MT5WebhookTrader:
    def __init__(self,
                 account: int,
                 password: str,
                 server: str,
                 mt5_symbol: str = "BTCUSDm",
                 lot: float = 0.01,
                 stop_loss_usd: float = 0,    # 0 means no SL
                 take_profit_usd: float = 0,   # 0 means no TP
                 signal_gap_seconds: int = 10 * 60, # 10 minutes
                 signal_file: str = "last_signal_time.json",
                 api_key: str = None):
        
        self.account = account
        self.password = password
        self.server = server
        self.mt5_symbol = mt5_symbol
        self.lot = lot
        self.stop_loss_usd = stop_loss_usd
        self.take_profit_usd = take_profit_usd
        self.signal_gap_seconds = signal_gap_seconds
        self.signal_file = signal_file
        self.api_key = api_key # The API key for webhook authentication

        self._mt5_connected = False
        self._last_signal_time = self._load_last_signal_time()

        self.app = Flask(__name__)
        self._setup_routes()

    def _load_last_signal_time(self):
        if os.path.exists(self.signal_file):
            with open(self.signal_file, "r") as f:
                try:
                    data = json.load(f)
                    return {k: float(v) if v is not None else None for k, v in data.items()}
                except json.JSONDecodeError:
                    logger.warning(f"Could not decode {self.signal_file}. Starting with empty signal times.")
                    return {"buy": None, "sell": None}
        return {"buy": None, "sell": None}

    def _save_last_signal_time(self):
        with open(self.signal_file, "w") as f:
            json.dump(self._last_signal_time, f)

    def _mt5_connect(self):
        if self._mt5_connected:
            return True
        
        if not mt5.initialize():
            logger.error("❌ MT5 initialize failed: %s", mt5.last_error())
            return False
        
        authorized = mt5.login(self.account, self.password, self.server)
        if not authorized:
            logger.error("❌ MT5 login failed (Account: %s, Server: %s): %s", self.account, self.server, mt5.last_error())
            mt5.shutdown()
            return False
        
        logger.info("✅ MT5 Connected successfully for account %s", self.account)
        self._mt5_connected = True
        return True

    def _close_all_positions(self, symbol: str):
        positions = mt5.positions_get(symbol=symbol)
        if not positions:
            logger.info("ℹ No open positions to close for %s.", symbol)
            return True
        
        for pos in positions:
            order_type = mt5.ORDER_TYPE_SELL if pos.type == mt5.POSITION_TYPE_BUY else mt5.ORDER_TYPE_BUY
            tick = mt5.symbol_info_tick(pos.symbol)
            if tick is None:
                logger.error("❌ Could not get tick for %s to close position %s", pos.symbol, pos.ticket)
                continue
            
            price = tick.bid if order_type == mt5.ORDER_TYPE_SELL else tick.ask
            request = {
                "action": mt5.TRADE_ACTION_DEAL,
                "position": pos.ticket,
                "symbol": pos.symbol,
                "volume": pos.volume,
                "type": order_type,
                "price": price,
                "deviation": 20,
                "magic": 123456,
                "comment": "Auto-close by webhook",
                "type_filling": mt5.ORDER_FILLING_IOC,
            }
            result = mt5.order_send(request)
            
            if hasattr(result, "retcode") and result.retcode == mt5.TRADE_RETCODE_DONE:
                logger.info("✅ Closed %s position (ticket %s, volume %s) at %s", pos.symbol, pos.ticket, pos.volume, price)
            else:
                logger.error("❌ Failed to close %s position (ticket %s): %s", pos.symbol, pos.ticket, result)
        return True

    def _calc_sl_tp(self, symbol: str, entry_price: float, order_type: str):
        if (self.stop_loss_usd <= 0 and self.take_profit_usd <= 0):
            logger.info("ℹ Both STOP_LOSS_USD and TAKE_PROFIT_USD are 0 or negative. No SL/TP will be set.")
            return 0.0, 0.0 # Return 0 to indicate no SL/TP

        info = mt5.symbol_info(symbol)
        if not info:
            logger.error("❌ Could not get symbol info for %s", symbol)
            return None, None

        # Ensure trade_tick_value and trade_tick_size are not zero to avoid division by zero
        # Using a default if 0, though MT5 usually provides proper values
        tick_value = info.trade_tick_value if info.trade_tick_value > 0 else 1.0 
        tick_size = info.trade_tick_size if info.trade_tick_size > 0 else info.point # fallback to point if tick_size is 0

        # Calculate per-point value based on LOT
        # For instruments like BTCUSDm, trade_contract_size is 1, so lot * tick_value is usually per point value
        per_point_value = self.lot * tick_value 

        sl_points = 0.0
        tp_points = 0.0

        if self.stop_loss_usd > 0:
            sl_points = self.stop_loss_usd / per_point_value
        if self.take_profit_usd > 0:
            tp_points = self.take_profit_usd / per_point_value

        sl = 0.0
        tp = 0.0

        if order_type.lower() == "buy":
            if self.stop_loss_usd > 0:
                sl = entry_price - sl_points * info.point
            if self.take_profit_usd > 0:
                tp = entry_price + tp_points * info.point
        else: # sell
            if self.stop_loss_usd > 0:
                sl = entry_price + sl_points * info.point
            if self.take_profit_usd > 0:
                tp = entry_price - tp_points * info.point

        logger.info("Calculated SL: %.5f, TP: %.5f for entry price %.5f (Order Type: %s)", sl, tp, entry_price, order_type)
        return sl, tp

    def _place_order(self, action: str):
        symbol_info = mt5.symbol_info(self.mt5_symbol)
        if symbol_info is None:
            logger.error("❌ Symbol %s not found", self.mt5_symbol)
            return False
        if not symbol_info.visible:
            mt5.symbol_select(self.mt5_symbol, True)
            symbol_info = mt5.symbol_info(self.mt5_symbol) # Re-fetch after selecting
            if not symbol_info.visible:
                logger.error("❌ Could not make symbol %s visible", self.mt5_symbol)
                return False

        order_type = mt5.ORDER_TYPE_BUY if action.lower() == "buy" else mt5.ORDER_TYPE_SELL
        tick = mt5.symbol_info_tick(self.mt5_symbol)
        if tick is None:
            logger.error("❌ Could not get symbol tick for %s", self.mt5_symbol)
            return False
        
        entry_price = tick.ask if order_type == mt5.ORDER_TYPE_BUY else tick.bid

        sl, tp = self._calc_sl_tp(self.mt5_symbol, entry_price, action)
        if sl is None or tp is None:
            logger.error("❌ SL/TP calculation failed")
            return False
        
        request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": self.mt5_symbol,
            "volume": self.lot,
            "type": order_type,
            "price": entry_price,
            "deviation": 20,
            "magic": 123456,
            "comment": "Webhook Trade",
            "type_filling": mt5.ORDER_FILLING_IOC,
        }

        # Only add SL/TP if they are effectively set (i.e., not 0)
        if self.stop_loss_usd > 0:
            request["sl"] = sl
        if self.take_profit_usd > 0:
            request["tp"] = tp

        result = mt5.order_send(request)
        
        if hasattr(result, "retcode") and result.retcode == mt5.TRADE_RETCODE_DONE:
            sl_info = f"SL={sl}" if self.stop_loss_usd > 0 else "No SL"
            tp_info = f"TP={tp}" if self.take_profit_usd > 0 else "No TP"
            logger.info("✅ Order placed: %s %s lot %s, %s, %s", action.upper(), self.mt5_symbol, self.lot, sl_info, tp_info)
            return True
        
        logger.error("❌ Order failed: %s", result)
        return False

    def _require_api_key(self, f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not self.api_key: # If no API key is set in config, bypass authentication
                return f(*args, **kwargs)

            # Check for API key in headers
            incoming_api_key = request.headers.get('X-API-Key')
            if not incoming_api_key:
                logger.warning("🚫 API Key missing from request.")
                return jsonify({"status": "error", "message": "API Key required"}), 401
            
            if incoming_api_key != self.api_key:
                logger.warning("🚫 Invalid API Key received.")
                return jsonify({"status": "error", "message": "Invalid API Key"}), 403
            
            return f(*args, **kwargs)
        return decorated_function

    def _setup_routes(self):
        @self.app.route('/tradingview-webhook', methods=['POST'])
        @self._require_api_key
        def webhook_handler():
            try:
                data = request.get_json()
                incoming_signal = data.get("signal", "").lower()
                if incoming_signal not in ["buy", "sell"]:
                    logger.warning("Received invalid signal: %s", incoming_signal)
                    return jsonify({"status": "error", "message": "Invalid signal"}), 400

                # Time gap check for same signal
                current_time = time.time()
                last_time = self._last_signal_time.get(incoming_signal)
                if last_time and (current_time - last_time < self.signal_gap_seconds):
                    wait_minutes = int((self.signal_gap_seconds - (current_time - last_time)) / 60) + 1
                    logger.info("%s signal ignored. Wait %s more minutes.", incoming_signal.upper(), wait_minutes)
                    return jsonify({
                        "status": "ignored",
                        "message": f"{incoming_signal.upper()} signal ignored. Wait {wait_minutes} more minutes."
                    }), 200

                # Save current signal time
                self._last_signal_time[incoming_signal] = current_time
                self._save_last_signal_time()

                logger.info("📨 Received signal: %s", incoming_signal.upper())

                if not self._mt5_connect():
                    return jsonify({"status": "error", "message": "MT5 connection failed"}), 500

                # Close existing positions before new signal
                positions = mt5.positions_get(symbol=self.mt5_symbol)
                if positions and len(positions) > 0:
                    logger.info("Detected existing positions. Closing them before new signal.")
                    self._close_all_positions(self.mt5_symbol)
                    time.sleep(0.5) # Give a small delay for closure to process

                # Place the order
                success = self._place_order(incoming_signal)
                if success:
                    return jsonify({
                        "status": "success",
                        "action": incoming_signal,
                        "message": f"{incoming_signal.upper()} order executed successfully",
                        "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    }), 200

                return jsonify({"status": "error", "message": "Failed to place order"}), 500
            except Exception as e:
                logger.exception("Error in webhook handler:")
                return jsonify({"status": "error", "message": str(e)}), 500

        @self.app.route('/position-status', methods=['GET'])
        @self._require_api_key
        def position_status_handler():
            try:
                if not self._mt5_connect():
                    return jsonify({"status": "error", "message": "MT5 connection failed"}), 500

                positions = mt5.positions_get(symbol=self.mt5_symbol)
                pos_list = []
                if positions and len(positions) > 0:
                    for pos in positions:
                        position_type = "buy" if pos.type == mt5.POSITION_TYPE_BUY else "sell"
                        pos_list.append({
                            "type": position_type,
                            "volume": pos.volume,
                            "profit": pos.profit,
                            "ticket": pos.ticket,
                            "open_time": datetime.fromtimestamp(pos.time).strftime('%Y-%m-%d %H:%M:%S')
                        })
                    return jsonify({"status": "success", "has_position": True, "positions": pos_list}), 200
                return jsonify({"status": "success", "has_position": False, "message": "No open positions"}), 200
            except Exception as e:
                logger.exception("Error in position status handler:")
                return jsonify({"status": "error", "message": str(e)}), 500

        @self.app.route('/close-all', methods=['POST'])
        @self._require_api_key
        def close_all_handler():
            try:
                if not self._mt5_connect():
                    return jsonify({"status": "error", "message": "MT5 connection failed"}), 500
                
                self._close_all_positions(self.mt5_symbol)
                return jsonify({"status": "success", "message": "All positions closed"}), 200
            except Exception as e:
                logger.exception("Error in close all handler:")
                return jsonify({"status": "error", "message": str(e)}), 500

    def run(self, host: str = '0.0.0.0', port: int = 5000, debug: bool = False):
        logger.info("🚀 Starting MT5 Webhook Trader Server...")
        if self.api_key:
            logger.info("🔑 API Key authentication is ENABLED. Provide 'X-API-Key' header in requests.")
        else:
            logger.warning("⚠️ No API Key provided. Webhook endpoints are publicly accessible.")
        self.app.run(host=host, port=port, debug=debug, threaded=True)