# Password Strength Analyzer

## _character_analysis

Analyzes the character diversity of the password and returns a score based on its diversity

Args:
    password (str): The password to analyze

## _entropy_analysis

Calculates the entropy of the password based on its length and character diversity.

Args:
    password (str): The password to analyze.
Returns:
    float: The entropy of the password.

## _length_analysis

Analyzes the length of the password and returns a score based on its length.

Args:
    password (str): The password to analyze.
    

## _score_calculator

Calculates the overall score of the password based on its length, character diversity, and entropy.

Args:
    scores (dict): A dictionary containing the scores for each analysis.
Returns:
    float: The overall score of the password.

## analyze_password_strength

Analyzes the strength of a password based on its length and character diversity.

Args:
    password (str): The password to analyze.
Returns:
    dict: A dictionary containing the analysis results, including length score, character diversity score, and overall strength score.

## estimate_crack_time

Estimates the time it would take to crack a password based on its entropy and the number of guesses per second.

args:
    entropy (float): The entropy of the password.
    guesses_per_second (float): The number of guesses per second. Default is 1e11 (100 billion).
Returns:
    str: A string representation of the estimated time to crack the password in years, days, hours, minutes, or seconds.

