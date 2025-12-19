import re

common_passwords = {
    "password", "123456", "123456789", "12345678", "12345",
    "qwerty", "abc123", "password1", "iloveyou", "welcome",
    "admin", "letmein", "monkey", "sunshine", "princess",
    "football", "baseball", "123123", "654321", "password123"
}

def check_password_strength(password):
    if not password.strip():
        return "Password cannot be empty"
    
    password = password.strip()
    score = 0

    if password.lower in {p.lower() for p in common_passwords}:
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

#Tips for user to improve password
def improvementSuggestions(password):
    missing = []

    if not re.search(r"[A-Z]", password):
        missing.append("uppercase letters")
    if not re.search(r"[a-z]", password):
        missing.append("lowercase letters")
    if not re.search(r"[0-9]", password):
        missing.append("numbers")
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        missing.append("special characters")

    if missing:
        return ", please include " + ", ".join(missing) + " in your password."
    return ""

#Main Loop
print("Password Strength Checker (type 'quit' to exit)\n")
while True:
    password = input("Enter a password to check its strength (or 'quit' to exit): ")
    if password.lower() == 'quit':
        print("Exiting Password Strength Checker. Goodbye!")
        break



    
    strength = check_password_strength(password)
    suggestion = improvementSuggestions(password)
    print("Your password is:", strength + suggestion)
