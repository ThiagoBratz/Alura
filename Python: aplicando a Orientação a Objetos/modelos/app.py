from restaurantes import Restaurante
#import bebida
#import prato


restaurante_praca = Restaurante("praca", "gourmet")
bebida_suco = Bebida("suco de melancia", 5.0, "grande")
prato_paozinho = ("paozinho", 2.0, "o melhor pao da cidade")
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_paozinho)

def main():
    print

if __name__ == "__main__":
    main()