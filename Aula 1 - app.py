import os

def exibir_nome_programa():
    print ("""
╭━━━┳━━━┳━━╮╭━━━┳━━━╮╭━━━┳━╮╭━┳━━━┳━━━┳━━━┳━━━┳━━━╮
┃╭━╮┃╭━╮┃╭╮┃┃╭━╮┃╭━╮┃┃╭━━┻╮╰╯╭┫╭━╮┃╭━╮┃╭━━┫╭━╮┃╭━╮┃
┃╰━━┫┃╱┃┃╰╯╰┫┃╱┃┃╰━╯┃┃╰━━╮╰╮╭╯┃╰━╯┃╰━╯┃╰━━┫╰━━┫╰━━╮
╰━━╮┃╰━╯┃╭━╮┃┃╱┃┃╭╮╭╯┃╭━━╯╭╯╰╮┃╭━━┫╭╮╭┫╭━━┻━━╮┣━━╮┃
┃╰━╯┃╭━╮┃╰━╯┃╰━╯┃┃┃╰╮┃╰━━┳╯╭╮╰┫┃╱╱┃┃┃╰┫╰━━┫╰━╯┃╰━╯┃
╰━━━┻╯╱╰┻━━━┻━━━┻╯╰━╯╰━━━┻━╯╰━┻╯╱╱╰╯╰━┻━━━┻━━━┻━━━╯\n""")

def exibir_opções ():
    print("1. Cadastrar restaurante")
    print("2. Listar restaurante")
    print("3. Ativar restaurante")
    print("4. Sair\n")

def finalizar_app():
    os.system("cls")
    print("Finalizando o app")


def escolher_opção():
    opção_escolhida = int(input("Escolha uma opção: "))

    if opção_escolhida == 1:
        print("cadastrar restaurante")
    elif opção_escolhida == 2:
        print("listar restaurantes")
    elif opção_escolhida == 3:
        print("ativar restaurante")
    else:
        finalizar_app()

def main ():
    exibir_nome_programa()
    exibir_opções()
    escolher_opção()

if __name__ == "__main__" :
    main()
