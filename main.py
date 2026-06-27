import analyzer
from pprint import pprint
from generator import suggest_password
from database import check_previous_password

print("Password Strength Analyzer")
menu = """
1. Analyze a password
2. Exit
"""
run = True

while run:
    print(menu)
    choice = input("Enter your choice: ")
    match choice:
        case "1":
            password = input("Enter the password to analyze: ")
            result = analyzer.analyze_password_strength(password)
            pprint(result)
            
            match result["OverallScore"]:
                case score if score >= 80:
                    print("Password Strength: Strong")
                case score if score >= 50:
                    print("Password Strength: Moderate")
                case score if score >= 30:
                    print("Password Strength: Weak")
                case _:
                    print("Password Strength: Very Weak")
            if score <= 30 or result["CharacterAnalysis"]["score"] != 4:
                suggest_password(password)
            print("Time to crack at 100 billion guesses/sec")
            print(result["TTC"])
            
            check_previous_password(password)
            
        case "2":
            run = False
        case _:
            print("Invalid choice. Please try again.")