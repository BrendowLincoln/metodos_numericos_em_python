from utils.numeric_method_type import NumericMethodType


def executar_main(nome_pasta):
    try:
        if nome_pasta == NumericMethodType.BISSECTION_METHOD:
            from bissection_method.main import main as main_pasta1
            main_pasta1()
        elif nome_pasta == NumericMethodType.SECANT_METHOD:
            from secant_method.main import main as main_pasta2
            main_pasta2()
        elif nome_pasta == NumericMethodType.NEWTON_METHOD:
            from newton_method.main import main as main_pasta3
            main_pasta3()
        elif nome_pasta == NumericMethodType.GAUSS_JACOBI_ALGEBRIC:
            from gauss_jacobi_algebric_mehtod.main import main as main_pasta4
            main_pasta4()
        elif nome_pasta == NumericMethodType.GAUSS_JACOBI_MATRIX:
            from newton_method.main import main as main_pasta5
            main_pasta5()
        else:
            print("Pasta não encontrada.")
    except ImportError as e:
        print(f"Erro ao importar: {e}")
    except Exception as ex:
        print(f"Ocorreu um erro: {ex}")

def exibir_menu():
    print("Selecione qual main executar:")
    print("1. Metodo Bisseccao")
    print("2. Metodo Secant")
    print("3. Metodo Newton")
    print("4. Gauss Jacobi (Algébrico)")
    print("5. Gauss Jacobi (Matricial)")
    opcao = input("Digite o número correspondente à pasta: ")
    return opcao

if __name__ == "__main__":
    while True:
        opcao = exibir_menu()
        if opcao == "1":
            executar_main(NumericMethodType.BISSECTION_METHOD)
            break
        elif opcao == "2":
            executar_main(NumericMethodType.SECANT_METHOD)
            break
        elif opcao == "3":
            executar_main(NumericMethodType.NEWTON_METHOD)
            break
        elif opcao == "4":
            executar_main(NumericMethodType.GAUSS_JACOBI_ALGEBRIC)
            break
        elif opcao == "5":
            executar_main(NumericMethodType.GAUSS_JACOBI_MATRIX)
            break
        else:
            print("Opção inválida. Tente novamente.")
