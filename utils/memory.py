
import sqlite3

conn = sqlite3.connect('memory.db')
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS memory (prompt TEXT, expanded TEXT)")
conn.commit()

def save_to_memory(prompt, expanded):
    cursor.execute("INSERT INTO memory (prompt, expanded) VALUES (?, ?)", (prompt, expanded))
    conn.commit()

def retrieve_from_memory(prompt):
    cursor.execute("SELECT expanded FROM memory WHERE prompt = ?", (prompt,))
    return cursor.fetchone()
