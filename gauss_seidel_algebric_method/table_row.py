class TableRow:
    def __init__(self, count = None, unknowns = {}, statusMessage = None, matrixSize = None):
        self.count = count
        self.unknowns = unknowns
        self.statusMessage = statusMessage
        self.matrixSize = matrixSize
        

    def printRow(self):
        string_line = "| "
        string_line += (str(self.count) + " \t|")

        for i in range(self.matrixSize):
            key = f'x{(i + 1)}'

            string_line += (str(self.unknowns[key]) + "\t\t\t|")

        string_line += (" " + str(self.statusMessage) + " \t|")

        print(string_line)
        print("-------------------------------------------------------------------------")