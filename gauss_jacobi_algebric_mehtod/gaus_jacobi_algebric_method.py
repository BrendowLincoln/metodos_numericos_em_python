import sys

def gaus_jacobi_algebric(matrix, matrixValue, error, times):

    # Definindo criterio de parada de força bruta
    BRUTE_FORCE_TIMES = times

    # Fazendo a convergência da matriz
    converged_matrix = convergeMatrix(matrix, matrixValue)

    if converged_matrix == None:
        return

    # Pegando o tamanho da matrix
    matrix_length = len(converged_matrix["matrix"])

    # Inicializando a matrix de incógnitas
    intial_values = []

    for i in range(matrix_length):
        intial_values.insert(i, 0)

    # Isolando incógnitas


    return converged_matrix

def convergeMatrix(matrix, matrixValue):
    try:
        #Criando uma copia de matrix
        matrixCopy = matrix

        if matrixValue != None:
            matrixValueCopy = matrixValue

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
        tipo, message, traceback = sys.exc_info();

        print(message)

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
