import os
import logging
from flask import Flask
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# Flask app for Render's health check
app = Flask(__name__)

@app.route('/')
def health_check():
    return "Bot is running!", 200

# Telegram Bot Handlers
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hi! I am your bot hosted on Render. Send me a message!')

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"You said: {update.message.text}")

def main():
    # Get token from environment variable
    TOKEN = os.getenv("TELEGRAM_TOKEN")
    if not TOKEN:
        logger.error("No TELEGRAM_TOKEN found in environment variables!")
        return

    # Build the Application
    application = Application.builder().token(TOKEN).build()

    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Start the bot
    logger.info("Bot started...")
    
    # Run Flask in the background or just use polling for simplicity on Render
    # Note: Render requires a web service to bind to a port, or use a Background Worker
    application.run_polling()

if __name__ == '__main__':
    # For Render Web Service, we need to bind to a port
    # If you use a 'Background Worker' on Render, you don't need Flask.
    # If you use a 'Web Service', keep the Flask part.
    import threading
    port = int(os.environ.get("PORT", 8080))
    threading.Thread(target=lambda: app.run(host='0.0.0.0', port=port)).start()
    
    main()