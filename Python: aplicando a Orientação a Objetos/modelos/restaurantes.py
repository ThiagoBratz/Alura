class Restaurante:
    nome = ""
    categoria = ""
    ativo = False

restaurante_praca = Restaurante()
restaurante_praca.nome = "praca"
restaurante_praca.categoria = "gourmet"


restaurante_pizza = Restaurante()

restaurantes = [restaurante_praca, restaurante_pizza]

print (vars(restaurante_praca))