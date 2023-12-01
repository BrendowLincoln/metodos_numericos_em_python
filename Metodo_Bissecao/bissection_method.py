def bissection(a, b, error, times, f):

    BRUTE_FORCE_TIMES = times

    x1 = a
    x2 = b
    avg = 0.0
    fX1 = 0.0
    fX2 = 0.0
    fAvg = 0.0
    lines = []

    for i in range(BRUTE_FORCE_TIMES):
        # Calculando a média
        avg = (x1+x2)/2

        # Calculando a imagem de a, b e a media
        fX1 = f(x1)
        fX2 = f(x2)
        fAvg = f(avg)

        
        # Verifca se chegou a um resultado aceitavel
        count = (i + 1)

        line = {
            "count": count,
            "x1": x1,
            "avg": avg,
            "x2": x2,
            "fX1": fX1,
            "fAvg": fAvg,
            "fX2": fX2,
            "statusMessage": ""
        }
        
        if abs(fAvg) <= error:

            line["statusMessage"] = "Finalizar"
            lines.append(line)
            
            return {"lines": lines, "root": avg, "rootImage": fAvg, "finalIteraction": count}
        else:                        

            line["statusMessage"] = "Continuar"
            lines.append(line)

            # Caso não esteja válido, ele repassa o valor  f

            if isValidValues(x1, avg, f):
                x2 = avg
            else:
                x1 = avg

        
    


def isValidValues(a, b, f):
    return f(a) * f(b) < 0
