import os
import requests
from dotenv import load_dotenv

load_dotenv()

def send_telegram_message(message):

    bot_token = os.getenv("BOT_TOKEN")
    chat_id = os.getenv("CHAT_ID")

    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

    response = requests.post(
        url,
        json={
            "chat_id": chat_id,
            "text": message
        }
    )

    return response.json()