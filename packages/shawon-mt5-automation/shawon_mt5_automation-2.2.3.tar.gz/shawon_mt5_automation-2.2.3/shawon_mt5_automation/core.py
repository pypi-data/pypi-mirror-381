from flask import Flask, request, jsonify
import MetaTrader5 as mt5
import time
from datetime import datetime
import logging
import json
import os
from functools import wraps

# ------------------- Logging -------------------
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class Trader:
    def __init__(self, account:int, password:str, server:str,
                 mt5_symbol:str="BTCUSDm", lot:float=0.01,
                 stop_loss_usd:float=0, take_profit_usd:float=0,
                 signal_gap_seconds:int=600, signal_file:str="last_signal_time.json",
                 api_key:str=None):

        self.account = account
        self.password = password
        self.server = server
        self.mt5_symbol = mt5_symbol
        self.lot = lot
        self.stop_loss_usd = stop_loss_usd
        self.take_profit_usd = take_profit_usd
        self.signal_gap_seconds = signal_gap_seconds
        self.signal_file = signal_file
        self.api_key = api_key

        self._mt5_connected = False
        self._last_signal_time = self._load_last_signal_time()

        self.app = Flask(__name__)
        self._setup_routes()

    # ------------------- Signal Time Handling -------------------
    def _load_last_signal_time(self):
        if os.path.exists(self.signal_file):
            try:
                with open(self.signal_file, "r") as f:
                    data = json.load(f)
                    return {k: float(v) if v is not None else None for k,v in data.items()}
            except:
                return {"buy": None, "sell": None}
        return {"buy": None, "sell": None}

    def _save_last_signal_time(self):
        with open(self.signal_file, "w") as f:
            json.dump(self._last_signal_time, f)

    # ------------------- MT5 Connect -------------------
    def _mt5_connect(self):
        if self._mt5_connected:
            return True
        if not mt5.initialize():
            logger.error("MT5 initialize failed: %s", mt5.last_error())
            return False
        if not mt5.login(self.account, self.password, self.server):
            logger.error("MT5 login failed: %s", mt5.last_error())
            mt5.shutdown()
            return False
        logger.info("MT5 Connected for account %s", self.account)
        self._mt5_connected = True
        return True

    # ------------------- Close Positions -------------------
    def _close_all_positions(self, symbol:str):
        positions = mt5.positions_get(symbol=symbol)
        if not positions:
            return True
        for pos in positions:
            order_type = mt5.ORDER_TYPE_SELL if pos.type==mt5.POSITION_TYPE_BUY else mt5.ORDER_TYPE_BUY
            tick = mt5.symbol_info_tick(pos.symbol)
            if not tick:
                continue
            price = tick.bid if order_type==mt5.ORDER_TYPE_SELL else tick.ask
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
                "type_filling": mt5.ORDER_FILLING_IOC
            }
            mt5.order_send(request)
        return True

    # ------------------- Place Order -------------------
    def _place_order(self, action:str):
        symbol_info = mt5.symbol_info(self.mt5_symbol)
        if not symbol_info:
            logger.error("Symbol not found")
            return False
        if not symbol_info.visible:
            mt5.symbol_select(self.mt5_symbol, True)
        tick = mt5.symbol_info_tick(self.mt5_symbol)
        if not tick:
            return False
        order_type = mt5.ORDER_TYPE_BUY if action.lower()=="buy" else mt5.ORDER_TYPE_SELL
        entry_price = tick.ask if order_type==mt5.ORDER_TYPE_BUY else tick.bid

        request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": self.mt5_symbol,
            "volume": self.lot,
            "type": order_type,
            "price": entry_price,
            "deviation": 20,
            "magic": 123456,
            "comment": "Webhook Trade",
            "type_filling": mt5.ORDER_FILLING_IOC
        }
        result = mt5.order_send(request)
        if hasattr(result,"retcode") and result.retcode==mt5.TRADE_RETCODE_DONE:
            logger.info("%s order placed", action.upper())
            return True
        logger.error("Order failed: %s", result)
        return False

    # ------------------- API Key Decorator (Body Only) -------------------
    def _require_api_key(self, f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not self.api_key:
                return f(*args, **kwargs)
            if not request.is_json:
                return jsonify({"status":"error","message":"API Key required"}), 401
            data = request.get_json()
            incoming_api_key = data.get("X-API-Key")
            if not incoming_api_key:
                return jsonify({"status":"error","message":"API Key required"}), 401
            if incoming_api_key != self.api_key:
                return jsonify({"status":"error","message":"Invalid API Key"}), 403
            return f(*args, **kwargs)
        return decorated_function

    # ------------------- Flask Routes -------------------
    def _setup_routes(self):
        @self.app.route("/tradingview-webhook", methods=["POST"])
        @self._require_api_key
        def webhook_handler():
            data = request.get_json()
            incoming_signal = data.get("signal","").lower()
            if incoming_signal not in ["buy","sell"]:
                return jsonify({"status":"error","message":"Invalid signal"}), 400

            current_time = time.time()
            last_time = self._last_signal_time.get(incoming_signal)
            if last_time and (current_time - last_time < self.signal_gap_seconds):
                wait = int((self.signal_gap_seconds - (current_time - last_time))/60)+1
                return jsonify({"status":"ignored","message":f"{incoming_signal.upper()} ignored. Wait {wait} min."}), 200

            self._last_signal_time[incoming_signal] = current_time
            self._save_last_signal_time()

            if not self._mt5_connect():
                return jsonify({"status":"error","message":"MT5 connection failed"}),500

            self._close_all_positions(self.mt5_symbol)
            success = self._place_order(incoming_signal)
            if success:
                return jsonify({"status":"success","action":incoming_signal,
                                "message":f"{incoming_signal.upper()} order executed",
                                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}),200
            return jsonify({"status":"error","message":"Failed to place order"}),500


