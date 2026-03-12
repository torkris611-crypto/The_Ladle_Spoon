import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN не найден в .env файле")

# ID администратора (Антона) из .env
ADMIN_ID = int(os.getenv("ADMIN_ID", "0"))
if ADMIN_ID == 0:
    raise ValueError("ADMIN_ID не найден в .env файле")

# Пути к файлам
BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"
MENU_FILE = DATA_DIR / "menu.json"
ORDERS_FILE = DATA_DIR / "orders.json"
USERS_FILE = DATA_DIR / "users.json"
BLACKLIST_FILE = DATA_DIR / "blacklist.json"
REVIEWS_FILE = DATA_DIR / "reviews.json"

# Временные слоты для получения заказов
TIME_SLOTS = [
    "12:00-12:30",
    "12:30-13:00",
    "13:00-13:30",
    "13:30-14:00"
]

# Константы из .env или значения по умолчанию
MAX_MISSED_PICKUPS = int(os.getenv("MAX_MISSED_PICKUPS", "3"))
REMINDER_HOURS = int(os.getenv("REMINDER_HOURS", "2"))