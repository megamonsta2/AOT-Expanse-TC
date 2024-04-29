inputFile = open("Inputs/bonus.txt", "r").readlines() # {string: {USERNAME - SCORE}}
divider = " - "

def GetBonus(usernames, missing):
    for _, line in enumerate(inputFile):
        line = line.strip()
        dividerIndex = line.find(divider)

        name = line[:dividerIndex]
        score = int(line[dividerIndex+len(divider):])

        if name.lower() in usernames: # player is an AT
            plrData = usernames[name.lower()]

            if "Bonus" not in plrData: # score doesnt exist
                plrData["Bonus"] = score # assign new score
            else: # score exists
                plrData["Bonus"] += score # add

        else: # not AT
            if name.lower() not in missing: # new missing data
                missing[name.lower()] = {"Username": name, "Bonus": score}
            else: # has missing data
                missing[name.lower()]["Bonus"] = score