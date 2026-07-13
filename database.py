import sqlite3


conn = sqlite3.connect("passwords.db")
cursor = conn.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS passwords(
    
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    website TEXT,
    username TEXT,
    password TEXT    
    )
    """
)


def save_data(website, username, password):

    cursor.execute(
        """
        INSERT INTO passwords(website, username, password) VALUES(?, ?, ?)
        """,
        (website, username, password)
    )
    conn.commit()


def delete_password(del_id):
    cursor.execute(
        """
        DELETE FROM passwords WHERE id = ?
        
        """,
        (del_id,)
    )
    conn.commit()

    rowcount = cursor.rowcount

    if rowcount == 0:
        print("No password found with this ID.")
    else:
        print("Password deleted successfully.")


def update_password(record_id, website, username, password):
    cursor.execute(
        """
        UPDATE passwords SET website=?, username=?, password=? WHERE id=?
        
        """,
        (website, username, password, record_id)
    )
    conn.commit()

    rowcount = cursor.rowcount

    if rowcount == 0:
        print("No password found with this ID.")
    else:
        print("Password update successfully.")


def data():
    cursor.execute("SELECT id, website, username, password FROM passwords")
    passwords = cursor.fetchall()
    return passwords


def search(keyword):
    cursor.execute(
        """
        SELECT id, website, username, password FROM passwords WHERE website LIKE ?
        """,
        (f"%{keyword}%",)
    )
    results = cursor.fetchall()
    return results


def copy_password(cop_id):
    cursor.execute(
        """
        SELECT password FROM passwords WHERE id = ?
        """,
        (cop_id,)
    )
    password = cursor.fetchone()
    return password
