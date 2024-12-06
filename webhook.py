from flask import Flask, request
import requests

app = Flask(__name__)

# Thay token và chat_id của bạn vào đây
BOT_TOKEN = "your_bot_token"
CHAT_ID = "your_chat_id"

# Hàm gửi tin nhắn đến Telegram
def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{7726901239:AAEfAG8kzDU8aG7W99vJvV5D_7zyX7V7bXQ}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    requests.post(url, json=payload)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    if data:
        # Xử lý dữ liệu alert từ TradingView
        alert_message = data.get('message', 'No message in alert!')
        send_telegram_message(f"🚨 *Trading Alert*\n\n{alert_message}")
        return "Alert received!", 200
    return "No data!", 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
