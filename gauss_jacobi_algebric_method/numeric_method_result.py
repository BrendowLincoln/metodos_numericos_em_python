class NumericMethodResult:
    def __init__(self, lines = None, finalResults = None, matrixSize = None):
            self.lines = lines
            self.finalResults = finalResults
            self.matrixSize = matrixSize

    def printResult(self):
        final_results = "Os valores das variáveis: ("
        
        for index, value in enumerate(self.finalResults):
            if (index + 1) != self.matrixSize:
                final_results += (str(value) + ", ") 
            else:
                final_results += (str(value) + ")")
        
        print("\nRESULTADOS\n")
        print(final_results, "\n")
        return