# print ("Python na Escola de Programação da Alura")

# nome = "Thiago"
# Idade = 17

# print("Meu nome é", nome, "tenho", Idade, "anos e sou foda")

# print("A", "L", "U", "R", "A", sep="\n")

# pi = 3.14159

# print("O valor arredondado de pi é", pi)

# print("EXERCÍCIO 2\n")


# número = int(input("Escolha um número"))
# if número == 2:
#     print("Este número é par")
# elif número == 4:
#     print("Este número é par")
# elif número == 6:
#     print("Este número é par")
# elif número == 8:
#     print("Este número é par")
# elif número == 1:
#     print("Este número é ímpar")
# elif número == 3:
#     print("Este número é ímpar")
# elif número == 5:
#     print("Este número é ímpar")
# elif número == 7:
#     print("Este número é ímpar")
# elif número == 9:
#     print("Este número é ímpar")
# else:
#     print("Resposta inválida")


# idade = int(input("Qual a sua idade?"))
# if 0 < idade <= 12:
#     print("criança")
# elif 12 < idade < 18:
#     print("Adolescente")
# elif idade >= 18:
#     print("Adulto")

# usuário_correto = "kaleu"
# senha_certa = "kaleu"

# usuário = input("Digite o nome do usuário:")
# senha = input("digite a senha do usuário:")

# if usuário == usuário_correto and senha == senha_certa:
#     print("Acesso liberado.")
# else:
#     print("Credenciais inválidas")


# cordenadas_x = int(input("Qual a cordenada X?"))
# cordenadas_y = int(input("Qual a cordenada ?"))

# if cordenadas_x > 0 and cordenadas_y > 0:
#     print("Primeiro quadrante")
# elif cordenadas_x < 0 and cordenadas_y > 0:
#     print("Segundo quadrante")
# elif cordenadas_x < 0 and cordenadas_y < 0:
#     print("Terceiro quadrante")
# elif cordenadas_x > 0 and cordenadas_y < 0:
#     print("Quarto quadrante")
# else:
#     print("o ponto está localizado no eixo ou origem")

#lista_preços = [1500, 100, 500, 2000]

#taxa_imposto = 0.1


#for preço in lista_preços:
    #imposto = preço * taxa_imposto
    #print(f"preço do produto {preço}, imposto é de {imposto}")


#total_imposto = 0
#for preço in lista_preços:
 #   if preço > 1000:
#        taxa = 0.15
 #   else:
 #       taxa = 0.1
 #   imposto = taxa * preço
#
#    total_imposto = total_imposto + imposto
#
#    print(f"preço do produto: {preço}, imposto: {imposto}\n") 
#    print(total_imposto)


lista_números = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# lista_nomes = ["Thiago", "Gabriel", "Eduardo", "Nicolas"]
# lista_anos = [2009, 2026]
# soma_impar = 0

# # for número in lista_números:
# #     if número %2:
# #         soma_impar = soma_impar + número

# # print(soma_impar)

# # lista_números.sort(reverse=True)
# # print(lista_números)

# for número in range(10, 0, -1):
#     print(número)

#número_usuário = int(input("Escolha um número: "))

# for número in lista_números:
#     tabuada = número_usuário * número
#     print(tabuada)

#for número in range(1, 11, 1):
#    tabuada = número_usuário * número
#    print (f"{número_usuário} X {número} = {tabuada}")

# lista = [10, 20, "30", 40]
# soma = 0

# for número in lista:
#     try:
#         soma = soma + número
#     except:
#         pass

# print(soma)


lista_números_2 = [7, 6, 10, 9, 6]


valor_lista = len(lista_números_2)
if valor_lista > 0:
    média_lista = sum(lista_números_2) / len(lista_números_2)
    print(média_lista)
elif valor_lista <= 0:
    pass
