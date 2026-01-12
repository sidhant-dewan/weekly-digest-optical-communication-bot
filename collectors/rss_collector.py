import feedparser
import requests
from readability import Document
from bs4 import BeautifulSoup
from dateutil import parser as dateparser
from datetime import datetime


def extract_text(url):
    try:
        html = requests.get(url, timeout=10).text
        doc = Document(html)
        soup = BeautifulSoup(doc.summary(), "html.parser")
        return soup.get_text(separator=" ", strip=True)
    except Exception:
        return ""


def fetch_rss(source):
    feed = feedparser.parse(source["url"])
    articles = []

    for entry in feed.entries:
        url = entry.get("link")
        title = entry.get("title", "").strip()

        published = entry.get("published", None)
        if published:
            published = dateparser.parse(published).isoformat()

        text = extract_text(url)

        articles.append({
            "title": title,
            "url": url,
            "source": source["name"],
            "published_at": published,
            "first_seen_at": datetime.utcnow().isoformat(),
            "raw_text": text
        })

    return articles
