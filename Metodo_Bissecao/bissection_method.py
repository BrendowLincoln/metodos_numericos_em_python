def bissection(a, b, error, times, f):

    BRUTE_FORCE_TIMES = times

    x1 = a
    x2 = b
    avg = 0.0
    fX1 = 0.0
    fX2 = 0.0
    fAvg = 0.0
    

    for i in range(BRUTE_FORCE_TIMES):

        '''
        CALCULANDO A MEDIA
        '''
        avg = (x1+x2)/2

        '''
        Calculando a imagem de a, b e a media
        '''
        fX1 = f(x1)
        fX2 = f(x2)
        fAvg = f(avg)


        '''
        Verifca se chegou a um resultado aceitavel
        '''
        statusMessage = ""

        count = (i + 1)
        

        if fAvg >= (error * -1) and fAvg <= error:
            statusMessage = "Finalizar"
            print("| ", count ,"\t|", "%.4f" % x1 ,"\t| ", "%.4f" % avg,"\t| ", "%.4f" % x2 ,"\t| ", "%.4f" % fX1 ,"\t| ", "%.4f" % fAvg ,"\t| ", "%.4f" % fX2 ,"\t| ", statusMessage ,"\t|")

            return {"root": avg, "rootImage": fAvg, "iterection": count}
        else:
            statusMessage = "Continuar"
            
            print("| ", count ,"\t|", "%.4f" % x1 ,"\t| ", "%.4f" % avg,"\t| ", "%.4f" % x2 ,"\t| ", "%.4f" % fX1 ,"\t| ", "%.4f" % fAvg ,"\t| ", "%.4f" % fX2 ,"\t| ", statusMessage ,"\t|")
            
            if isValidValues(x1, avg, f):
                x2 = avg
            else:
                x1 = avg

            
    


def isValidValues(a, b, f):
    return f(a) * f(b) < 0
