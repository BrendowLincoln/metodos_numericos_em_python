def newton(a, error, derivativeDelta, times, f):

    '''
    TODO VERIFICAR COM O LUCIANO UMA POSSIVEL INTERACAO A MAIS QUE O CODIGO ESTA
    GERANDO. FIZ A VERIFICACAO EM UM SITE ONLINE E FEZ COM UMA INTERACAO A MENOS.
    '''

    BRUTE_FORCE_TIMES = times

    x0 = a
    x1 = 0.0
    fX0 = 0.0
    derivative = 0.0

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
        statusMessage = ""

        count = (i + 1)
        

        if abs(fX0) <= error:
            statusMessage = "Finalizar"
            print("| ", count ,"\t|", "%.4f" % x0 ,"\t| ", "%.4f" % fX0 ,"\t| ", "%.4f" % x1 ,"\t| ", statusMessage ,"\t|")

            return {"root": x0, "rootImage": fX0, "iterection": count}
        else:
            statusMessage = "Continuar"
            
            print("| ", count ,"\t|", "%.4f" % x0 ,"\t| ", "%.4f" % fX0 ,"\t| ", "%.4f" % x1 ,"\t| ", statusMessage ,"\t|")
            

            '''
            FAZENDO A PASSAGEM DOS VALORES PARA A PROXIMA INTERACAO
            '''
            x0 = x1


def isValidValues(a, b, f):
    return f(a) * f(b) < 0

def calcNumericDerivate(x, delta, f):
    return (f(x+delta) - f(x))/(delta)
