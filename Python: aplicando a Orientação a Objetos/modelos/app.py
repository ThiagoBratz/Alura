from restaurantes import Restaurante

restaurante_praca = Restaurante("praca", "gourmet")
restaurante_praca.receber_avaliacao("thi", 10)
restaurante_praca.receber_avaliacao("lara", 6)
restaurante_praca.receber_avaliacao("miguel", 5)

def main():
    Restaurante.listar_restaurantes()

if __name__ == "__main__":
    main()