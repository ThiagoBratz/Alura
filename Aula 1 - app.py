import os

print ("""
╭━━━┳━━━┳━━╮╭━━━┳━━━╮╭━━━┳━╮╭━┳━━━┳━━━┳━━━┳━━━┳━━━╮
┃╭━╮┃╭━╮┃╭╮┃┃╭━╮┃╭━╮┃┃╭━━┻╮╰╯╭┫╭━╮┃╭━╮┃╭━━┫╭━╮┃╭━╮┃
┃╰━━┫┃╱┃┃╰╯╰┫┃╱┃┃╰━╯┃┃╰━━╮╰╮╭╯┃╰━╯┃╰━╯┃╰━━┫╰━━┫╰━━╮
╰━━╮┃╰━╯┃╭━╮┃┃╱┃┃╭╮╭╯┃╭━━╯╭╯╰╮┃╭━━┫╭╮╭┫╭━━┻━━╮┣━━╮┃
┃╰━╯┃╭━╮┃╰━╯┃╰━╯┃┃┃╰╮┃╰━━┳╯╭╮╰┫┃╱╱┃┃┃╰┫╰━━┫╰━╯┃╰━╯┃
╰━━━┻╯╱╰┻━━━┻━━━┻╯╰━╯╰━━━┻━╯╰━┻╯╱╱╰╯╰━┻━━━┻━━━┻━━━╯\n""")

print("1. Cadastrar restaurante")
print("2. Listar restaurante")
print("3. Ativar restaurante")
print("4. Sair\n")

opção_escolhida = int(input("Escolha uma opção: "))

def finalizar_app():
    os.system("cls")
    print("Finalizando o app\n")





if opção_escolhida == 1:
    print("cadastrar restaurante")
elif opção_escolhida == 2:
    print("listar restaurantes")
elif opção_escolhida == 3:
  print("ativar restaurante")
else:
    finalizar_app()
