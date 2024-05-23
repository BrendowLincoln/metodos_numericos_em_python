from initial_value import InitialValues
from table_row import TableRow
from numeric_method_result import NumericMethodResult

def rectangleMethod(initialValues: InitialValues, f):
    
    x1 = initialValues.inferiorLimit
    avg = 0.0
    lines = []

    for i in range(initialValues.n):
        # Calculando o Xk+1 e ponto médio
        x2 =  x1 + initialValues.getH()
        avg = (x1 + x2)/2

        # Calculando a função no limite do ponto médio
        fAvg = f(avg)

        # Criando as linhas para renderização da tabela
        line = TableRow(i, x1, avg, x2, fAvg)
        lines.append(line)

        # Passando o valor de Xk+1 para Xk para  próxima iteração
        x1 = x2

    # Retornando o resultado obtido a partir das linhas geradas
    result = NumericMethodResult(lines, initialValues.getH())

    return result