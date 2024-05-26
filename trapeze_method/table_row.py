class TableRow:
    
    def __init__(self, count = None, xk = None, fXk = None, c = None, productCFXk = None):
        self.count = count
        self.xk = xk
        self.fXk = fXk
        self.c = c
        self.productCFXk = productCFXk

    def printRow(self):
        print(f"| {self.count} \t| {self.xk: .4f} \t| {self.fXk: .4f} \t| {self.c: .4f} \t| {self.productCFXk: .4f} \t|")

