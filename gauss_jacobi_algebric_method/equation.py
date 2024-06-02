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