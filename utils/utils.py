def printText():
    print("Texto")

def convergeMatrix(matrix, matrixValue):
    #Criando uma copia de matrix
    matrixCopy = matrix

    if matrixValue != None:
        matrixValueCopy = matrixValue

    #Pegando o tamanho da w
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

            actualLineValue = matrixCopy[i][j]
            sumOtherValues = sum([x for x in matrixCopy[i] if x != actualLineValue])

            if actualLineValue > sumOtherValues:
                biggestLineValueIndex = j
                convergedMatrix["matrix"].insert(biggestLineValueIndex, matrixCopy[i])
                if matrixValue != None:
                    convergedMatrix["matrixValue"].insert(biggestLineValueIndex, matrixValueCopy[j])
                break

    # Retorna a matriz convergida 
    return convergedMatrix
