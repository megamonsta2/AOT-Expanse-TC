from GetCadets import GetCadets
from GetKnowledge import GetKnowledge
from GetPracticals import GetPracticals

outputFiles = {
    "Usernames": open("Outputs/Usernames.txt", "w")
}

def main():
    scores = GetCadets() # {LowercaseUsername: {Username: username}}
    missing = {}

    GetKnowledge(scores, missing)
    GetPracticals(scores, missing)
    # scores, missing = GetKnowledge(scores, missing)

    print(scores)
    print(missing)
    
    input()

# def writeUsernames():
#     file = outputFiles["Usernames"]

#     for _, username in enumerate(usernames):
#         file.write(username + "\n")
#     file.close()

if __name__ == "__main__":
    main()