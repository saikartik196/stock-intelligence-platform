import pandas as pd
from src.config import PRICE_FILE, NEWS_FILE

print("Price path:", PRICE_FILE)
print("News path:", NEWS_FILE)

df_price = pd.read_csv(PRICE_FILE)
df_news = pd.read_csv(NEWS_FILE)

print(df_price.head())
print(df_news.head())