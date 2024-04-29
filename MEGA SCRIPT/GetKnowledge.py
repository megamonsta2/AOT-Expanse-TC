inputFolder = "Inputs"
outputFolder = "Outputs"

inputNames = open(inputFolder + "/knowledgeNames.txt", "r").readlines()
inputScores = open(inputFolder + "/knowledgeScores.txt", "r").readlines()

def GetKnowledge(usernames, missing):
    for key, name in enumerate(inputNames):

        name = name.strip()
        score = int(inputScores[key].strip())

        if name.lower() in usernames: # player is an AT
            addScore(usernames, name.lower(), score)
        
        else: # not AT
            if name.lower() not in missing: # new missing data
                missing[name.lower()] = {"Username": name, "Written": score}
            else: # has missing data
                addScore(missing, name.lower(), score)

def addScore(tbl, name, score):
    plrData = tbl[name]
    if ("Written" not in plrData) or (plrData["Written"] > score): # score doesnt exist OR existing score is greater than new score
        plrData["Written"] = score # assign new score