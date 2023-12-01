def secant(a, b, error, times, f):

    BRUTE_FORCE_TIMES = times

    x0 = a
    x1 = b
    x2 = 0.0
    fX0 = 0.0
    fX1 = 0.0
    lines = []

    for i in range(BRUTE_FORCE_TIMES):
        
        '''
        Calculando a imagem de a, b e a media
        '''
        fX0 = f(x0)
        fX1 = f(x1)

        '''
        CALCULANDO A RAIZ
        '''
        x2 = x1 - fX1 * ((x1 - x0)/(fX1 - fX0))

        '''
        Verifca se chegou a um resultado aceitavel
        '''

        count = (i + 1)

        line = {
            "count": count,
            "x0": x0,
            "x1": x1,
            "fX0": fX0,
            "fX1": fX1,
            "fX1": fX1,
            "x2": x2,
            "statusMessage": ""
        }
        

        if abs(fX1) <= error:

            line["statusMessage"] = "Finalizar"
            lines.append(line)

            return {"lines": lines, "root": x1, "rootImage": fX1, "finalIterection": count}
        else:
            line["statusMessage"] = "Continuar"
            lines.append(line)
            
            '''
            FAZENDO A PASSAGEM DOS VALORES PARA A PROXIMA INTERACAO
            '''
            x0 = x1
            x1 = x2


def isValidValues(a, b, f):
    return f(a) * f(b) < 0
