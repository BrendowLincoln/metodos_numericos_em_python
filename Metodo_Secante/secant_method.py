def secant(a, b, error, times, f):

    BRUTE_FORCE_TIMES = times

    x0 = a
    x1 = b
    x2 = 0.0
    fX0 = 0.0
    fX1 = 0.0

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
        statusMessage = ""

        count = (i + 1)
        

        if fX1 <= error:
            statusMessage = "Finalizar"
            print("| ", count ,"\t|", "%.4f" % x0 ,"\t| ", "%.4f" % x1,"\t| ", "%.4f" % fX0 ,"\t| ", "%.4f" % fX1 ,"\t| ", "%.4f" % x2 ,"\t| ", statusMessage ,"\t|")

            return {"root": x1, "rootImage": fX1, "iterection": count}
        else:
            statusMessage = "Continuar"
            
            print("| ", count ,"\t|", "%.4f" % x0 ,"\t| ", "%.4f" % x1,"\t| ", "%.4f" % fX0 ,"\t| ", "%.4f" % fX1 ,"\t| ", "%.4f" % x2 ,"\t| ", statusMessage ,"\t|")
            

            '''
            FAZENDO A PASSAGEM DOS VALORES PARA A PROXIMA INTERACAO
            '''
            x0 = x1
            x1 = x2


def isValidValues(a, b, f):
    return f(a) * f(b) < 0
