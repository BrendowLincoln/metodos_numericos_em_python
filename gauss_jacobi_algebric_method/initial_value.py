class InitialValue:
    def __init__(self, matrix = None, startValues = None, error = None, times = None):
        self.matrix = matrix
        self.startValues = [] if startValues == None else startValues
        self.error = error
        self.times = times