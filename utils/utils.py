import copy
import sys


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
        
        _, message, __ = sys.exc_info()
        print(message)
        return

