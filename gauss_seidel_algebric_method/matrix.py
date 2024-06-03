class Matrix:
    def __init__(self, coefficient = None, independentTerms = None, size = None):
        if coefficient != None and independentTerms != None and size != None:
            self.coefficient = coefficient
            self.independentTerms = independentTerms
            self.size = size
        else:
            self.coefficient = coefficient if coefficient != None else []
            self.independentTerms = independentTerms if independentTerms != None else []
            self.size = len(self.independentTerms) if len(self.independentTerms) == len(self.coefficient) else 0

    def __str__(self):
        for i in range(self.size):
            print(f"{self.coefficient[i].__str__()} = {self.independentTerms[i]}")
        
        return ""

    def getConvergedMatrix(self):
        # Definindo a matrix que será o resultado
        convergedMatrix = Matrix()

        for i in range(self.size):
            for j in range(self.size):
                #Pega o valor da posicao dessa linha presente na diagonal principal
                actualLineValue = self.coefficient[i][j]

                #Faz a soma dos outros valores da linha atual, desconciderando o valor na diagonal principal
                sumOtherValues = sum([x for x in self.coefficient[i] if x != actualLineValue])

                if actualLineValue > sumOtherValues:
                    biggestLineValueIndex = j
                    convergedMatrix.coefficient.insert(biggestLineValueIndex, self.coefficient[i])
                    if self.independentTerms != []:
                        convergedMatrix.independentTerms.insert(biggestLineValueIndex, self.independentTerms[i])
                    break

        convergedMatrix.size = len(convergedMatrix.independentTerms)

        return convergedMatrix