import sys
import os

projeto_dir = os.path.dirname(os.path.abspath(__file__))
projeto_dir = os.path.dirname(projeto_dir)

sys.path.append(projeto_dir)

from gaus_jacobi_algebric_method import gaus_jacobi_algebric

def main():
    # Variaveis 
    matrix = [
        [1, 8, -1],
        [6, -1, 1],
        [1, 1, 5],
    ]

    matrixValue = [16, 7, 18]

    error = 0.01

    times = 100

    result = gaus_jacobi_algebric(matrix, matrixValue, error, times)

    print(result)

if __name__ == "__main__":
    main()

