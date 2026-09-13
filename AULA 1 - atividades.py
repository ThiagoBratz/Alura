print ("Python na Escola de Programação da Alura")

nome = "Thiago"
Idade = 17

print("Meu nome é", nome, "tenho", Idade, "anos e sou foda")

print("A", "L", "U", "R", "A", sep="\n")

pi = 3.14159

print("O valor arredondado de pi é", pi)

print("EXERCÍCIO 2\n")


número = int(input("Escolha um número"))
if número == 2:
    print("Este número é par")
elif número == 4:
    print("Este número é par")
elif número == 6:
    print("Este número é par")
elif número == 8:
    print("Este número é par")
elif número == 1:
    print("Este número é ímpar")
elif número == 3:
    print("Este número é ímpar")
elif número == 5:
    print("Este número é ímpar")
elif número == 7:
    print("Este número é ímpar")
elif número == 9:
    print("Este número é ímpar")
else:
    print("Resposta inválida")


idade = int(input("Qual a sua idade?"))
if 0 < idade <= 12:
    print("criança")
elif 12 < idade < 18:
    print("Adolescente")
elif idade >= 18:
    print("Adulto")

usuário_correto = "kaleu"
senha_certa = "kaleu"

usuário = input("Digite o nome do usuário:")
senha = input("digite a senha do usuário:")

if usuário == usuário_correto and senha == senha_certa:
    print("Acesso liberado.")
else:
    print("Credenciais inválidas")


cordenadas_x = int(input("Qual a cordenada X?"))
cordenadas_y = int(input("Qual a cordenada ?"))

if cordenadas_x > 0 and cordenadas_y > 0:
    print("Primeiro quadrante")
elif cordenadas_x < 0 and cordenadas_y > 0:
    print("Segundo quadrante")
elif cordenadas_x < 0 and cordenadas_y < 0:
    print("Terceiro quadrante")
elif cordenadas_x > 0 and cordenadas_y < 0:
    print("Quarto quadrante")
else:
    print("o ponto está localizado no eixo ou origem")