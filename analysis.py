import sqlite3
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

import database

analyzer = SentimentIntensityAnalyzer()

def get_vader_scores(text):
    if not text:
        return None
    return analyzer.polarity_scores(text)

def get_analysis_results(conn, article_id):
    text = database.get_article_text(conn, article_id)
    emotion_overall = get_emotion_overall(text)
    emotion_score_overall = get_emotion_score_overall(text)
    emotion_positive_score = get_emotion_positive_score(text)
    emotion_negative_score = get_emotion_negative_score(text)
    emotion_dispersion = get_emotion_dispersion(text)
    database.update_article_analysis(conn, article_id, emotion_overall, emotion_score_overall, emotion_positive_score, emotion_negative_score, emotion_dispersion)


def word_count(text):
    return len(text.split()) if text else 0

def get_emotion_overall(text):
    pass

def get_emotion_score_overall(text):
    pass

def get_emotion_positive_score(text):
    pass

def get_emotion_negative_score(text):
    pass

def get_emotion_dispersion(text):
    pass    



'''
class article:
    title
    date 
    no. of words
    source
    topic
    url

    emotion_overall
    emotion_score_overall
    emotion_positive_score
    emotion_negative_score
    e




'''