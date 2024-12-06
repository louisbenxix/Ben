from flask import Flask, request
import requests

app = Flask(__name__)

# Thay token và chat_id của bạn vào đây
BOT_TOKEN = "7726901239:AAEfAG8kzDU8aG7W99vJvV5D_7zyX7V7bXQ"  # Đặt trong dấu ngoặc kép
CHAT_ID = "968290827"  # Đặt trong dấu ngoặc kép

# Hàm gửi tin nhắn đến Telegram
def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,  # Sử dụng biến CHAT_ID thay vì cố định
        "text": message,
        "parse_mode": "Markdown"
    }
    try:
        response = requests.post(url, json=payload)
        if response.status_code != 200:
            print(f"Failed to send message: {response.text}")
    except Exception as e:
        print(f"Error sending message: {e}")

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
