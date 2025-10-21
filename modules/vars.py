# Configuration - All values MUST be set via Replit Secrets or environment variables
import os
from os import environ

# Required Telegram API credentials - Get from https://my.telegram.org/apps
API_ID = int(environ.get("API_ID") or "0")
if API_ID == 0:
    raise ValueError("API_ID environment variable is required. Get it from https://my.telegram.org/apps")

API_HASH = (environ.get("API_HASH") or "").strip()
if not API_HASH:
    raise ValueError("API_HASH environment variable is required. Get it from https://my.telegram.org/apps")

# Bot token from @BotFather
BOT_TOKEN = (environ.get("BOT_TOKEN") or "").strip()
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN environment variable is required. Get it from @BotFather on Telegram")

# Owner Telegram user ID
OWNER = int(environ.get("OWNER") or "0")
if OWNER == 0:
    raise ValueError("OWNER environment variable is required. Your Telegram user ID (get from @userinfobot)")

# Bot credit/name
CREDIT = environ.get("CREDIT", "𝙎𝘼𝙄𝙉𝙄 𝘽𝙊𝙏𝙎")

# YouTube cookies file path
cookies_file_path = os.getenv("cookies_file_path", "youtube_cookies.txt")

# User lists - defaults to owner if not set
TOTAL_USER = os.environ.get('TOTAL_USERS', str(OWNER)).split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', str(OWNER)).split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
