import math

from initial_value import InitialValues
from table_row import TableRow
from numeric_method_result import NumericMethodResult

def simpsonMethod(initialValues: InitialValues, f):
    
    xK = initialValues.inferiorLimit
    lines = []
    c = 0
    fXk = 0.0
    productCFXk = 0.0

    for i in range((initialValues.n + 1)):
        # Definindo o valor de Ck
        if i == 0 or i == initialValues.n:
            c = 1
        elif verifyIfNIsEven(i):
            c = 2
        else:
            c = 4

        # Calculando a função no limite do ponto médio
        fXk = f(xK)

        # Calculando o produto de C * f(XK)
        productCFXk = c * fXk

        # Criando as linhas para renderização da tabela
        line = TableRow(i, xK, fXk, c, productCFXk)
        lines.append(line)

        # Passando o valor para Xk para próxima iteração
        xK = xK + initialValues.getH()

    # Retornando o resultado obtido a partir das linhas geradas
    result = NumericMethodResult(lines, initialValues.getH())

    return result

def verifyIfNIsEven(value):
    return value % 2 == 0