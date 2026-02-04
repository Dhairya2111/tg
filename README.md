# Telegram Bot Repository

This is a production-ready Telegram bot template.

## Setup Instructions

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Set Environment Variable**:
   - On Windows:
     ```cmd
     set BOT_TOKEN=your_token_here
     ```
   - On Linux/Mac:
     ```bash
     export BOT_TOKEN=your_token_here
     ```

3. **Run the Bot**:
   ```bash
   python main.py
   ```

## Features
- Basic `/start` and `/help` commands.
- Logging enabled for debugging.
- Uses `python-telegram-bot` v20+ (asyncio).