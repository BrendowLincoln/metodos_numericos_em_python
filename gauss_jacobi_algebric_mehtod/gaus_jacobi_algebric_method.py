import sys
import os
import math

projeto_dir = os.path.dirname(os.path.abspath(__file__))
projeto_dir = os.path.dirname(projeto_dir)

sys.path.append(projeto_dir)

from utils.utils import convergeMatrix

def gaus_jacobi_algebric(matrix, matrixValue, error, times):

    # Definindo criterio de parada de força bruta
    BRUTE_FORCE_TIMES = times

    # Fazendo a convergência da matriz
    converged_matrix = convergeMatrix(matrix, matrixValue)

    if converged_matrix == None:
        return

    # Pegando o tamanho da matrix
    matrix_length = len(converged_matrix["matrix"])

    # Inicializando a matrix de incógnitas com 0
    iteration_variables_values = [0] * matrix_length

    # Isolando incognitas
    equation = {
        "equationValues": [],
        "equalityEquationValue": None
    }

    for i in range(matrix_length):
        equation["equationValues"] = converged_matrix["matrix"][i]
        equation["equalityEquationValue"] = converged_matrix["matrixValue"][i]


        print(get_isolate_equations(equation, iteration_variables_values))

    return converged_matrix

def get_isolate_equations(equation, iterationVariableValues):
    """
    Essa função retorna um objeto com o resultado das incógnitas de X1 à Xn, para cada iteração.

    Parâmetros:
    equation ({equationValues ([int]), equalityEquationValue int}): Objeto com as propriedade:
        equationValues - array de números da equação.
        equalityEquationValue - valor da igualdade da equação.

    iterationVariableValues ([int]): Array de inteiros que são os valores das incóguinitas dessa iteração. 

    Retorna:
    int: A soma de a e b.
    """

    iterationEquationsResults = {}

    for i in range(len(equation["equationValues"])):
        x_count = i + 1
        x_key = f"x{x_count}"
        
        # Pegando o valor ligado à da incóguinita da iteração atual. 
        current_equation_value = round(equation["equationValues"][i], 4)

        # Filtrando os valores dos outros valores da equação que não sejam o mesmo que o da incóguinita atual para uma lista.
        others_equation_values = remove_value_from_list_by_index(equation["equationValues"], i)

        # Invertando o sinal da lista dos outros valores da equação
        others_equation_values = list(map(lambda x: x * (-1), others_equation_values))

        # Filtrando os valores das variaveis que não sejam a que corresponde a variavel que está sendo isolada para uma lista.
        current_iteration_variable_values = remove_value_from_list_by_index(iterationVariableValues, i)

        # Iniciando o calculo da equacao, adicionando o valor da igualdade original da equacao. 
        iterationEquationsResults[x_key] = round((equation["equalityEquationValue"]), 4)

        # Fazendo o calculo de todos os valores da equacao com o valor da incoguinita ferente.
        for index, equation_value in enumerate(others_equation_values):
            iterationEquationsResults[x_key] += (round(equation_value, 4) * round(current_iteration_variable_values[index], 4))

        # Por fim do calculo, divindo o valor atual da propriedade referente a incoguinita da iteracao, com o valor da equacao original relacionado a ela.
        iterationEquationsResults[x_key] = round((iterationEquationsResults[x_key] / current_equation_value), 4)

    return iterationEquationsResults


def remove_value_from_list_by_index(list, index):
    filtered_list = list[:index] + list[index+1:]
    return filtered_list