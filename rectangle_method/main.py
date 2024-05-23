import math
from initial_value import InitialValues
from rectangle_method import rectangleMethod

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


if __name__ == "__main__":
    main()