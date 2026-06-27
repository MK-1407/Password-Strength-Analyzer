import secrets
import string

def _strengthen_password(password):
    """Suggests alternative strong password based on any given password
    
    args:
        password (str): the password to analyze
    Returns:
        A strong password basede on orignal password
    """
    chars = list(password)

    # Random capitalization
    for i in range(len(chars)):
        if secrets.randbelow(2):
            chars[i] = chars[i].upper()

    # Insert random characters at random positions
    for _ in range(4):
        pos = secrets.randbelow(len(chars) + 1)
        chars.insert(
            pos,
            secrets.choice(
                string.ascii_letters +
                string.digits +
                "!@#$%^&*"
            )
        )

    return "".join(chars)

def suggest_password(password):
    print(f"""
          Suggested Passwords:
          1. {_strengthen_password(password)}
          2. {_strengthen_password(password)}
          3. {_strengthen_password(password)}
          4. {_strengthen_password(password)}
          5. {_strengthen_password(password)}
          """)