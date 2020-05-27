from Compare import Compare
import time

class UserInterface:
    def __init__(self, file):
        self.file = file
        self.line = 0
        self.timeSpent = 0
    def runTest(self):
        for i in self.file:
            startTime = time.time()
            self.line += 1

            currentLine = i.rstrip()
            print(f"type: \"{currentLine}\"", end="")
            userInput = str(input("\n>"))
            comparision = Compare(userInput, currentLine)
            while comparision.compareTo():
                if comparision.compareTo():
                    print("yeah")
                    break
                else:
                    print("wrong")
                    continue
            self.timeSpent += time.time() - startTime
        print(f"average time spent per line: {float(self.timeSpent / self.line).__round__(2)} seconds")
