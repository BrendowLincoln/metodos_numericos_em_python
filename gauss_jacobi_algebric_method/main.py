
from matrix import Matrix
from initial_value import InitialValue
from gaus_jacobi_algebric_method import gaussJacobiAlgebric


def main():

    print('\n\n*** MÉTODO ALGÉBRICO: GAUSS JACOBI (ALGÉBRICO) ***\n')

    # Obtendo os parâmetros de entrada
    initialValue = getParametersFromUser()

    # Executando o método para o calculo do método
    result = gaussJacobiAlgebric(initialValue)

    # Printando tabela
    buildTable(result, initialValue)

    # Printando o resultado e tabela
    result.printResult()

def getParametersFromUser():

    try:
        initialValue = InitialValue()
        initialValue.matrix = Matrix()

        initialValue.matrix.size = int(input("Informe o tamanho da matrix quadrada (nXn): "))
        print("")

        for i in range(initialValue.matrix.size):
            line = []
            
            for j in range(initialValue.matrix.size):
                value = float(input(f"a{i+1}{j+1}: "))
                line.append(value)
            
            initialValue.matrix.coefficient.append(line)
            indepedentValue = float(input(f"X{i+1}: "))
            initialValue.matrix.independentTerms.append(indepedentValue)
            print("")

        print("Escolha os valores inicias")
        for i in range(initialValue.matrix.size):
            initialValue.startValues.append(float(input(f"X{i+1}: ")))
            

        initialValue.error = float(input("Informe o erro: "))
        initialValue.times = int(input("Informe a quantidade de repetições: "))
        print("")

        return initialValue
    
        
    except:
        print("\nValor digitado inválido!\n")
        return

def buildTable(result, initialValue):
    # Montando o header baseado nas variaveis
    print("-------------------------------------------------------------------------")
    string_header = ""
    string_header += "| K \t"

    for i in range(initialValue.matrix.size):
        
        string_header += ("| " + "X" + str((i+1)) + " \t\t")

    string_header += "| Situação \t|"

    print(string_header)
    print("-------------------------------------------------------------------------")


    for item in result.lines:
        item.printRow()


if __name__ == "__main__":
    main()

