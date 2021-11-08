def observed():
    observations = []
    
    for count in range(5):
        print("Enter an observation: ")
        observations.append(input())
    
    return observations

def remove_observations(observations):
    isRunning = True

    while(isRunning == True):
        choice = input("Would you like to remove any observations (Y/N)? ")
        if choice == "Y":
            toRemove = str(input("Please enter the string you would like to remove: "))
            observations.remove(toRemove)
        else:
            isRunning = False
    return observations    

def run():
    observations = observed()
    remove_observations(observations)

    observations_set = set()
    for observation in observations:
        data = (observation, observations.count(observation))
        observations_set.add(data)

    print("Observations: ")
    for data in observations_set:
        print(f"{data[0]} observed {data[1]} times.")

run()

#Added code to demonstrate how to manipulate and sort a set.