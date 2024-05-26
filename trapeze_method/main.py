import math

from initial_value import InitialValues
from trapeze_method import trapezeMethod

def main():
    '''
    Função da integral
    '''
    def f(value):
        return 1/value

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


if __name__ == "__main__":
    main()