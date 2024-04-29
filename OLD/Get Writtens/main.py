inputFolder = "Inputs"
outputFolder = "Outputs"

orderedNames = open(inputFolder + "/orderedNames.txt", "r").readlines()
inputNames = open(inputFolder + "/names.txt", "r").readlines()
inputScores = open(inputFolder + "/scores.txt", "r").readlines()

outputScores = open(outputFolder + "/scores.txt", "w")
missingScores = open(outputFolder + "/missing.txt", "w")

orderedScores = {}

def main():
    Prepare()
    AddToOrdered()
    WriteToFile()
    outputScores.close()
    missingScores.close()

def Prepare():
    for key, name in enumerate(orderedNames):
        orderedNames[key] = name.strip().lower()
    
    for key, name in enumerate(inputNames):
        inputNames[key] = name.strip()
    
    for key, score in enumerate(inputScores):
        inputScores[key] = score.strip()

def AddToOrdered():
    for key, name in enumerate(inputNames):
        if name.lower() in orderedNames: # found username in ordered list
            i = orderedNames.index(name.lower())
            if i in orderedScores: # if already there
                if int(orderedScores[i]) > int(inputScores[key]): # if new score is lower, edit value
                    orderedScores[i] = inputScores[key]
            else:
                orderedScores[i] = inputScores[key] # puts score into orderedScores in the same index that the username is in orderedNames
        else: # not found in ordered list
            print(name + " is missing.")
            missingScores.write(name + " | " + inputScores[key] + "\n") # write directly to missingScores

def WriteToFile():
    counter = 0
    while counter <= len(orderedNames):
        if counter in orderedScores:
            outputScores.write(orderedScores[counter] + "\n")
        else:
            outputScores.write("\n")
        counter += 1

if __name__ == "__main__":
    main()
