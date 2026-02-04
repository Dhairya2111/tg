from telethon.sync import TelegramClient
from telethon.sessions import StringSession

print("--- Telegram Session String Generator ---")
api_id = int(input("Enter API ID: "))
api_hash = input("Enter API Hash: ")

with TelegramClient(StringSession(), api_id, api_hash) as client:
    print("\nYour Session String is:\n")
    print(client.session.save())
    print("\nCopy this string and paste it into main.py")