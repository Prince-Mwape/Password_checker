import re

common_passwords = {
    "password", "123456", "123456789", "12345678", "12345",
    "qwerty", "abc123", "password1", "iloveyou", "welcome",
    "admin", "letmein", "monkey", "sunshine", "princess",
    "football", "baseball", "123123", "654321", "password123"
}

def check_password_strength(password):
    score = 0

    if password in common_passwords:
        return "Very weak! Very common password."

    if len(password) >= 8:
        score += 1
    else:
        return "Too short, should be at least 8 characters."

    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    if score >= 5:
        return "Strong"
    elif score >= 3:
        return "Moderate"
    else:
        return "Weak"


password = input("Please enter a password to verify its strength: ")
strength = check_password_strength(password)
print("Your password is:", strength)
