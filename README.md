# 🔐 Password Strength Analyzer

A Python-based password security toolkit that analyzes password strength, estimates entropy, predicts crack resistance, generates secure passwords, and detects password reuse through a local hash database.

## ✨ Features

- 📏 Password length analysis
- 🔤 Character diversity analysis
  - Uppercase letters
  - Lowercase letters
  - Numbers
  - Special characters
- 🧮 Entropy calculation
- ⏱️ Crack time estimation
- 🎯 Overall strength scoring
- 🎲 Secure password generation
- 🗄️ Password history tracking using hashed passwords
- 🐍 Modular and extensible Python codebase

---

## 📂 Project Structure

```text
Password-Strength-Analyzer/
│
├── analyzer.py      # Password analysis logic
├── generator.py     # Secure password generator
├── database.py      # Password history database operations
├── main.py          # Application entry point
└── README.md
```

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/MK-1407/Password-Strength-Analyzer.git
cd Password-Strength-Analyzer
```

Install any required dependencies:

```bash
pip install -r requirements.txt
```

If no requirements file exists, the project runs using Python standard libraries.

---

## ▶️ Usage

Run the application:

```bash
python main.py
```

Enter a password when prompted.

Example:

```text
Enter a password to analyze:
SWERFsdfgh23058[;l,
```

Example output:

```text
{
    'LengthAnalysis': 16,
    'CharacterAnalysis': {
        'lowercase': True,
        'uppercase': True,
        'digits': True,
        'special': True,
        'score': 4
    },
    'EntropyAnalysis': 124.53,
    'OverallScore': 100.0
}

Password Strength: Strong
```

---

## 🧠 How Strength Is Evaluated

The analyzer combines multiple metrics:

### Length Score
Longer passwords receive higher scores.

### Character Diversity
Checks whether the password contains:

- Uppercase letters
- Lowercase letters
- Numbers
- Special characters

### Entropy Analysis

Entropy estimates the randomness of a password using the available character set and password length.

Higher entropy generally means greater resistance to brute-force attacks.

### Crack Time Estimation

The analyzer estimates how long a brute-force attack may take based on the calculated entropy.

---

## 🎲 Password Generator

The built-in generator can create strong passwords containing:

- Uppercase letters
- Lowercase letters
- Numbers
- Symbols

Generated passwords are designed to maximize entropy and complexity.

---

## 🗄️ Password Reuse Detection

Passwords are hashed before storage and checked against a local database to determine whether a password has been used previously.

This helps encourage unique password usage.

---

## 🔒 Security Notes

This project is intended for educational and portfolio purposes.

For production-grade password storage, consider using:

- Argon2
- bcrypt
- scrypt

instead of fast hashing algorithms.

---

## 🛠️ Future Improvements

Potential enhancements:

- Common password detection
- Dictionary attack simulation
- Keyboard pattern detection
- Have I Been Pwned integration
- Exportable security reports
- GUI/Web interface

---

## 📜 License

This project is open source and available under the license chosen by the repository owner.

---

## 👨‍💻 Author

Created by **Mayank (MK-1407)**.
