inputFolder = "Inputs"
outputFolder = "Outputs"

inputNames = open(inputFolder + "/knowledgeNames.txt", "r").readlines()
inputScores = open(inputFolder + "/knowledgeScores.txt", "r").readlines()

def GetKnowledge(usernames, missing):
    for key, name in enumerate(inputNames):
        name = name.strip()
        
        scoreToAdd = int(inputScores[key].strip())

        if name.lower() in usernames: # player is an AT
            plrData = usernames[name.lower()]

            if ("Written" not in plrData) or (plrData["Written"] > scoreToAdd): # score doesnt exist OR existing score is greater than new score
                plrData["Written"] = scoreToAdd # assign new score
        
        else: # missing users
            if name.lower() not in missing: # new missing data
                missing[name.lower()] = {"Username": name, "Written": scoreToAdd}
            else: # has missing data
                missing[name.lower()]["Written"] = scoreToAdd
    
    # return usernames, missing
