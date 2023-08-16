from secant_method import *

def main():
    '''
    Imagem da funcao escolhida
    '''
    def f(value):
        return pow(value, 2) - 16
    
    '''
    Variaveis
    '''
    next = True
    a = 0.0
    b  = 0.0
    error = 0.0
    times = 0

    print('\n\n*** MÉTODO DA SECANTE ***\n')

    '''
    Usando uma retentativa para erro na entrada da informação inicial!
    '''
    while next:

        try:
            a = float(input("Primeiro chute (Xk-1): "))
            b = float(input("Segundo chute (Xk): "))
            error = float(input("Erro desejado: "))
            times = int(input("Quantas reptições: "))
            next = False
                

            print("\n")
            
        except:
            print("\nValor digitado inválido! Insira novamente\n")

    print("| k \t| Xk-1 \t\t| Xk \t\t| f(Xk-1) \t| f(Xk) \t| Xk+1 \t\t| Situação \t|")
    
    '''
    Chamando o método da bissessao0
    '''
    result = secant(a, b, error, times, f)

    print("\nRESULTADOS\n")
    print("A raiz da função é: ",  "%.4f" % result["root"])
    print("O valor da imagem chegou no erro desejado: ", "%.4f" %  result["rootImage"])
    print("Parou na interação: ", result["iterection"])


if __name__ == "__main__":
    main()