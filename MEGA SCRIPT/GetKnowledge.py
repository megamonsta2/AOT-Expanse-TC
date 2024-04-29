inputFolder = "Inputs"
outputFolder = "Outputs"

inputNames = open(inputFolder + "/knowledgeNames.txt", "r").readlines()
inputScores = open(inputFolder + "/knowledgeScores.txt", "r").readlines()

def GetKnowledge(usernames, missing):
    for key, name in enumerate(inputNames):

        name = name.strip()
        score = int(inputScores[key].strip())

        if name.lower() in usernames: # player is an AT
            plrData = usernames[name.lower()]

            if ("Written" not in plrData) or (plrData["Written"] > score): # score doesnt exist OR existing score is greater than new score
                plrData["Written"] = score # assign new score
        
        else: # not AT
            if name.lower() not in missing: # new missing data
                missing[name.lower()] = {"Username": name, "Written": score}
            else: # has missing data
                missing[name.lower()]["Written"] = score
    
    # return usernames, missing
