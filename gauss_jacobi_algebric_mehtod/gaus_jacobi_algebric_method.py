import sys
import os
import math
from typing import List

projeto_dir = os.path.dirname(os.path.abspath(__file__))
projeto_dir = os.path.dirname(projeto_dir)

sys.path.append(projeto_dir)

from utils.utils import convergeMatrix

# Auxiliary class to help structure of code
class Equation:
    def __init__(self, terms, solution):
        self.terms = terms
        self.solution = solution

def gaus_jacobi_algebric(matrix, matrixValue, error, times):

    # Definindo criterio de parada de força bruta
    BRUTE_FORCE_TIMES = times

    # Fazendo a convergência da matriz
    converged_matrix = convergeMatrix(matrix, matrixValue)

    if converged_matrix != None:
        # Pegando o tamanho da matrix
        matrix_length = len(converged_matrix["matrix"])

        # Inicializando a matrix de incógnitas com 0
        iteration_variable_values = [0] * matrix_length

        # Isolando incognitas
        iteration_variable_results = {}

        for i in range(matrix_length):
            # Defining variable name that will be add in result object
            current_variable_key = f'x{(i + 1)}'

            equation = Equation(converged_matrix["matrix"][i], converged_matrix["matrixValue"][i])
            iteration_variable_results[current_variable_key] = resolve_current_variables(equation, iteration_variable_values, i)

        print(iteration_variable_results)

        return converged_matrix
    

def resolve_current_variables(equation: Equation, iteration_variable_values: List[int], variable_target_index: int):

    # Retrieving term that match to position of current variable
    match_position_term = round(equation.terms[variable_target_index], 4)

    # Extracting the remaining terms of the equation to a new list
    remaining_terms = remove_element_by_index(equation.terms, variable_target_index)

    # Inverting the sign of the remaining terms for calculation
    remaining_terms = list(map(lambda value: value * (-1), remaining_terms))

    # Extracting the iteration variable values that match to the remaining terms position
    remaining_terms_iteration_variable_values = remove_element_by_index(iteration_variable_values, variable_target_index)

    # Starting the calculation by adding the solution of the equation to the initial value of the current variable result 
    variable_result = round(equation.solution)
    
    # Calculating the product for each remaining term with a matching iteration variable value and summing the product to the current iteration variable result
    for index, equation_value in enumerate(remaining_terms):
        variable_result += (round(equation_value, 4) * round(remaining_terms_iteration_variable_values[index], 4))
    
    # For the final step of calculation, divide the actual value by the term at the matching position
    variable_result = round((variable_result / match_position_term), 4)

    return variable_result


def remove_element_by_index(list: List, index: int):

    filtered_list = list[:index] + list[index+1:]
    return filtered_list