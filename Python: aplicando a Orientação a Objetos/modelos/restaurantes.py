class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f"{self._nome} | {self.categoria}"

    @classmethod
    def listar_restaurantes(cls):
        print(f"{"nome do restaurante".ljust(25)} | {"categoria do restaurante".ljust(25)} | {"status do restaurante".ljust(25)}")
        for restaurante in cls.restaurantes:
            print(f"{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo}")


    @property
    def ativo(self):
            return "¶" if self._ativo else "♞"

    def alternar_estado(self):
         self._ativo = not self._ativo

restaurante_praca = Restaurante("praca", "gourmet")
restaurante_praca.alternar_estado
restaurante_pizza = Restaurante("pizza empress", "italiana")

Restaurante.listar_restaurantes()


