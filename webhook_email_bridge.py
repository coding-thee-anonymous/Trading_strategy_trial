from datetime import datetime, timezone
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.post("/tradingview-webhook")
def tradingview_webhook():
    payload = request.get_json(silent=True) or {}
    raw_text = request.data.decode("utf-8", errors="ignore")
    event = payload if payload else raw_text
    timestamp = datetime.now(timezone.utc).isoformat()
    print(f"[{timestamp}] TradingView webhook received: {event}", flush=True)
    return jsonify({"ok": True, "printed": True}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
