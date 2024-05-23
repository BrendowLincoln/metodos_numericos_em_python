import math

def main():
    '''
    Função da integral
    '''
    def f(value):
        return value/(1 + pow(value, 2))

    # Mostrando cabeçalho do programa
    print('\n\n*** MÉTODO DE INTEGRAÇÃO: RETÂNGULO ***\n')

    # Pegando os valores dos parâmetros com o usuário
    initialValues = getParametersFromUser(f)

    #Passando os valores informados pelo usuário para o método que irá calcular
    result = rectangleMethod(initialValues, f)

    # Mostrando as linhas contidas no objeto de result como uma tabela.
    print("-------------------------------------------------------------------------")
    print("| k \t| Xk \t\t| Avg \t\t| Xk+1 \t\t| f(X) \t\t|")
    print("|-----------------------------------------------------------------------|")

    for line in result.lines:
        line.printRow()
    print("-------------------------------------------------------------------------")

    # Mostrando o resultado
    result.printResult()

def getParametersFromUser(f):

    try:
        initialValues = InitialValues()
        
        initialValues.inferiorLimit = float(input("Limite inferior: "))
        initialValues.upperLimit = float(input("Limite superior: "))
        initialValues.n = int(input("Número de repartições (n): "))
        print("\n")

        return initialValues

    except:
        print("\nValor digitado inválido!\n")
        return

def rectangleMethod(initialValues, f):
    
    x1 = initialValues.inferiorLimit
    avg = 0.0
    lines = []

    for i in range(initialValues.n):
        # Calculando o Xk+1 e ponto médio
        x2 =  x1 + initialValues.getH()
        avg = (x1 + x2)/2

        # Calculando a função no limite do ponto médio
        fAvg = f(avg)

        # Criando as linhas para renderização da tabela
        line = TableRow(i, x1, avg, x2, fAvg)
        lines.append(line)

        # Passando o valor de Xk+1 para Xk para  próxima iteração
        x1 = x2

    # Retornando o resultado obtido a partir das linhas geradas
    result = NumericMethodResult(lines, initialValues.getH())

    return result

class InitialValues:
    def __init__(self, inferiorLimit = None, upperLimit = None, n = None):
        self.inferiorLimit = inferiorLimit
        self.upperLimit = upperLimit
        self.n = n

    def getH(self):
        return (self.upperLimit - self.inferiorLimit)/self.n

    def toString(self):
        return f"inferiorLimit: {self.inferiorLimit}, upperLimit: {self.upperLimit}, n: {self.n}, getH: {self.getH()}"
    

class TableRow:
    
    def __init__(self, count = None, x1 = None, avg = None, x2 = None, fAvg = None):
        self.count = count
        self.x1 = x1
        self.avg = avg
        self.x2 = x2
        self.fAvg = fAvg

    def printRow(self):
        print(f"| {self.count} \t| {self.x1: .4f} \t| {self.avg: .4f} \t| {self.x2: .4f} \t| {self.fAvg: .4f} \t|")

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


if __name__ == "__main__":
    main()
