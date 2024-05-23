import math

def main():
    '''
    Imagem da funcao escolhida
    '''
    def f(value):
        return pow(value, 2) - (1/value) + 1
    
    print('\n\n*** MÉTODO DE NEWTON ***\n')

    '''
    Variaveis
    '''
    initialValues = InitialValues()

    '''
    Usando uma retentativa para erro na entrada da informação inicial!
    '''
    
    '''
    Chamando o método de newton
    '''
    result = newton(initialValues, f)
    printTableResult(result)

def newton(initialValues, f):
    BRUTE_FORCE_TIMES = initialValues.times

    x0 = initialValues.a
    x1 = 0.0
    fX0 = 0.0
    derivative = 0.0
    lines = []

    for i in range(BRUTE_FORCE_TIMES):
        '''
        DERIVADA NUMERICA

        '''
        derivative = calcNumericDerivate(x0, initialValues.derivativeDelta, f)
        
        '''
        Calculando a imagem de a
        '''
        fX0 = f(x0)

        '''
        CALCULANDO A RAIZ
        '''
        x1= x0 - (fX0/derivative)

        '''
        Verifca se chegou a um resultado aceitavel
        '''
        count = (i + 1)

        line = TableRow(count, x0, fX0, derivative, x1, "")

        if abs(fX0) <= initialValues.error:
            line.statusMessage = "Finalizar"
            lines.append(line)

            result = NumericMethodResult(lines, x0, fX0, count)
            return result
        else:
            line.statusMessage = "Continuar"
            lines.append(line)            

            '''
            FAZENDO A PASSAGEM DOS VALORES PARA A PROXIMA INTERACAO
            '''
            x0 = x1

def calcNumericDerivate(x, delta, f):
    return (f(x+delta) - f(x))/(delta)

def getParametersFromUer(initialValues, f):
    try:
        initialValues.a = float(input("Primeiro chute (Xk): "))
        initialValues.error = float(input("Erro desejado: "))
        initialValues.derivativeDelta = float(input("Delta da derivada: "))
        initialValues.times = int(input("Quantas reptições: "))
        initialValues.next = False

        print("\n")
    except:
        print("\nValor digitado inválido!\n")

def printTableResult(result):
    print("-----------------------------------------------------------------------------------------")
    print("| k \t| Xk \t\t| f(Xk) \t| f'(Xk) \t| Xk+1 \t\t| Situação \t|")
    print("|---------------------------------------------------------------------------------------|")

    for line in result.lines:
        line.printRow()
    print("-----------------------------------------------------------------------------------------")

    print("\n### RESULTADOS ###\n")
    print(f"A raiz da função é: {result.root: .4f}")
    print(f"O valor da imagem chegou no erro desejado: {result.rootImage: .4f}")
    print(f"Parou na interação: {result.finalIteraction}")
    print("-----------------------------------------------------------------------------------------\n")

class InitialValues:
    def __init__(self, a = None, error = None, derivativeDelta = None, times = None, next = None):
        self.a = a
        self.error = error
        self.derivativeDelta = derivativeDelta
        self.times = times
        self.next = next

class TableRow:
    def __init__(self, count = None, x0 = None, fX0 = None, fX0Derivate = None, x1 = None, statusMessage = None):
        self.count = count
        self.x0 = x0
        self.fX0 = fX0
        self.fX0Derivate = fX0Derivate
        self.x1 = x1
        self.statusMessage = statusMessage

    def printRow(self):
        print(f"| {self.count} \t| {self.x0: .4f} \t| {self.fX0: .4f} \t| {self.fX0Derivate: .4f} \t| {self.x1: .4f} \t| {self.statusMessage} \t|")

class NumericMethodResult:
    def __init__(self, lines = None, root = None, rootImage = None, finalIteraction = None):
            self.lines = lines
            self.root = root
            self.rootImage = rootImage
            self.finalIteraction = finalIteraction


if __name__ == "__main__":
    main()