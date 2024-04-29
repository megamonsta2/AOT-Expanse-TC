from GetCadets import GetCadets
from GetKnowledge import GetKnowledge
from GetPracticals import GetPracticals
from GetBonus import GetBonus

outputFolder = "Outputs"
outputFiles = {
    "Username": True,
    "Knowledge": True,
    "Musket": True,
    "Dummies": True,
    "Speed": True,
    "TT": True,
    "Bonus": True,
}

def main():
    InitialiseOutputFiles()

    scores = GetCadets() # {LowercaseUsername: {Username: username}}
    missing = {}

    GetKnowledge(scores, missing)
    GetPracticals(scores, missing)
    GetBonus(scores, missing)
    # scores, missing = GetKnowledge(scores, missing)

    print(scores)
    print(missing)
    
    input()

def InitialiseOutputFiles():
    for key in outputFiles:
        outputFiles[key] = open(outputFolder + "/" + key + ".txt", "w")

# def writeUsernames():
#     file = outputFiles["Usernames"]

#     for _, username in enumerate(usernames):
#         file.write(username + "\n")
#     file.close()

if __name__ == "__main__":
    main()