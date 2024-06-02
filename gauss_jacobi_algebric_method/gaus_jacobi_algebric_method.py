import sys
import copy
from typing import List

from equation import Equation
from matrix import Matrix
from initial_value import InitialValue
from table_row import TableRow
from numeric_method_result import NumericMethodResult

def gaussJacobiAlgebric(initialValues: InitialValue):

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