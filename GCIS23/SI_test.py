import pytest

from SI_example import password_checker

def test_non_empty_password():
    assert password_checker("password123") is False

def test_empty_password():
    assert password_checker("") is False

def test_whitespace_password():
    assert password_checker("   ") is False

def test_special_characters_password():
    assert password_checker("!@#$%^&*()") is False

def test_numeric_password():
    assert password_checker("123456") is False

def test_single_character_password():
    assert password_checker("A") is False
    assert password_checker("1") is False


def test_valid_passwords():
    assert password_checker("abcdefgh") == False
    assert password_checker("abc12345") == False
    assert password_checker("Abcdefghij123!") == True
    assert password_checker("Abcd123!efghijklmnop") == True
    assert password_checker("Password123!") == True
    assert password_checker("Secure!1234") == True
    assert password_checker("MyPass1!") == True
    assert password_checker("A1!bcdef") == True
    assert password_checker("SecurePassword123!") == True
    

def test_invalid_passwords():
    assert password_checker("abcde12345!fg") == False
    assert password_checker("abc") == False
    assert password_checker("abcdefg") == False
    assert password_checker("12345678!") == False
    assert password_checker("Abcdefgh") == False
    assert password_checker("Password") == False
    assert password_checker("password123") == False
    assert password_checker("PASSWORD123!") == False
    assert password_checker("12345678!") == False
    assert password_checker("@#$%^&*") == False
    assert password_checker("!!!@@@!!!") == False

def test_edge_cases():
    assert password_checker("A1!bcdef") == True  # Minimum valid
    assert password_checker("abc") == False  # Too short
    assert password_checker("12345678!") == False  # No letters
    assert password_checker("!@#$%^&*") == False  # No letters or digits

def test_stress_cases():
    assert password_checker("A1!abcdefghijklmnoqt") == True  # Long valid
    assert password_checker("A1!abcdefghijklmnoqrst") == False  # Long invalid

if __name__ == "__main__":
    pytest.main()