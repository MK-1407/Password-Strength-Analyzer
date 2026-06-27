import re, math

MAX_SCORE = 75

def _length_analysis(password):
    """
    Analyzes the length of the password and returns a score based on its length.

    Args:
        password (str): The password to analyze.
        """
    match len(password):
        case length if length < 8:
            return 0
        case length if 8 <= length < 12:
            return 8
        case length if 12 <= length < 16:
            return 12
        case length if length >= 16:
            return 16

def _character_analysis(password):
    """Analyzes the character diversity of the password and returns a score based on its diversity
    
    Args:
        password (str): The password to analyze
    """
    lowercase = bool(re.search(r'[a-z]',password))
    uppercase = bool(re.search(r'[A-Z]',password))
    digits = bool(re.search(r'[0-9]',password))
    special = bool(re.search(r'[!@#$%^&*()_+\-=\[\]{};:"\\|,.<>/?~]', password))
    score = sum([lowercase, uppercase, digits, special])
    return {
        "lowercase":lowercase,
        "uppercase":uppercase,
        "digits":digits,
        "special":special,
        "score":score
    }

def _entropy_analysis(password):
    """Calculates the entropy of the password based on its length and character diversity.
    
    Args:
        password (str): The password to analyze.
    Returns:
        float: The entropy of the password.
    """
    pool_size = 0

    if re.search(r'[a-z]', password):
        pool_size += 26

    if re.search(r'[A-Z]', password):
        pool_size += 26

    if re.search(r'[0-9]', password):
        pool_size += 10

    if re.search(r'[!@#$%^&*()_+\-=\[\]{};:"\\|,.<>/?~]', password):
        pool_size += 32

    if pool_size == 0:
        return 0

    entropy = len(password) * math.log2(pool_size)

    unique_ratio = len(set(password)) / len(password)

    if unique_ratio < 0.2:
        entropy *= 0.3
    elif unique_ratio < 0.4:
        entropy *= 0.6
    elif unique_ratio < 0.6:
        entropy *= 0.8

    return entropy

def _score_calculator(scores: dict) -> float:
    """Calculates the overall score of the password based on its length, character diversity, and entropy.
    
    Args:
        scores (dict): A dictionary containing the scores for each analysis.
    Returns:
        float: The overall score of the password.
    """
    length_score = (
        scores["LengthAnalysis"] / 16
    ) * 30

    character_score = (
        scores["CharacterAnalysis"] / 4
    ) * 40

    entropy_score = (
        min(scores["EntropyAnalysis"], 80) / 80
    ) * 30

    score = (
        length_score
        + character_score
        + entropy_score
    )

    if scores["CharacterAnalysis"] == 1:
        score *= 0.5

    score = max(0, min(score, 100))

    return round(score, 2)

def estimate_crack_time(entropy: float,
                        guesses_per_second: float = 1e11):
    """Estimates the time it would take to crack a password based on its entropy and the number of guesses per second.
    
    args:
        entropy (float): The entropy of the password.
        guesses_per_second (float): The number of guesses per second. Default is 1e11 (100 billion).
    Returns:
        str: A string representation of the estimated time to crack the password in years, days, hours, minutes, or seconds.
    """

    seconds = (2 ** entropy) / (2 * guesses_per_second)

    units = [
        ("years", 31536000),
        ("days", 86400),
        ("hours", 3600),
        ("minutes", 60),
        ("seconds", 1)
    ]

    for name, value in units:
        if seconds >= value:
            return f"{seconds / value:.2e} {name}"

    return f"{seconds:.2f} seconds"

def analyze_password_strength(password: str) -> dict:
    """
    Analyzes the strength of a password based on its length and character diversity.

    Args:
        password (str): The password to analyze.
    Returns:
        dict: A dictionary containing the analysis results, including length score, character diversity score, and overall strength score.
    """
    length_score = _length_analysis(password)
    character_analysis = _character_analysis(password)
    character_score = character_analysis.get('score')
    entropy_score = _entropy_analysis(password)
    
    time_to_crack = estimate_crack_time(entropy=entropy_score)
    
    scores = {
        "LengthAnalysis": length_score,
        "CharacterAnalysis": character_score,
        "EntropyAnalysis": entropy_score
    }
    
    overall_score = _score_calculator(scores)
    
    return {
        "LengthAnalysis": length_score,
        "CharacterAnalysis": character_analysis,
        "EntropyAnalysis": entropy_score,
        "OverallScore": overall_score,
        "TTC":time_to_crack
    }
