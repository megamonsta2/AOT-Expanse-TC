inputFolder = "Inputs"
outputFolder = "Outputs"

orderedNames = open(inputFolder + "/orderedNames.txt", "r").readlines()
inputScore = {
    "Dummies": open(inputFolder + "/Dummies.txt", "r").readlines(),
    "Muskets": open(inputFolder + "/Musket.txt", "r").readlines(),
    "Speed": open(inputFolder + "/Speed.txt", "r").readlines(),
} # {string: {USERNAME - SCORE}}

outputScore = {
    "Dummies": open(outputFolder + "/Dummies.txt", "w"),
    "Muskets": open(outputFolder + "/Musket.txt", "w"),
    "Speed": open(outputFolder + "/Speed.txt", "w"),
}
missingScores = open(outputFolder + "/missing.txt", "w")

divider = " - "
scores = {} # {USERNAME: {Musket: score, Speed: score, Dummies: score}}

def main():
    FormatScoreInput()
    AssignScores()
    CloseOutputs()

def FormatScoreInput():
    for test in inputScore:
        data = inputScore[test]

        for key, line in enumerate(data):
            line = line.strip()
            dividerIndex = line.find(divider)

            username = line[:dividerIndex]
            score = line[dividerIndex+len(divider):]

            if username.lower() not in scores:
                scores[username.lower()] = {test: score, "Username": username}
            else:
                if test in scores[username.lower()]:
                    if int(score) < int(scores[username.lower()][test]):
                        scores[username.lower()][test] = score
                else:
                    scores[username.lower()][test] = score

def AssignScores():
    for key, username in enumerate(orderedNames):
        loweredUsername = username.strip().lower()

        if loweredUsername in scores: # if username is in ordered list            
            for test in inputScore: # write every score to the txt files
                if test in scores[loweredUsername]: # has data for that test
                    outputScore[test].write(scores[loweredUsername][test] + "\n")
                else: # if no registered score, make it blank
                    outputScore[test].write("\n")
            scores.pop(loweredUsername, None) # remove from scores list
        else: # if username isnt there then make it blank in all txt
            for test in inputScore:
                outputScore[test].write("\n")

    for username in scores: # any missing username from ordered list
        plrScores = scores[username]
        print(plrScores["Username"] + " is missing.")

        for test in inputScore:
            if test not in plrScores:
                plrScores[test] = "N/A"
        
        plr = plrScores["Username"] + " Dummies: " + plrScores["Dummies"] + " Speed: " + plrScores["Speed"] + " Muskets: " + plrScores["Muskets"] + "\n" # add to missing ppl doc
        missingScores.write(plr)

def CloseOutputs():
    for key in outputScore:
        outputScore[key].close()
    missingScores.close()

if __name__ == "__main__":
    main()
