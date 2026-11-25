class Banco:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco

class Agencia(Banco):
    def __init__(self, nome, endereco, numero):
        super().__init__(nome, endereco)
        self.numero = numero

class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self._ligado = False

def __str__(self):
    status = "ligado" if self._ligado else "desligado"
    return f"{self.marca} {self.modelo} - Status: {status}"

class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.portas = portas

def __str__(self):
    return f"{super().__str__()} - Portas: {self.portas}"

class Moto(Veiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self.tipo = tipo

def __str__(self):
    return f"{super().__str__()} - Tipo: {self.tipo}"