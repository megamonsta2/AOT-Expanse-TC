from GetCadets import getCadets

outputFiles = {
    "Usernames": open("Outputs/Usernames.txt", "w")
}

usernames = getCadets()

def main():

    # write usernames
    file = outputFiles["Usernames"]

    for _, username in enumerate(usernames):
        file.write(username + "\n")
    file.close()

if __name__ == "__main__":
    main()