import requests
import json

groupID = "8536935"
roleID = "107675583" # AT

outputFile = "Outputs/Usernames.txt"

def main():
    writeToFile(getCadets())

def getCadets():
    usernames = []
    nextCursor = ""

    while True:
        url = "https://groups.roblox.com/v1/groups/" + groupID + "/roles/" + roleID + "/users?limit=100&sortOrder=Desc&cursor=" + nextCursor + "&"
        
        parsedData = json.loads(requests.get(url).text)
        for _, plrData in enumerate(parsedData["data"]):
            usernames.append(plrData["username"])

        if not parsedData["nextPageCursor"]:
            break
        else:
            nextCursor = parsedData["nextPageCursor"]
    
    print(usernames)
    return usernames

def writeToFile(usernames):
    file = open(outputFile, "w")

    for _, username in enumerate(usernames):
        file.write(username + "\n")
    file.close()

if __name__ == "__main__":
    main()
