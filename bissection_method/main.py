import sys
import os
import math

from bissection_method.bissection_method import bissection, isValidValues
import math

def main():
    '''
    Imagem da funcao escolhida
    '''
    def f(value):
        return pow((value/2), 2) - math.sin(math.radians(value))
    
    '''
    Variaveis
    '''
    next = True
    a = 0.0
    b  = 0.0
    error = 0.0
    times = 0

    print('\n\n*** MÉTODO DA BISSEÇÃO ***\n')

    '''
    Usando uma retentativa para erro na entrada da informação inicial!
    '''
    while next:

        try:
            a = float(input("Primeiro chute (a): "))
            b = float(input("Segundo chute (b): "))


            '''
            Verificar se os valores de A e B são válido para gerar um resultado
            '''
            if isValidValues(a, b, f) == False:
                message = "Os valores ", a,  " ", b, " não geram resultado!\n Insira novos valores.\n"
                print(message)
                
            else:
                error = float(input("Erro desejado: "))
                times = int(input("Quantas reptições: "))
                next = False

            print("\n")
            
        except:
            print("\nValor digitado inválido!\n")
            return

    print("| k \t| A \t\t| X \t\t| B \t\t| f(A) \t\t| f(X) \t\t| f(B) \t\t| Situação \t|")
    
    '''
    Chamando o método da bissessao0
    '''
    result = bissection(a, b, error, times, f)

    for line in result["lines"]:

        print("| ", line["count"] ,"\t|", "%.4f" % line["x1"] ,"\t| ", "%.4f" % line["avg"],"\t| ", "%.4f" % line["x2"] ,"\t| ", "%.4f" % line["fX1"] ,"\t| ", "%.4f" % line["fAvg"] ,"\t| ", "%.4f" % line["fX2"] ,"\t| ", line["statusMessage"] ,"\t|")

    print("\nRESULTADOS\n")
    print("A raiz da função é: ",  "%.4f" % result["root"])
    print("O valor da imagem chegou no erro desejado: ", "%.4f" %  result["rootImage"])
    print("Parou na interação: ", result["finalIteraction"])

if __name__ == "__main__":
    main()