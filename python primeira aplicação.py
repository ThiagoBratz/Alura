import os

restaurantes = [{"nome" : "praça", "categoria" : "japonesa", "ativo" : False}, 
                {"nome" : "pizza suprema", "categoria" : "pizza","ativo" :True},
                 {"nome" : "camtina", "categoria" : "italiana", "ativo" :False}]

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
    exibir_subtitulos("Finalizando programa")

def voltar_ao_menu_principal():
    input("Digite uma tecla para voltar ao menu principal: ")
    main()

def opção_inválida():
    print("Opção inválida!\n")
    voltar_ao_menu_principal()

def exibir_subtitulos(texto):
    os.system("cls")
    print(texto)
    print()

def cadastrar_novo_restaurante():
    exibir_subtitulos ("Cadastro de novos restaurantes")
    nome_do_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    restaurantes.append(nome_do_restaurante)
    print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n")
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulos("Listando restaurantes")
    for restaurante in restaurantes:
        nome_restaurante = restaurante["nome"]
        categoria = restaurante["categoria"]
        ativo = restaurante["ativo"]
        print(f"- {nome_restaurante} | {categoria} | {ativo}")
    voltar_ao_menu_principal()

def escolher_opção():
    try:
        opção_escolhida = int(input("Escolha uma opção: "))

        if opção_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opção_escolhida == 2:
            listar_restaurantes()
        elif opção_escolhida == 3:
            print("ativar restaurante")
        elif opção_escolhida == 4:
            finalizar_app()
        else:
            opção_inválida()
    except:
        opção_inválida



def main ():
    os.system("cls")
    exibir_nome_programa()
    exibir_opções()
    escolher_opção()

if __name__ == "__main__" :
    main()
