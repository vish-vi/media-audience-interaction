import numpy as np
import re
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import database

analyzer = SentimentIntensityAnalyzer()

def split_into_sentences(text):
    if not text:
        return []
    # Basic sentence splitter using regex
    sentences = re.split(r'(?<=[.!?])\s+', text)
    return [s.strip() for s in sentences if s.strip()]

def get_vader_scores(text):
    if not text:
        return None
    return analyzer.polarity_scores(text)

def get_analysis_results(conn, article_id):
    text = database.get_article_text(conn, article_id)
    
    # Calculate word count and update if necessary
    # Note: You can add word_count to your update query if you want to store it!
    
    emotion_overall = get_emotion_overall(text)
    emotion_score_overall = get_emotion_score_overall(text)
    emotion_positive_score = get_emotion_positive_score(text)
    emotion_negative_score = get_emotion_negative_score(text)
    emotion_dispersion = get_emotion_dispersion(text)
    
    database.update_article_analysis(conn, article_id, emotion_overall, emotion_score_overall, emotion_positive_score, emotion_negative_score, emotion_dispersion)

def get_emotion_overall(text):
    scores = get_vader_scores(text)
    if not scores: return "Neutral"
    if scores['compound'] >= 0.05: return "Positive"
    elif scores['compound'] <= -0.05: return "Negative"
    return "Neutral"

def get_emotion_score_overall(text):
    scores = get_vader_scores(text)
    return scores['compound'] if scores else 0.0

def get_emotion_positive_score(text):
    scores = get_vader_scores(text)
    return scores['pos'] if scores else 0.0

def get_emotion_negative_score(text):
    scores = get_vader_scores(text)
    return scores['neg'] if scores else 0.0

def get_emotion_dispersion(text):
    sentences = split_into_sentences(text)
    if len(sentences) < 2:
        return 0.0
    
    # Get the compound score for every individual sentence
    sentence_scores = [analyzer.polarity_scores(s)['compound'] for s in sentences]
    
    # Variance measures the statistical spread/dispersion of emotion across sentences
    variance = np.var(sentence_scores)
    return float(variance)


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
