# Telegram Bot for Render

This is a production-ready Telegram bot template designed to be deployed on [Render](https://render.com).

## Setup Instructions

1. **Get a Bot Token**: Message [@BotFather](https://t.me/botfather) on Telegram to get your API Token.
2. **Create a GitHub Repo**: Push these files to your repository.
3. **Deploy on Render**:
   - Create a new **Web Service**.
   - Connect your GitHub repository.
   - **Runtime**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python main.py`
4. **Environment Variables**:
   - Add `TELEGRAM_TOKEN` in the Render dashboard under the 'Environment' tab.

## Features
- Includes a Flask server to satisfy Render's port binding requirement for Web Services.
- Uses `python-telegram-bot` v20+ (async/await).
- Auto-restarts on failure.