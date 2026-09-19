import os

restaurantes = [{"nome" : "praça", "categoria" : "japonesa", "ativo" : False}, 
                {"nome" : "pizza suprema", "categoria" : "pizza","ativo" :True},
                 {"nome" : "cantina", "categoria" : "italiana", "ativo" :False}]

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
    print("3. Alternar estado do restaurante")
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
    linha = "*" * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    exibir_subtitulos ("Cadastro de novos restaurantes")
    nome_do_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    categoria = input(f"Digite o nome da caterogira do restaurante {nome_do_restaurante} ")
    dados_do_restaurante = {"nome" : nome_do_restaurante, "categoria" : categoria, "ativo":False}
    restaurantes.append(dados_do_restaurante)
    print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n")
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulos("Listando restaurantes")
    print(f"{"Nome do restaurante".ljust(22)} | {"Categoria".ljust(20)} | Status")
    for restaurante in restaurantes:
        nome_restaurante = restaurante["nome"]
        categoria = restaurante["categoria"]
        ativo = "ativado " if restaurante["ativo"] else "desativado"
        print(f"- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}")
    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    exibir_subtitulos("Alternando estado do restaurante")
    nome_restaurante = input("Digite o nome do restaurante que deseja alterar o estado: ")
    restaurante_encontrado = False

    for restaurante in restaurantes:
     if nome_restaurante == restaurante["nome"]:
        restaurante_encontrado = True
        restaurante["ativo"] = not restaurante["ativo"]
        mensagem = (f"O restaurante {nome_restaurante} foi ativado com sucesso") if restaurante["ativo"] else f"o restaurante {nome_restaurante} foi desativado com sucesso"
        print(mensagem)
    if not restaurante_encontrado:
        print("O restaurante não foi encontrado")

    voltar_ao_menu_principal()

def escolher_opção():
    try:
        opção_escolhida = int(input("Escolha uma opção: "))

        if opção_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opção_escolhida == 2:
            listar_restaurantes()
        elif opção_escolhida == 3:
            alternar_estado_restaurante()   
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
