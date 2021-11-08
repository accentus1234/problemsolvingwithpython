def started(msg=""):
    print("--------------------------------------------------")
    print("Operation started: {msg}...\n")

def completed():
    print("\n\nOperation Completed")
    print("--------------------------------------------------")

def error(msg):
    print("Error! {msg}")

def menu():
    print(f"""Please select one of the following options:
    {"[years]":<10} List unique years
    {"[tally]":<10} Tally up medals
    {"[team]":<10} Tally up medals for each team
    {"[exit]":<10} Exit the program
    """)
    selection = input("Your selection: ")
    return selection.strip().lower()

def display_medal_tally(tally):
    tally = {"Gold": 10, "Silver": 5, "Bronze": 2}
    for key, value in tally.items():
        print(f"{key}: {value}")

def display_medal_tally(team_tally):
    team_tally = {}