# MT5 Webhook Trader

A Python Flask application designed to automate MetaTrader 5 (MT5) trading based on incoming webhook signals, typically from platforms like TradingView. This package allows users to configure their MT5 account details, trade parameters (lot size, optional Stop Loss/Take Profit in USD), and secure the webhook endpoints with an API key.

## Features

-   **Configurable MT5 Details**: Easily set your MT5 account, password, server, and trading symbol.
-   **Flexible Trade Parameters**: Define lot size, and optional Stop Loss (SL) and Take Profit (TP) values in USD. If SL/TP values are 0 or not provided, they won't be set on the trade.
-   **API Key Authentication**: Secure your webhook endpoints with an API key (`X-API-Key` header) to prevent unauthorized access.
-   **Signal Gap Control**: Prevent over-trading by setting a minimum time gap between consecutive BUY or SELL signals.
-   **Automatic Position Management**: Closes all existing positions for the specified symbol before placing a new trade signal.
-   **Status Endpoints**: Check current open positions or manually close all positions via dedicated API endpoints.
-   **Persistent Signal Times**: Stores the last signal time to disk to maintain state across restarts.

## Installation

```bash
pip install shawon_mt5_automation