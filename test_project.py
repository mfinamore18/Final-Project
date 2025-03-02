import pytest
import sqlite3
from project import split_bill, calculate_tip, calculate_individual_share, register_user, login_user, create_users_table

def test_split_bill():
    assert split_bill(100, 4) == 25.00
    assert split_bill(75.5, 3) == 25.17
    with pytest.raises(ValueError):
        split_bill(100, 0)

def test_calculate_tip():
    assert calculate_tip(100, 15) == 15.00
    assert calculate_tip(50, 10) == 5.00
    with pytest.raises(ValueError):
        calculate_tip(100, -5)

def test_calculate_individual_share():
    assert calculate_individual_share(100, 15, 4) == 28.75
    assert calculate_individual_share(50, 5, 2) == 27.50
    with pytest.raises(ValueError):
        calculate_individual_share(100, 15, 0)

def test_user_registration_and_login():
    create_users_table()
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users") 
    conn.commit()
    conn.close()

    register_user("testuser", "password123")
    assert login_user("testuser", "password123") is True
    assert login_user("wronguser", "password123") is False
    assert login_user("testuser", "wrongpassword") is False
