import getnews
import analysis
import output
import database
import sqlite3

database.create_database()

# Topic A
topic_1 = "artificial intelligence"
ids_1 = getnews.get_articles(topic_1, count=15)

# Topic B
topic_2 = "climate change"
ids_2 = getnews.get_articles(topic_2, count=15)

# Process all of them
conn = sqlite3.connect('news_analysis.db')
for aid in ids_1 + ids_2:
    analysis.get_analysis_results(conn, aid)
conn.close()

# Compare them
metrics = comparison.analyze_topic_comparison(topic_1, topic_2)
comparison.print_comparison_report(metrics, topic_1, topic_2)



'''
import requests 
import os
from dotenv import load_dotenv
import sqlite3


# Load environment variables from .env file
load_dotenv()

API_KEY = os.getenv('NEWS_API_KEY')

def get_articles(topic, count=10, file=None):
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": topic,
        "pageSize": count,
        "apiKey": API_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()

    articles = []
    for i, article in enumerate(data["articles"], start=1):
        articles.append(article)
        file.write(f"\nArticle {i}\n")
        file.write(f"Source: {article['source']['name']}\n")
        file.write(f"Author: {article['author']}\n")
        file.write(f"Title: {article['title']}\n")
        file.write(f"Description: {article['description']}\n")
        file.write(f"URL: {article['url']}\n")
        file.write(f"Published: {article['publishedAt']}\n")
        file.write(f"Content: {article['content']}\n")
        file.write(f"\n")
        file.write(f"Title Word Count: {word_count(article['title'])}\n")
        file.write(f"Description Word Count: {word_count(article['description'])}\n")
        file.write(f"Word Count: {word_count(article['content'])}\n")
        file.write("---\n")

    return articles


#word_count = lambda text: len(text.split()) if text else 0

topics = ["prediction market", "gambling"] #, "sports betting", "stock market", "cryptocurrency", "scams"]

with open("output.txt", "w", encoding="utf-8") as f:
    for topic in topics:
        f.write(f"\n=== {topic.upper()} ===\n ")
        get_articles(topic, count=10, file=f)
'''
