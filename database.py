import sqlite3

def create_database():
    conn = sqlite3.connect('news_analysis.db')
    c = conn.cursor()
    
    c.execute('''
        CREATE TABLE IF NOT EXISTS articles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            date TEXT,
            word_count INTEGER,
            source TEXT,
            topic TEXT,
            url TEXT,
            emotion_overall TEXT,
            emotion_score_overall REAL,
            emotion_positive_score REAL,
            emotion_negative_score REAL,
            description TEXT,
            content TEXT,
            emotion_dispersion REAL
        )
    ''')
    
    conn.commit()
    conn.close()

def insert_article(conn, topic, title, description, content, source, url, date):
    c = conn.cursor()
    c.execute('''
        INSERT INTO articles (topic, title, description, content, source, url, date)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (topic, title, description, content, source, url, date))
    conn.commit()
    return c.lastrowid

def update_article_analysis(conn, article_id, emotion_overall, emotion_score_overall, emotion_positive_score, emotion_negative_score, emotion_dispersion):
    c = conn.cursor()
    c.execute('''
        UPDATE articles
        SET emotion_overall = ?, emotion_score_overall = ?, emotion_positive_score = ?, emotion_negative_score = ?, emotion_dispersion = ?
        WHERE id = ?
    ''', (emotion_overall, emotion_score_overall, emotion_positive_score, emotion_negative_score, emotion_dispersion, article_id))
    conn.commit()