from newton_method import *

def main():
    '''
    Imagem da funcao escolhida
    '''
    def f(value):
        return pow(value, 3) - 2 * value - 1
    
    def create_function(expression):
        def func(x):
            return eval(expression)
        return func
    
    '''
    Variaveis
    '''
    next = True
    a = 0.0
    error = 0.0
    derivativeDelta = 0.0
    times = 0

    print('\n\n*** MÉTODO DE NEWTON ***\n')

    '''
    Usando uma retentativa para erro na entrada da informação inicial!
    '''
    while next:

        expression = input("Digite a expressão numérica (use 'x' para a variavel e pode usar funções da biblioteca 'math'): ")

        try:
            func = create_function(expression)
            a = float(input("Primeiro chute (Xk): "))
            error = float(input("Erro desejado: "))
            derivativeDelta = float(input("Delta da derivada: "))
            times = int(input("Quantas reptições: "))
            next = False
                

            print("\n")
            
        except:
            print("\nValor digitado inválido! Insira novamente\n")

    print("| k \t| Xk \t\t| f(Xk) \t| Xk+1 \t\t| Situação \t|")
    
    '''
    Chamando o método de newton
    '''
    result = newton(a, error, derivativeDelta, times, func)

    print("\nRESULTADOS\n")
    print("A raiz da função é: ",  "%.4f" % result["root"])
    print("O valor da imagem chegou no erro desejado: ", "%.4f" %  result["rootImage"])
    print("Parou na interação: ", result["iterection"])


if __name__ == "__main__":
    main()