orderedNames = open("Inputs/orderedNames.txt", "r").readlines()
ranklocked = open("Inputs/ranklocked.txt", "r").readlines()
output = open("output.txt", "w")

goonsFound = []

def main():
    Format()
    GetGoons()
    output.close()

def Format():
    for i, line in enumerate(orderedNames):
        orderedNames[i] = line.strip()
        
    for i, line in enumerate(ranklocked):
        ranklocked[i] = line.strip()

def GetGoons():
    for i, line in enumerate(ranklocked):
        if line in orderedNames:
            output.write(line+"\n")

if __name__ == "__main__":
    main()
