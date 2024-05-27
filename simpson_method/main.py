import math

from initial_value import InitialValues
from simpson_method import simpsonMethod
from simpson_method import verifyIfNIsEven

def main():
    '''
    Função da integral
    '''
    def f(value):
        return pow(math.e, value)

    # Mostrando cabeçalho do programa
    print('\n\n*** MÉTODO DE INTEGRAÇÃO: SIMPSON ***\n')

    # Pegando os valores dos parâmetros com o usuário
    initialValues = getParametersFromUser(f)

    #Passando os valores informados pelo usuário para o método que irá calcular
    result = simpsonMethod(initialValues, f)

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

        while True:
            initialValues.n = int(input("Número de repartições (n) (Aviso - Precisar ser par): "))

            if verifyIfNIsEven(initialValues.n):
                break
            else:
                print("'n' não é par! Insíra novamente!\n")

        print("\n")

        return initialValues

    except:
        print("\nValor digitado inválido!\n")
        return


if __name__ == "__main__":
    main()