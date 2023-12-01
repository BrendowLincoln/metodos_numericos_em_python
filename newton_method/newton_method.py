def newton(a, error, derivativeDelta, times, f):
    BRUTE_FORCE_TIMES = times

    x0 = a
    x1 = 0.0
    fX0 = 0.0
    derivative = 0.0
    lines = []

    for i in range(BRUTE_FORCE_TIMES):
        '''
        DERIVADA NUMERICA

        '''
        derivative = calcNumericDerivate(x0, derivativeDelta, f)
        
        '''
        Calculando a imagem de a
        '''
        fX0 = f(x0)

        '''
        CALCULANDO A RAIZ
        '''
        x1= x0 - (fX0/derivative)

        '''
        Verifca se chegou a um resultado aceitavel
        '''
        count = (i + 1)
        
        line = {
            "count": count,
            "x0": x0,
            "fX0": fX0,
            "x1": x1,
            "statusMessage": ""
        }

        if abs(fX0) <= error:
            line["statusMessage"] = "Finalizar"
            lines.append(line)

            return {"lines": lines, "root": x0, "rootImage": fX0, "finalIteraction": count}
        else:
            line["statusMessage"] = "Continuar"
            lines.append(line)            

            '''
            FAZENDO A PASSAGEM DOS VALORES PARA A PROXIMA INTERACAO
            '''
            x0 = x1


def isValidValues(a, b, f):
    return f(a) * f(b) < 0

def calcNumericDerivate(x, delta, f):
    return (f(x+delta) - f(x))/(delta)
