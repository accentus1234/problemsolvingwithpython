def pattern():
    sequences = {"Short Sequence":3, "Medium Sequence":2, "Long Sequence":1}
    return sequences

def display_keys(data):
    for key in data:
        print(key)

def display_values(data):
    for value in data.values():
        print(value)

def display_items(data):
    for key, value in data.items():
        print(f"{key}: {value}")

def run():
    data = pattern()
    print(f"Dictionary:\n{data}")
    print("Keys: ")
    display_keys(data)
    print("Values: ")
    display_values(data)
    print("Pairs: ")
    display_items(data)    

run()

#"Added code to demonstrate how to iterate through a dictionary."