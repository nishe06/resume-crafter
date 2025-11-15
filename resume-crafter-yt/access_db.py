import sqlite3

def view_all_users():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM user')
    users = cursor.fetchall()
    
    print(f"Total users: {len(users)}")
    for user in users:
        print(f"ID: {user[0]}, Username: {user[1]}, Email: {user[2]}")
    
    conn.close()

def search_user_by_username(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM user WHERE username = ?', (username,))
    user = cursor.fetchone()
    
    if user:
        print(f"Found user: ID={user[0]}, Username={user[1]}, Email={user[2]}")
    else:
        print(f"No user found with username: {username}")
    
    conn.close()

def search_user_by_email(email):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM user WHERE email = ?', (email,))
    user = cursor.fetchone()
    
    if user:
        print(f"Found user: ID={user[0]}, Username={user[1]}, Email={user[2]}")
    else:
        print(f"No user found with email: {email}")
    
    conn.close()

if __name__ == "__main__":
    print("=== DATABASE ACCESS ===")
    print("1. View all users")
    print("2. Search by username")
    print("3. Search by email")
    
    choice = input("Enter your choice (1-3): ")
    
    if choice == "1":
        view_all_users()
    elif choice == "2":
        username = input("Enter username to search: ")
        search_user_by_username(username)
    elif choice == "3":
        email = input("Enter email to search: ")
        search_user_by_email(email)
    else:
        print("Invalid choice!") 