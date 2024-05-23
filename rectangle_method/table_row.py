class TableRow:
    
    def __init__(self, count = None, x1 = None, avg = None, x2 = None, fAvg = None):
        self.count = count
        self.x1 = x1
        self.avg = avg
        self.x2 = x2
        self.fAvg = fAvg

    def printRow(self):
        print(f"| {self.count} \t| {self.x1: .4f} \t| {self.avg: .4f} \t| {self.x2: .4f} \t| {self.fAvg: .4f} \t|")
