inputFolder = "Inputs"

inputScore = {
    "Dummies": {
        "Override": "Lower"
    },
    "Musket": {
        "Override": "Lower"
    },
    "Speed": {
        "Override": "Lower"
    },
    "TT": {
        "Override": "Higher"
    },
} # {string: {USERNAME - SCORE}}

divider = " - "

def GetPracticals(usernames, missing):
    InitialiseInputs()

    for test in inputScore:
        override = inputScore[test]["Override"]
        scoreData = inputScore[test]["File"]

        for _, line in enumerate(scoreData):
            line = line.strip()
            dividerIndex = line.find(divider)

            name = line[:dividerIndex]
            score = int(line[dividerIndex+len(divider):])

            if name.lower() in usernames: # player is an AT
                addScore(usernames, name.lower(), test, score, override)

            else: # not AT
                if name.lower() not in missing: # new missing data
                    missing[name.lower()] = {"Username": name, test: score}
                else: # has missing data
                    addScore(missing, name.lower(), test, score, override)

def addScore(tbl, name, test, score, override):
    plrData = tbl[name]

    if (
        test not in plrData or # score doesnt exist
        (override == "Lower" and plrData[test] > score) or # existing score is greater than new score
        (override == "Higher" and plrData[test] < score) # existing score is less than new score
        ): # score doesnt exist
            plrData[test] = score # assign new score

def InitialiseInputs():
    for test in inputScore:
        inputScore[test]["File"] = open(inputFolder + "/practical" + test + ".txt", "r").readlines()