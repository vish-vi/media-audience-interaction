import sqlite3

def output_results():
    conn = sqlite3.connect('news_analysis.db')
    c = conn.cursor()
    c.execute('SELECT topic, title, emotion_overall, emotion_score_overall FROM articles')
    results = c.fetchall()
    with open("output.txt", "w", encoding="utf-8") as f:
        
        for topic, title, emotion_overall, emotion_score_overall in results:
            f.write(f"Topic: {topic}\n")
            f.write(f"Title: {title}\n")
            f.write(f"Emotion Overall: {emotion_overall}\n")
            f.write(f"Emotion Score Overall: {emotion_score_overall}\n")
            f.write("---\n")
    conn.close()