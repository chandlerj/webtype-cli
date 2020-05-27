class Compare:
    def __init__(self, userInput, sample):
        self.userInput = userInput
        self.sample = sample

    def compareTo(self):
        if self.userInput == self.sample:
            return True
        else:
            return False