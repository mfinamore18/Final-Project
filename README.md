# Restaurant Order Splitter & Tip Calculator 🍽️
## Video Demo: 

The **Restaurant Order Splitter & Tip Calculator** is a Python application that enables one to share restaurant bills with friends and calculate tips with ease. The application provides a smooth experience with **user authentication** to enable users to **register and log in** prior to using the calculator. It additionally securely stores user credentials in a **SQLite database**.

This project was designed to address the common challenges faced by groups dining together—calculating each person's share, ensuring fair tip distribution, and making the process smooth and error-free. With a simple **command-line interface**, users can enter their total bill, the number of people sharing it, and their desired tip percentage to get a clear breakdown of individual costs.

## Features
- **User Registration & Login:** Users must create an account and log in before accessing the bill calculator.
- **Secure Data Storage:** Usernames and passwords are stored in a **SQLite database**.
- **Bill Splitting:** The total bill is evenly divided among the specified number of people.
- **Tip Calculation:** Users can input a tip percentage, which is added to the bill.
- **Individual Payment Calculation:** Each person's share (including the tip) is displayed.
- **Error Handling:** The program prevents invalid inputs such as division by zero and negative tip percentages.

## File Structure

### `project.py`
This is the **main program file**, containing all the core functionalities of the project:
- **User Authentication Functions:**
  - `create_users_table()`: Creates a SQLite database and users table if it doesn’t exist.
  - `register_user(username, password)`: Adds a new user to the database.
  - `login_user(username, password)`: Authenticates a user by checking credentials.
- **Bill Calculation Functions:**
  - `split_bill(total_amount, num_people)`: Divides the bill evenly among participants.
  - `calculate_tip(total_bill, tip_percentage)`: Computes the tip based on a given percentage.
  - `calculate_individual_share(total_bill, tip, num_people)`: Determines each person's total amount to pay, including the tip.
- **Main Function:**
  - `main()`: Runs the command-line interface, handling user input and calculations.

### `test_project.py`
This file contains **unit tests** using the `pytest` framework to verify the correctness of each function:
- `test_split_bill()`: Ensures proper division of the bill.
- `test_calculate_tip()`: Verifies that the tip amount is computed accurately.
- `test_calculate_individual_share()`: Checks that the total share per person is correct.
- `test_user_registration_and_login()`: Tests the authentication system, ensuring that users can register and log in with valid credentials while rejecting invalid ones.

### `requirements.txt`
Lists the external dependencies required for the project:
```
pytest
```
Since the project primarily uses built-in Python libraries (`sqlite3` for database management), only `pytest` is listed for running tests.

### `users.db`
This **SQLite database** file is created automatically when the program runs. It stores user credentials securely.

## Design Decisions

### 1. **Why Use SQLite for Authentication?**
Rather than storing user credentials in a plain text file, I opted for **SQLite**, which provides a structured and scalable way to handle authentication data. It ensures that usernames remain unique and allows for future expansions, such as storing user transaction history.

## Use of AI Assistance
In this ultimate project, AI-powered tools like **ChatGPT & CS50 duck** were used to enhance productivity and efficiency. These tools were employed as **helpers** in the process of code organization, debugging, and documentation. Nonetheless, the **brain behind the work is original**, and AI tools were employed to augment problem-solving capability, not a substitute for human labor.

## Future Enhancements
This project provides a solid foundation for expansion. Here are some potential improvements:
- **Password Encryption:** Implement hashing techniques to store passwords securely.
- **GUI Interface:** Build a graphical user interface using **Tkinter** or **Streamlit**.
- **User Transaction History:** Store past bill splits and allow users to retrieve them later.
- **Multi-Currency Support:** Enable bill calculations in different currencies using real-time exchange rates.

## How to Run the Project
### 1. Install Dependencies
Ensure you have Python installed and run:
```sh
pip install pytest
```

### 2. Run the Program
```sh
python project.py
```
- If it's your first time using the program, **register an account**.
- Log in with your credentials.
- Enter the bill amount, number of people, and tip percentage.
- View the calculated results.

### 3. Run Tests
To ensure all functions work correctly, execute:
```sh
pytest test_project.py
```

## Conclusion
This project is a practical tool that simplifies group dining by automating bill splitting and tip calculations. With **user authentication**, **error handling**, and a **structured database**, it demonstrates fundamental Python skills learning in class 🚀

# Example

![Screenshot 2025-03-02 at 1 50 24 AM](https://github.com/user-attachments/assets/d2f22f6f-3682-48c1-a7d5-03b230975017)


![Screenshot 2025-03-02 at 1 49 57 AM](https://github.com/user-attachments/assets/a507a6a7-c0c4-4d5e-ba34-ab4c9a0939b8)
