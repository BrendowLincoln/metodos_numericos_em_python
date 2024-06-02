import copy

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

def gaussJacobiAlgebric(initialValues):

    # Definindo valor de critério de parada de forca bruta
    BRUTE_FORCE_TIMES = initialValues.times

    # Obtendo a matriz convergida
    converged_matrix = initialValues.matrix.getConvergedMatrix()

    if converged_matrix != None:

        # Inicializando um vetor de valores iniciais das incognitas
        unknownValuesIteration = initialValues.startValues

        # Inicializano a lista de linhas da tabela
        lines = []

        for i in range(BRUTE_FORCE_TIMES):
            line = TableRow()
            line.matrixSize = converged_matrix.size
            final_results = []

            # Colocando o index da linha atual
            line.count = (i+1)

            for j in range(initialValues.matrix.size):
                # Definindo o nome da variável que será adicionada no objeto resultado
                unknown_key = f'x{(j + 1)}'

                equation = Equation(converged_matrix.coefficient[j], converged_matrix.independentTerms[j])
                line.unknowns[unknown_key] = equation.resolve_current_variables(unknownValuesIteration, j)
                final_results.append(line.unknowns[unknown_key])
        
            # Verificando a condição de parada
            variable_result_values_list = list(line.unknowns.values())
            is_break_criteria_attempt = False

            for index, value in enumerate(variable_result_values_list):
                is_break_criteria_attempt = abs((value - unknownValuesIteration[index])) <= initialValues.error
                
                if is_break_criteria_attempt == False:
                    break

            if is_break_criteria_attempt:
                line.statusMessage = "Finalizar"
                lines.append(line)

                return NumericMethodResult(lines, final_results, initialValues.matrix.size)
            
            line.statusMessage = "Continuar"
            lines.append(copy.deepcopy(line))

            for index, value in enumerate(variable_result_values_list):
                unknownValuesIteration[index] = value

class InitialValue:
    def __init__(self, matrix = None, startValues = None, error = None, times = None):
        self.matrix = matrix
        self.startValues = [] if startValues == None else startValues
        self.error = error
        self.times = times

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
    
class TableRow:
    def __init__(self, count = None, unknowns = {}, statusMessage = None, matrixSize = None):
        self.count = count
        self.unknowns = unknowns
        self.statusMessage = statusMessage
        self.matrixSize = matrixSize
        

    def printRow(self):
        string_line = "| "
        string_line += (str(self.count) + " \t|")

        for i in range(self.matrixSize):
            key = f'x{(i + 1)}'

            string_line += (str(self.unknowns[key]) + "\t\t|")

        string_line += (" " + str(self.statusMessage) + " \t|")

        print(string_line)
        print("-------------------------------------------------------------------------")

class NumericMethodResult:
    def __init__(self, lines = None, finalResults = None, matrixSize = None):
            self.lines = lines
            self.finalResults = finalResults
            self.matrixSize = matrixSize

    def printResult(self):
        final_results = "Os valores das variáveis: ("
        
        for index, value in enumerate(self.finalResults):
            if (index + 1) != self.matrixSize:
                final_results += (str(value) + ", ") 
            else:
                final_results += (str(value) + ")")
        
        print("\nRESULTADOS\n")
        print(final_results, "\n")
        return

class Equation:
    def __init__(self, terms, solution):
        self.terms = terms
        self.solution = solution

    def resolve_current_variables(self, startValues, unknownIndex):
         # Retornando o termo que corresponde à posição da variável atual
        match_position_term = round(self.terms[unknownIndex], 4)

        # Extraindo os termos restantes da equação para uma nova lista
        remaining_terms = self.__remove_element_by_index(self.terms, unknownIndex)

        # Invertendo o sinal dos termos restantes para cálculo
        remaining_terms = list(map(lambda value: value * (-1), remaining_terms))

        # Extraindo os valores das variáveis ​​de iteração que correspondem à posição dos termos restantes
        remaining_terms_iteration_variable_values = self.__remove_element_by_index(startValues, unknownIndex)

        # Iniciando o cálculo adicionando a solução da equação ao valor inicial do resultado da variável atual
        variable_result = round(self.solution)

        # Calculando o produto para cada termo restante com um valor de variável de iteração correspondente e somando o produto ao resultado da variável de iteração atual
        for index, equation_value in enumerate(remaining_terms):
            variable_result += (round(equation_value, 4) * round(remaining_terms_iteration_variable_values[index], 4))

        # Para a etapa final do cálculo, divida o valor real pelo termo na posição correspondente
        variable_result = round((variable_result / match_position_term), 4)

        return variable_result
    
    def __remove_element_by_index(self, list, index):
        filtered_list = list[:index] + list[index+1:]
        return filtered_list
    

if __name__ == "__main__":
    main()