from functools import reduce

class NumericMethodResult:
    def __init__(self, lines = None, h = None):
            self.lines = lines
            self.sumImage = self.getSumAvgImage()
            self.result = h * self.sumImage
            


    def getSumAvgImage(self):
        avgImageList = list(map(lambda x: x.fAvg, self.lines))
        return float(reduce(lambda x, y: x + y, avgImageList))

    def printResult(self):
        print("\n### RESULTADOS ###\n")
        print(f"A aproximação do resultado: {self.result: .4f}")
        print(f"O somatório de f(avg): {self.sumImage: .4f}")
        print("-------------------------------------------------------------------------")
