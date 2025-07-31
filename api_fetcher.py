import os
import requests
from dotenv import load_dotenv

load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
NEWS_API_ENDPOINT = "https://newsapi.org/v2/everything"


def fetch_articles(query, language="en", page_size=5):
    if not NEWS_API_KEY:
        raise ValueError("NEWS_API_KEY not found in environment variables.")

    params = {
        "q": query,
        "apiKey": NEWS_API_KEY,
        "language": language,
        "pageSize": page_size,
    }

    response = requests.get(NEWS_API_ENDPOINT, params=params)
    if response.status_code == 200:
        articles = response.json().get("articles", [])
        return articles
    else:
        raise Exception(f"News API request failed: {response.status_code} {response.text}")
