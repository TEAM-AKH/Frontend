import sqlite3
from werkzeug.security import generate_password_hash

def update_admin_credentials(new_username, new_password):
    conn = sqlite3.connect('instance/data.db')
    cursor = conn.cursor()

    hashed_password = generate_password_hash(new_password)

    # Update the admin user (assuming admin user has id=1 or a specific username)
    # For simplicity, we'll update the user with the old username 'admin'
    cursor.execute("UPDATE user SET username = ?, password_hash = ? WHERE username = ?",
                   (new_username, hashed_password, 'admin'))
    conn.commit()
    conn.close()
    print(f"Admin credentials updated: Username='{new_username}', Password='{new_password}'")

if __name__ == '__main__':
    new_username = 'acknowledgementhub'
    new_password = 'ack@admin'
    update_admin_credentials(new_username, new_password)