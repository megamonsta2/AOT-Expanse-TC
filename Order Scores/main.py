inputScores = open("input.txt", "r").readlines()
outputScores = open("output.txt", "w")

scoreDict = {}
divider = " - "
divider2 = " ("

def main():
    GetScores()
    WriteToFile()

def GetScores():
    for i, line in enumerate(inputScores):
        line = line.strip()
        if line == "": continue

        startOfNum = line.find(divider)+len(divider)
        endOfNum = line.find(divider2)
        
        marks = int(line[startOfNum:endOfNum])
        if marks not in scoreDict:
            scoreDict[marks] = []
        
        scoreDict[marks].append(line)

def WriteToFile():
    for i in range(100, -1, -1):
        if not (i in scoreDict): continue

        for x, line in enumerate(scoreDict[i]):
            outputScores.write(line + "\n")

    outputScores.close()

if __name__ == "__main__":
    main()
