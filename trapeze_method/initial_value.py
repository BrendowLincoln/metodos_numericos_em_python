class InitialValues:
    def __init__(self, inferiorLimit = None, upperLimit = None, n = None):
        self.inferiorLimit = inferiorLimit
        self.upperLimit = upperLimit
        self.n = n

    def getH(self):
        return (self.upperLimit - self.inferiorLimit)/self.n

    def toString(self):
        return f"inferiorLimit: {self.inferiorLimit}, upperLimit: {self.upperLimit}, n: {self.n}, getH: {self.getH()}"