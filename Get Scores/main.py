from GetCadets import GetCadets
from GetKnowledge import GetKnowledge
from GetPracticals import GetPracticals
from GetBonus import GetBonus

outputFolder = "Outputs"
outputFiles = {
    "Username": True,
    "Knowledge": True,
    "Dummies": True,
    "Speed": True,
    "Musket": True,
    "TT": True,
    "Bonus": True,
}
missingFiles = open(outputFolder + "/Missing.txt", "w")

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

    WriteToFiles(scores)
    WriteToMissing(missing)
    CloseFiles()
    
    input()

def InitialiseOutputFiles():
    for key in outputFiles:
        outputFiles[key] = open(outputFolder + "/" + key + ".txt", "w")

def WriteToFiles(scores):
    for name in scores:
        plrData = scores[name]

        for test in outputFiles:
            file = outputFiles[test]

            if test in plrData:
                file.write(str(plrData[test]) + "\n")
            else:
                file.write("\n")

writeMissingOrder = ["Username",  "Knowledge", "Dummies", "Speed", "Musket", "TT", "Bonus"]
def WriteToMissing(missing):
    file = missingFiles

    for name in missing:
        plrData = missing[name]

        toWrite = ""
        for _, test in enumerate(writeMissingOrder):
            toWrite += test + ": "
            if plrData[test]:
                toWrite += str(plrData[test])
            else:
                toWrite += "N/A"
            toWrite += test + " | "
        file.write(toWrite)

def CloseFiles():
    for file in outputFiles:
        outputFiles[file].close()
    missingFiles.close()


# def writeUsernames():
#     file = outputFiles["Usernames"]

#     for _, username in enumerate(usernames):
#         file.write(username + "\n")
#     file.close()

if __name__ == "__main__":
    main()
