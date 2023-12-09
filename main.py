import os

def executar_main(nome_pasta):
    try:
        if nome_pasta == "bissection_method":
            from bissection_method.main import main as main_pasta1
            from bissection_method.bissection_method import bissection, isValidValues
            main_pasta1()
        elif nome_pasta == "secant_method":
            from secant_method.main import main as main_pasta2
            main_pasta2()
        elif nome_pasta == "newton_method":
            from newton_method.main import main as main_pasta3
            main_pasta3()
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
    opcao = input("Digite o número correspondente à pasta: ")
    return opcao

if __name__ == "__main__":
    while True:
        opcao = exibir_menu()
        if opcao == "1":
            executar_main("bissection_method")
            break
        elif opcao == "2":
            executar_main("secant_method")
            break
        elif opcao == "3":
            executar_main("newton_method")
            break
        else:
            print("Opção inválida. Tente novamente.")
