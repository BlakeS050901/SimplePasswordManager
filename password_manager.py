import string
import random
import json

PASSWORDS_FILE = "passwords.json"

def create_password(num_chars, allowed_chars):
    """
    Generates a random password.

    Parameters:
        num_chars (int): the number of characters the password should contain
        allowed_chars (str): a string of characters allowed in the password

    Returns:
        str: a randomly generated password
    """
    chars = allowed_chars.replace(" ", "")
    password = "".join(random.choice(chars) for _ in range(num_chars))
    return password

def store_password(website, password):
    """
    Stores a website and its corresponding password in a dictionary and saves it to a file.

    Parameters:
        website (str): the name of the website
        password (str): the password for the website
    """
    passwords = {}
    try:
        with open(PASSWORDS_FILE, "r") as f:
            passwords = json.load(f)
    except FileNotFoundError:
        pass

    passwords[website] = password

    with open(PASSWORDS_FILE, "w") as f:
        json.dump(passwords, f)

def view_passwords():
    """
    Returns a list of tuples containing the stored website and password pairs.

    Returns:
        list: a list of tuples representing website-password pairs
    """
    passwords = {}
    try:
        with open(PASSWORDS_FILE, "r") as f:
            passwords = json.load(f)
    except FileNotFoundError:
        pass

    pairs = [(website, password) for website, password in passwords.items()]
    return pairs
