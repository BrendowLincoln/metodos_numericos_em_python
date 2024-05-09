import sys
import copy
from typing import List


# Auxiliary class to help structure of code
class Equation:
    def __init__(self, terms, solution):
        self.terms = terms
        self.solution = solution

def gauss_jacobi_matrix(matrix, matrixValue, initial_values, error, times):

    # Defining the brute force stopping criterion
    BRUTE_FORCE_TIMES = times

    # Performing the convergence of the matrix
    converged_matrix = convergeMatrix(matrix, matrixValue)

    if converged_matrix != None:
        # Getting the size of the matrix
        matrix_length = len(converged_matrix["matrix"])

        # Initializing the matrix of unknowns with 0
        iteration_variable_initial_values = initial_values

        # Isolating variables
        iteration_variable_results = {}

        # Inicializing de lines result
        lines = []
        line = {}

        for i in range(BRUTE_FORCE_TIMES):
            final_results = []

            # Setting index of line
            line.__setitem__("count", (i+1))

            for j in range(matrix_length):
                # Defining variable name that will be add in result object
                current_variable_key = f'x{(j + 1)}'

                equation = Equation(converged_matrix["matrix"][j], converged_matrix["matrixValue"][j])
                iteration_variable_results[current_variable_key] = resolve_current_variables(equation, iteration_variable_initial_values, j)

            for key, value in iteration_variable_results.items():
                    line.__setitem__(key, value)
                    final_results.append(value)
        
            # Verifing the break condition
            variable_result_values_list = list(iteration_variable_results.values())
            is_break_criteria_attempt = False

            for index, value in enumerate(variable_result_values_list):
                is_break_criteria_attempt = abs((value - iteration_variable_initial_values[index])) <= error
                
                if is_break_criteria_attempt == False:
                    break

            if is_break_criteria_attempt:
                line.__setitem__("statusMessage", "Finalizar")
                lines.append(line)
                result = {"lines": lines, "final_results": final_results}

                return result
            
            line.__setitem__("statusMessage", "Continuar")
            lines.append(copy.deepcopy(line))

            for index, value in enumerate(variable_result_values_list):
                iteration_variable_initial_values[index] = value

def resolve_current_variables(equation: Equation, iteration_variable_initial_values: List[int], variable_target_index: int):

    try:
        # Retrieving term that match to position of current variable
        match_position_term = round(equation.terms[variable_target_index], 4)

        # Extracting the remaining terms of the equation to a new list
        remaining_terms = remove_element_by_index(equation.terms, variable_target_index)

        # Inverting the sign of the remaining terms for calculation
        remaining_terms = list(map(lambda value: value * (-1), remaining_terms))

        # Extracting the iteration variable values that match to the remaining terms position
        remaining_terms_iteration_variable_values = remove_element_by_index(iteration_variable_initial_values, variable_target_index)

        # Starting the calculation by adding the solution of the equation to the initial value of the current variable result 
        variable_result = round(equation.solution)

        # Calculating the product for each remaining term with a matching iteration variable value and summing the product to the current iteration variable result
        for index, equation_value in enumerate(remaining_terms):
            variable_result += (round(equation_value, 4) * round(remaining_terms_iteration_variable_values[index], 4))

        # For the final step of calculation, divide the actual value by the term at the matching position
        variable_result = round((variable_result / match_position_term), 4)

        return variable_result

    except:
        _, message, __ = sys.exc_info()
        print("".join(["ERROR!: An error has ocurred when resolve current variables calculation: ", str(message), "\n"]))
        raise

def remove_element_by_index(list: List, index: int):

    filtered_list = list[:index] + list[index+1:]
    return filtered_list

def convergeMatrix(matrix, matrixValue):
    try:
        #Criando uma copia de matrix
        matrixCopy = copy.deepcopy(matrix)
        matrixValueCopy = copy.deepcopy(matrixValue)

        #Pegando o tamanho da matrix
        if len(matrix) != len(matrixValue):
            raise Exception("Tamanho da matriz de equações não corresponde ao tamanho da matriz de resultados das equações.")

        matrixLength = len(matrixCopy)

        #Convergendo a matrix
        if matrixValue != None:
            convergedMatrix = {
                "matrix": [],
                "matrixValue": []
            }
        else:
            convergedMatrix = {
                "matrix": []
            }

        biggestLineValueIndex = 0

        for i in range(matrixLength):
            for j in range(matrixLength):
                #Pega o valor da posicao dessa linha presente na diagonal principal
                actualLineValue = matrixCopy[i][j]

                #Faz a soma dos outros valores da linha atual, desconciderando o valor na diagonal principal
                sumOtherValues = sum([x for x in matrixCopy[i] if x != actualLineValue])

                if actualLineValue > sumOtherValues:
                    biggestLineValueIndex = j
                    convergedMatrix["matrix"].insert(biggestLineValueIndex, matrixCopy[i])
                    if matrixValue != None:
                        convergedMatrix["matrixValue"].insert(biggestLineValueIndex, matrixValueCopy[i])
                    break

        # Retorna a matriz convergida 
        return convergedMatrix
    except Exception as e:
        print("Ocorreu um erro!\n")
        _, message, __ = sys.exc_info()
        print(message)
        return