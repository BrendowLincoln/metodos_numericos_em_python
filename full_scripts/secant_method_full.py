import math

def main():
    '''
    Imagem da funcao escolhida
    '''
    def f(value):
        return math.sqrt(value) - math.cos(value)
    
    print('\n\n*** MÉTODO DA SECANTE ***\n')

    '''
    Variaveis
    '''
    initialValues = InitialValues()

    '''
    Usando uma retentativa para erro na entrada da informação inicial!
    '''
    initialValues.next = True
    while initialValues.next:
       getParametersFromUer(initialValues, f)

    '''
    Chamando o método da bissessao0
    '''
    result = secant(initialValues, f)
    printTableResult(result)

def secant(initialValue, f):

    BRUTE_FORCE_TIMES = initialValue.times

    x0 = initialValue.a
    x1 = initialValue.b
    x2 = 0.0
    fX0 = 0.0
    fX1 = 0.0
    lines = []

    for i in range(BRUTE_FORCE_TIMES):
        
        '''
        Calculando a imagem de a, b e a media
        '''
        fX0 = f(x0)
        fX1 = f(x1)

        '''
        CALCULANDO A RAIZ
        '''
        x2 = x1 - ((fX1 * (x1 - x0))/(fX1 - fX0))

        '''
        Verifca se chegou a um resultado aceitavel
        '''
        count = (i + 1)

        line = TableRow(count, x0, x1, fX0, fX1, x2, "")

        if abs(fX1) <= initialValue.error:
            line.statusMessage = "Finalizar"
            lines.append(line)

            result = NumericMethodResult(lines, x1, fX1, count)
            return result
        
        else:
            line.statusMessage = "Continuar"
            lines.append(line)
            
            '''
            FAZENDO A PASSAGEM DOS VALORES PARA A PROXIMA INTERACAO
            '''
            x0 = x1
            x1 = x2

def getParametersFromUer(initialValues, f):
    try:
        initialValues.a = float(input("Primeiro chute (Xk-1): "))
        initialValues.b = float(input("Segundo chute (Xk): "))
        initialValues.error = float(input("Erro desejado: "))
        initialValues.times = int(input("Quantas reptições: "))
        initialValues.next = False

        print("\n")
    except:
        print("\nValor digitado inválido!\n")

def printTableResult(result):
    print("---------------------------------------------------------------------------------------------------------")
    print("| k \t| Xk-1 \t\t| Xk \t\t| f(Xk-1) \t| f(Xk) \t| Xk+1 \t\t| Situação \t|")
    print("|-------------------------------------------------------------------------------------------------------|")

    for line in result.lines:
        line.printRow()
    print("---------------------------------------------------------------------------------------------------------")

    print("\n### RESULTADOS ###\n")
    print(f"A raiz da função é: {result.root: .4f}")
    print(f"O valor da imagem chegou no erro desejado: {result.rootImage: .4f}")
    print(f"Parou na interação: {result.finalIteraction}")
    print("---------------------------------------------------------------------------------------------------------\n")

class InitialValues:
    def __init__(self, a = None, b = None, error = None, times = None, next = None):
        self.a = a
        self.b = b
        self.error = error
        self.times = times
        self.next = next

class TableRow:
    def __init__(self, count = None, x0 = None, x1 = None, fX0 = None, fX1 = None, x2 = None, statusMessage = None):
        self.count = count
        self.x0 = x0
        self.x1 = x1
        self.fX0 = fX0
        self.fX1 = fX1
        self.x2 = x2
        self.statusMessage = statusMessage
        

    def printRow(self):
        print(f"| {self.count} \t| {self.x0: .4f} \t| {self.x1: .4f} \t| {self.fX0: .4f} \t| {self.fX1: .4f} \t| {self.x2: .4f} \t| {self.statusMessage} \t|")

class NumericMethodResult:
    def __init__(self, lines = None, root = None, rootImage = None, finalIteraction = None):
            self.lines = lines
            self.root = root
            self.rootImage = rootImage
            self.finalIteraction = finalIteraction

if __name__ == "__main__":
    main()