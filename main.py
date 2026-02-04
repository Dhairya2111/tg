import asyncio
import sys
from telethon import TelegramClient, functions, types
from telethon.errors import SessionPasswordNeededError, FloodWaitError

# Configuration
API_ID = 1234567  # Replace with your API ID
API_HASH = 'your_api_hash'  # Replace with your API Hash
SESSION_STRING = 'your_session_string' # Telethon Session String

async def report_user(target_username, reason_type):
    """
    Reports a user using a specific session string.
    """
    client = TelegramClient(None, API_ID, API_HASH)
    
    try:
        # Connect using session string
        await client.start()
        print("[+] Connected to session.")

        # Get the target entity
        target = await client.get_input_entity(target_username)
        
        # Mapping reasons to Telethon types
        reasons = {
            'spam': types.InputReportReasonSpam(),
            'violence': types.InputReportReasonViolence(),
            'porn': types.InputReportReasonPornography(),
            'child_abuse': types.InputReportReasonChildAbuse(),
            'other': types.InputReportReasonOther()
        }

        selected_reason = reasons.get(reason_type, types.InputReportReasonSpam())

        # Sending the report
        # Note: Telegram requires a message ID or a reason string for some reports
        result = await client(functions.account.ReportPeerRequest(
            peer=target,
            reason=selected_reason,
            message="This user is violating terms of service and spreading harmful content."
        ))

        if result:
            print(f"[SUCCESS] Reported {target_username} for {reason_type}")
        else:
            print(f"[FAILED] Could not report {target_username}")

    except FloodWaitError as e:
        print(f"[!] Rate limited. Wait for {e.seconds} seconds.")
    except Exception as e:
        print(f"[ERROR] {str(e)}")
    finally:
        await client.disconnect()

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python main.py <target_username> <reason>")
        print("Reasons: spam, violence, porn, child_abuse, other")
    else:
        target = sys.argv[1]
        reason = sys.argv[2]
        
        loop = asyncio.get_event_loop()
        loop.run_until_complete(report_user(target, reason))