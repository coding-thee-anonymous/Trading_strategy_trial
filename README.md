# XAUUSD Return-to-Point-A Alert Bot (TradingView)

This project gives you an MVP for your idea:

- Detect a **Point A** on XAUUSD chart (pivot high/low).
- Wait for price to move away by a minimum percent.
- Alert when price returns to that same Point A.

This version is print-only:

- Pine script prints on-chart markers/labels when price returns to Point A.
- Optional webhook server prints TradingView payloads to terminal.

## 1) Add the Pine script in TradingView

1. Open TradingView chart for XAUUSD.
2. Open **Pine Editor**.
3. Copy content of `xauusd_return_to_point_a.pine`.
4. Click **Add to chart**.
5. Set inputs:
   - **Pattern**: `High → Down → Back to High` (matches your example)
   - **Minimum Move Away (%)**: e.g. `0.25`
   - **Return Tolerance (ticks)**: e.g. `8`

## 2) Use it on chart (print-only)

1. Use Pine version **6** (`//@version=6`).
2. In script settings, choose:
   - **Pattern**: `HIGH_DOWN_HIGH` (matches your example), or
   - **`LOW_UP_LOW`** for the opposite direction.
3. When a return happens, the script prints a label on chart: `Returned to A`.

## 3) Optional: run webhook print server

Use this only if you want TradingView webhook payloads printed in your terminal.

### Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Run server:

```bash
python webhook_email_bridge.py
```

Use this as your TradingView webhook URL:

- `http://YOUR_SERVER_IP:5000/tradingview-webhook`

## Notes

- This is bar-based logic (it confirms on candle close for clean signals).
- The script finds Point A automatically using pivots.
- If you want manual Point A selection (you click a level), I can add that next.
