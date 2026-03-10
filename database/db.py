import sqlite3

conn = sqlite3.connect("trend_engine.db")

cursor = conn.cursor()

cursor.execute("""

CREATE TABLE IF NOT EXISTS trends(

id INTEGER PRIMARY KEY AUTOINCREMENT,

keyword TEXT,

score REAL

)

""")

def save(keyword,score):

    cursor.execute(

        "INSERT INTO trends(keyword,score) VALUES(?,?)",

        (keyword,score)

    )

    conn.commit()
