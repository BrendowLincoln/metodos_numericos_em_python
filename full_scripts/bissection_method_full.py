import math

def main():
    '''
    Funcao escolhida para gerar imagem de x
    '''
    def f(value):
        return math.sin(math.radians(value)) - pow(value, 2)
    

    print('\n\n*** MÉTODO DA BISSEÇÃO ***\n')

    '''
    Variaveis iniciais
    '''
    initialValues = InitialValues()

    '''
    Usando uma retentativa para erro na entrada da informação inicial!
    '''
    initialValues.next = True
    while initialValues.next:
        getParametersFromUer(initialValues, f)
    
    '''
    Chamando o método da bissessao
    '''
    result = bissection(initialValues, f)

    printTableResult(result)

def bissection(initialValues, f):

    BRUTE_FORCE_TIMES = initialValues.times

    x1 = initialValues.a
    x2 = initialValues.b
    avg = 0.0
    fX1 = 0.0
    fX2 = 0.0
    fAvg = 0.0
    lines = []

    for i in range(BRUTE_FORCE_TIMES):
        # Calculando a média
        avg = (x1+x2)/2

        # Calculando a imagem de a, b e a media
        fX1 = f(x1)
        fX2 = f(x2)
        fAvg = f(avg)

        # Verifca se chegou a um resultado aceitavel
        count = (i + 1)

        line = TableRow(count, x1, avg, x2, fX1, fAvg, fX2, "")
        
        if abs(fAvg) <= initialValues.error:

            line.statusMessage = "Finalizar"
            lines.append(line)

            result = NumericMethodResult(lines, avg, fAvg, count)

            return result
        else:                        

            line.statusMessage = "Continuar"
            lines.append(line)

            # Caso não esteja válido, ele repassa o valor  f
            if isValidValues(x1, avg, f):
                x2 = avg
            else:
                x1 = avg

def isValidValues(a, b, f):
    return f(a) * f(b) < 0

def getParametersFromUer(initialValues, f):
    initialValues.a = float(input("Primeiro chute (a): "))
    initialValues.b = float(input("Segundo chute (b): "))

    try:
        if isValidValues(initialValues.a, initialValues.b, f) == False:
            message = f"\nOs valores '{initialValues.a}' e '{initialValues.b}' não geram resultado!\nInsira novos valores.\n"
            print(message)
            return
            
        else:
            initialValues.error = float(input("Erro desejado: "))
            initialValues.times = int(input("Quantas reptições: "))
            initialValues.next = False

        print("\n")
        
    except:
        print("\nValor digitado inválido!\n")
        return

def printTableResult(result):

    print("-------------------------------------------------------------------------------------------------------------------------")
    print("| k \t| A \t\t| X \t\t| B \t\t| f(A) \t\t| f(X) \t\t| f(B) \t\t| Situação \t|")
    print("|-----------------------------------------------------------------------------------------------------------------------|")

    for line in result.lines:
        line.printRow()
    print("-------------------------------------------------------------------------------------------------------------------------")

    print("\n### RESULTADOS ###\n")
    print(f"A raiz da função é: {result.root: .4f}")
    print(f"O valor da imagem chegou no erro desejado: {result.rootImage: .4f}")
    print(f"Parou na interação: {result.finalIteraction}")
    print("-------------------------------------------------------------------------------------------------------------------------\n")

class InitialValues:
    def __init__(self, a = None, b = None, error = None, times = None, next = None):
        self.a = a
        self.b = b
        self.error = error
        self.times = times
        self.next = next

class TableRow:
    
    def __init__(self, count = None, x1 = None, avg = None, x2 = None, fX1 = None, fAvg = None, fX2 = None, statusMessage = None):
        self.count = count
        self.x1 = x1
        self.avg = avg
        self.x2 = x2
        self.fX1 = fX1
        self.fAvg = fAvg
        self.fX2 = fX2
        self.statusMessage = statusMessage

    def printRow(self):
        print(f"| {self.count} \t| {self.x1: .4f} \t| {self.avg: .4f} \t| {self.x2: .4f} \t| {self.fX1: .4f} \t| {self.fAvg: .4f} \t| {self.fX2: .4f} \t|  {self.statusMessage} \t|")

class NumericMethodResult:
    def __init__(self, lines = None, root = None, rootImage = None, finalIteraction = None):
            self.lines = lines
            self.root = root
            self.rootImage = rootImage
            self.finalIteraction = finalIteraction


if __name__ == "__main__":
    main()