import sys
import os

projeto_dir = os.path.dirname(os.path.abspath(__file__))
projeto_dir = os.path.dirname(projeto_dir)

sys.path.append(projeto_dir)

from gauss_jacobi_matrix_method import gauss_jacobi_matrix

def main():

    print('\n\n*** MÉTODO DE GAUSS JACOBI (MATRICIAL) ***\n')

    # Variaveis 
    matrix = [
        [2, 1, 1],
        [-2, 5, 1],
        [-3, -1, 6]
    ]

    matrixValue = [20, 25, 30]

    initial_values = [0, 0, 0]

    error = 0.05

    times = 100

    results = gauss_jacobi_matrix(matrix, matrixValue, initial_values, error, times)

    if results != None:
        quantity_variable = len(matrix)
        
        string_header = ""

        string_header += "| k \t"

        for i in range(quantity_variable):
            
            string_header += ("| " + "x" + str(results["lines"][i]["count"]) + " \t\t")

        string_header += "| Situação \t|"

        print(string_header)

        for item in results["lines"]:
            string_line = "| "
            string_line += (str(item["count"]) + " \t|")

            for i in range(quantity_variable):
                key = f'x{(i + 1)}'

                string_line += (str(item[key]) + "\t\t|")

            string_line += (" " + str(item["statusMessage"]) + " \t|")

            print(string_line)
        
        print()


        final_results = "Os valores das variáveis: ("
        
        for index, value in enumerate(results["final_results"]):
            if (index + 1) != quantity_variable:
                final_results += (str(value) + ", ") 
            else:
                final_results += (str(value) + ")")
        
        print("\nRESULTADOS\n")
        print(final_results, "\n")

    print("O sistema não gerou resultados!")

if __name__ == "__main__":
    main()

