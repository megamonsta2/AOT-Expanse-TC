import requests
import json

groupID = "8536935"
roleID = "107675583" # AT

def GetCadets():
    usernames = {}
    nextCursor = ""

    while True:
        url = "https://groups.roblox.com/v1/groups/" + groupID + "/roles/" + roleID + "/users?limit=100&sortOrder=Desc&cursor=" + nextCursor + "&"
        
        parsedData = json.loads(requests.get(url).text)
        for _, plrData in enumerate(parsedData["data"]):
            username = plrData["username"]
            usernames[username.lower()] = {"Username": username}

        if not parsedData["nextPageCursor"]:
            break
        else:
            nextCursor = parsedData["nextPageCursor"]
    
    return usernames