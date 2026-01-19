import sqlite3

# Connect to database
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS data_store (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data TEXT UNIQUE
)
""")
conn.commit()

def insert_data(value):
    try:
        cursor.execute("INSERT INTO data_store (data) VALUES (?)", (value,))
        conn.commit()
        print("Data inserted successfully (Unique)")
    except sqlite3.IntegrityError:
        print("Duplicate data detected. Insert Failed.")

while True:
    user_input = input("Enter data (type exit to quit): ")
    if user_input.lower() == "exit":
        break
    insert_data(user_input)

conn.close()