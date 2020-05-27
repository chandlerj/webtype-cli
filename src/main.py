from UserInterface import UserInterface
import sys

print("basic newsracer")
print(f"pulling text from", sys.argv[1])

file = open(sys.argv[1])

test = UserInterface(file)
test.runTest()
