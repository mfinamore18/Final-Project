import sqlite3

def create_users_table():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def register_user(username: str, password: str):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        print("User registered successfully!")
    except sqlite3.IntegrityError:
        print("Username already exists. Try a different one.")
    finally:
        conn.close()

def login_user(username: str, password: str) -> bool:
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    conn.close()
    return user is not None

def split_bill(total_amount: float, num_people: int) -> float:
    if num_people <= 0:
        raise ValueError("Number of people must be greater than zero.")
    return round(total_amount / num_people, 2)

def calculate_tip(total_bill: float, tip_percentage: float) -> float:
    if tip_percentage < 0:
        raise ValueError("Tip percentage cannot be negative.")
    return round(total_bill * (tip_percentage / 100), 2)

def calculate_individual_share(total_bill: float, tip: float, num_people: int) -> float:
    if num_people <= 0:
        raise ValueError("Number of people must be greater than zero.")
    return round((total_bill + tip) / num_people, 2)

def main():
    create_users_table()
    print("Welcome to the Restaurant Order Splitter & Tip Calculator!")
    choice = input("Do you have an account? (yes/no): ").strip().lower()

    if choice == "no":
        username = input("Choose a username: ")
        password = input("Choose a password: ")
        register_user(username, password)
    
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if login_user(username, password):
        print("Login successful! Proceeding with bill splitting...")
        try:
            total_bill = float(input("Enter the total bill amount: "))
            num_people = int(input("Enter the number of people: "))
            tip_percentage = float(input("Enter the tip percentage: "))

            tip = calculate_tip(total_bill, tip_percentage)
            individual_share = calculate_individual_share(total_bill, tip, num_people)

            print(f"Total Tip: ${tip}")
            print(f"Each person should pay: ${individual_share}")
        except ValueError as e:
            print(f"Error: {e}")
    else:
        print("Login failed. Please check your username and password.")

if __name__ == "__main__":
    main()