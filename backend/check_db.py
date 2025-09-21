import sqlite3

def check_database():
    conn = sqlite3.connect('instance/data.db')
    cursor = conn.cursor()

    print("\n--- Events ---")
    cursor.execute("SELECT id, title, description FROM event")
    events = cursor.fetchall()
    for event in events:
        print(event)

    print("\n--- Products ---")
    cursor.execute("SELECT id, name, details FROM product")
    products = cursor.fetchall()
    for product in products:
        print(product)

    conn.close()

if __name__ == '__main__':
    check_database()