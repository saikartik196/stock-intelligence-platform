from pathlib import Path

# Project root
BASE_DIR = Path(__file__).resolve().parent.parent

# Data folders
DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

# Files
PRICE_FILE = RAW_DATA_DIR / "Dow_Jones_OHLC.csv"
NEWS_FILE = RAW_DATA_DIR / "Dow_Jones_News.csv"