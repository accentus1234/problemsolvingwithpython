def short_pattern():
    pattern = {"sequence":"101", "occurrences":5}
    return pattern

def medium_pattern():
    pattern = {"sequence":"111000", "occurrences": 25}
    return pattern

def long_pattern():
    pattern = {"sequence":"1100110011001100", "occurrences":50}
    return pattern

def run():
    print("Analysing patterns...")
    patterns = {"short_pattern":short_pattern(),"medium_pattern":medium_pattern(),"long_pattern":long_pattern()}
    
    for key, value in patterns.items():
        print(f"{key}: {value}")

run()