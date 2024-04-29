
import requests
import json

groupID = "8536935"
roleID = "106749302" # AT

def main():
    writeToFile(getAllPlayers())

def getAllPlayers():
    playerData = []
    nextCursor = ""

    while True:
        rawData = requests.get("https://groups.roblox.com/v1/groups/" + groupID + "/roles/" + roleID + "/users?limit=100&sortOrder=Desc&cursor=" + nextCursor + "&").text
        parsedData = json.loads(rawData)
        print(parsedData["data"])
        playerData += parsedData["data"]

        if not parsedData["nextPageCursor"]:
            break
        else:
            nextCursor = parsedData["nextPageCursor"]
    
    return playerData

def writeToFile(players):
    file = open("output.txt", "w")
    for key, plrData in enumerate(players):
        file.write(plrData["username"] + "\n")
    file.close()

if __name__ == "__main__":
    main()
