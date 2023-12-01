import utils

def gaus_jacobi_algebric(matrix, matrixValue, error, times):

    # Definindo criterio de parada de força bruta
    BRUTE_FORCE_TIMES = times

    # Pegando o tamanho da matrix
    matrix_length = len(matrix)

    # Inicializando a matrix de incógnitas
    intial_values = []

    for i in range(matrix_length):
        intial_values.insert(i, 0)

    # Fazendo a convergência da matriz
    converged_matrix = utils.convergeMatrix(matrix, matrixValue)

    # Isolando incógnitas

            
            
    




    return converged_matrix


def criar_equacao_e_isolar_incognita(array, valor_alvo, incognita_alvo):
    n = len(array)

    # Verifique se o índice da incógnita alvo está dentro dos limites
    incognita_index = incognita_alvo
    if incognita_index < 0 or incognita_index >= n:
        return None  # Índice fora dos limites

    # Calcule o valor da incógnita alvo
    incognitas = [1.0 if i == incognita_index else 0.0 for i in range(n)]
    incognita_alvo_valor = ((valor_alvo * -1) - sum(incognitas[i] * array[i] for i in range(n))) / incognitas[incognita_index]

    return incognita_alvo_valor
