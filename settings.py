import os
from datetime import datetime, timedelta, timezone

from dotenv import load_dotenv

load_dotenv()
DISCORD_TOKEN = os.environ.get("DISCORDBOT_TOKEN")
CHANNEL_ID = int(os.environ.get("CHANNEL_ID"))
NOTIFY_CHANNEL_ID = int(os.environ.get("NOTIFY_CHANNEL_ID"))
DATABASE_URL = os.environ.get("DATABASE_URL")
DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%S%z"
DATE_FORMAT = "%Y-%m-%d"
TIMEZONE = timezone(timedelta(hours=9))
BEGINNING_DATE = datetime.strptime(os.environ.get("BEGINNING_DATE"), DATE_FORMAT).date()
