import math

def main():
    '''
    Função da integral
    '''
    def f(value):
        return value * math.log(value)

    # Mostrando cabeçalho do programa
    print('\n\n*** MÉTODO DE INTEGRAÇÃO: TRAPÉZIO ***\n')

    # Pegando os valores dos parâmetros com o usuário
    initialValues = getParametersFromUser(f)

    #Passando os valores informados pelo usuário para o método que irá calcular
    result = trapezeMethod(initialValues, f)

    # Mostrando as linhas contidas no objeto de result como uma tabela.
    print("-------------------------------------------------------------------------")
    print("| k \t| Xk \t\t| f(Xk) \t| Ck \t\t| Ck * f(Xk) \t|")
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

def trapezeMethod(initialValues, f):
    
    xK = initialValues.inferiorLimit
    lines = []
    c = 0
    fXk = 0.0
    productCFXk = 0.0

    for i in range((initialValues.n + 1)):
        # Definindo o valor de Ck
        if (i == 0 or i == initialValues.n):
            c = 1
        else:
            c = 2

        # Calculando a função no limite do ponto médio
        fXk = f(xK)

        # Calculando o produto de C * f(XK)
        productCFXk = c * fXk

        # Criando as linhas para renderização da tabela
        line = TableRow(i, xK, fXk, c, productCFXk)
        lines.append(line)

        # Passando o valor de Xk+1 para Xk para  próxima iteração
        xK = xK + initialValues.getH()

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
    
    def __init__(self, count = None, xk = None, fXk = None, c = None, productCFXk = None):
        self.count = count
        self.xk = xk
        self.fXk = fXk
        self.c = c
        self.productCFXk = productCFXk

    def printRow(self):
        print(f"| {self.count} \t| {self.xk: .4f} \t| {self.fXk: .4f} \t| {self.c: .4f} \t| {self.productCFXk: .4f} \t|")

from functools import reduce

class NumericMethodResult:
    def __init__(self, lines = None, h = None):
            self.lines = lines
            self.sumImage = self.getSumAvgImage()
            self.result = (h/2) * self.sumImage
            


    def getSumAvgImage(self):
        avgImageList = list(map(lambda x: x.productCFXk, self.lines))
        return float(reduce(lambda x, y: x + y, avgImageList))

    def printResult(self):
        print("\n### RESULTADOS ###\n")
        print(f"A aproximação do resultado: {self.result: .4f}")
        print(f"O somatório do produto de C * f(Xk): {self.sumImage: .4f}")
        print("-------------------------------------------------------------------------")


if __name__ == "__main__":
    main()