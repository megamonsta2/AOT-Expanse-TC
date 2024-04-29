inputFolder = "Inputs"
outputFolder = "Outputs"

orderedNames = open(inputFolder + "/orderedNames.txt", "r").readlines()
inputScore = open(inputFolder + "/input.txt", "r").readlines()

outputScore = open(outputFolder + "/output.txt", "w")
missingScores = open(outputFolder + "/missing.txt", "w")

divider = " - "
scores = {} # {USERNAME: score}

def main():
    FormatScoreInput()
    AssignScores()
    CloseOutputs()

def FormatScoreInput():
    data = inputScore

    for key, line in enumerate(data):
        line = line.strip()
        dividerIndex = line.find(divider)

        username = line[:dividerIndex]
        score = line[dividerIndex+len(divider):]

        if username.lower() not in scores:
            scores[username.lower()] = {"TT": score, "Username": username}
        else:
            if int(score) > int(scores[username.lower()]["TT"]):
                scores[username.lower()][test] = score

def AssignScores():
    for key, username in enumerate(orderedNames):
        loweredUsername = username.strip().lower()

        if loweredUsername in scores: # if username is in ordered list
            outputScore.write(scores[loweredUsername]["TT"] + "\n")
            
            scores.pop(loweredUsername, None) # remove from scores list
        else: # if username isnt there then make it blank in all txt
            outputScore.write("\n")

    for username in scores: # any missing username from ordered list
        plrScores = scores[username]
        print(plrScores["Username"] + " is missing.")
        
        plr = plrScores["Username"] + " TT: " + plrScores["TT"] + "\n" # add to missing ppl doc
        missingScores.write(plr)

def CloseOutputs():
    outputScore.close()
    missingScores.close()

if __name__ == "__main__":
    main()
