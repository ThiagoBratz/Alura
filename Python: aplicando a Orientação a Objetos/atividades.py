
class Musica:
    def __init__(self, nome="", artista="", duracao=0):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao


musica1 = Musica(
    nome="Capitão de Praia",
    artista="Matuê",
    duracao=140
)

musica2 = Musica(
    nome="Me Lambe",
    artista="Raimundos",
    duracao=183
)

musica3 = Musica(
    nome="Shape of You",
    artista="Ed Sheeran",
    duracao=234
)

class Carro:
    def __init__(self, marca="", modelo="", ano=0, cor=""):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor


carro1 = Carro(
    marca="Volkswagen",
    modelo="Fusca",
    ano=1970,
    cor="Azul"
)

class Restaurante:
    def __init__(self, nome, categoria, capacidade=0,
                 nota_avaliacao=0.0, ativo=False):
        self.nome = nome
        self.categoria = categoria
        self.capacidade = capacidade
        self.nota_avaliacao = nota_avaliacao
        self.ativo = ativo

    def __str__(self):
        return f"{self.nome} | {self.categoria}"


restaurante_exemplo = Restaurante(
    nome="Comida Boa",
    categoria="Gourmet",
    capacidade=50,
    nota_avaliacao=4.5,
    ativo=True
)

novo_restaurante = Restaurante(
    nome="Santa Marmita",
    categoria="Fast Food"
)

restaurante_formatado = Restaurante(
    nome="Bom Sabor",
    categoria="Tradicional"
)

restaurante_praca = Restaurante(
    nome="Praça",
    categoria="Brasileira"
)

restaurante_praca.categoria = "Italiana"
nome_do_restaurante = restaurante_praca.nome

if restaurante_praca.ativo:
    print("O restaurante está ativo.")
else:
    print("O restaurante está inativo.")

categoria = restaurante_praca.categoria
restaurante_praca.nome = "Bistrô"

restaurante_pizza = Restaurante(
    nome="Pizza Place",
    categoria="Fast Food"
)

restaurante_pizza.ativo = True

print(restaurante_pizza.categoria)

print(
    f"Restaurante: {restaurante_praca.nome}, "
    f"categoria: {restaurante_praca.categoria}"
)

print(restaurante_formatado)


class Cliente:
    def __init__(self, nome, idade, email, telefone):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.telefone = telefone


cliente1 = Cliente(
    nome="Alice",
    idade=25,
    email="alice@gmail.com",
    telefone="123-456-7890"
)

cliente2 = Cliente(
    nome="Bob",
    idade=30,
    email="bob@gmail.com",
    telefone="987-654-3210"
)

cliente3 = Cliente(
    nome="Charlie",
    idade=22,
    email="charlie@gmail.com",
    telefone="555-123-4567"
)

class Pessoa:
    def __init__(self, nome="", idade=0, profissao=""):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def __str__(self):
        return f"{self.nome}, {self.idade}, {self.profissao}"

    def aniversario(self):
        self.idade += 1

    @property
    def saudacao(self):
        if self.profissao:
            return f"Olá, trabalho como {self.profissao}."
        else:
            return f"Olá, me chamo {self.nome}."


pessoa1 = Pessoa(
    nome="Alice",
    idade=25,
    profissao="Engenheira"
)

pessoa2 = Pessoa(
    nome="Luiza",
    idade=30,
    profissao="Desenvolvedora"
)

pessoa3 = Pessoa(
    nome="Jaque",
    idade=22
)

print("\nInformações Iniciais:")
print(pessoa1)
print(pessoa2)
print(pessoa3)

pessoa1.aniversario()
pessoa3.aniversario()

print("\nInformações após aniversário:")
print(pessoa1)
print(pessoa3)

print()
print(pessoa1.saudacao)
print(pessoa2.saudacao)
print(pessoa3.saudacao)


class ContaBancaria:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False

    @property
    def titular(self):
        return self._titular

    @property
    def saldo(self):
        return self._saldo

    @property
    def ativo(self):
        return self._ativo

    def ativar_conta(self):
        self._ativo = True


conta1 = ContaBancaria("Thiago", 2000)
conta2 = ContaBancaria("Lara", 2500)

print(conta1.titular)
print(conta2.titular)

conta3 = ContaBancaria("Carlos", 200)

print(f"Antes de ativar: Conta ativa? {conta3.ativo}")

conta3.ativar_conta()

print(f"Depois de ativar: Conta ativa? {conta3.ativo}")

conta4 = ContaBancaria("Fernanda", 1500)

print(f"Titular da conta 4: {conta4.titular}")


class ClienteBanco:
    def __init__(self, nome, idade, endereco, cpf, profissao):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.cpf = cpf
        self.profissao = profissao


    @classmethod
    def criar_conta(cls, titular, saldo_inicial):
        conta = ContaBancaria(titular, saldo_inicial)
        return conta


cliente_banco1 = ClienteBanco(
    nome="Thiago",
    idade=18,
    endereco="Porto Alegre",
    cpf="000.000.000-00",
    profissao="Estudante"
)

conta_cliente = ClienteBanco.criar_conta("Thiago", 1500)

print(f"\nConta criada para: {conta_cliente.titular}")
print(f"Saldo inicial: R$ {conta_cliente.saldo:.2f}")


class Livro:
    def __init__(self, titulo, autor, ano_pub):
        self.titulo = titulo
        self.autor = autor
        self.ano_pub = ano_pub
        self.disponivel - True

    def __str__(self):
                return f"Livro: {self.titulo} | Autor: {self.autor} | Ano de Publicação: {self.ano_publicacao}"

    def emprestar(self):
        self.disponivel = False

livro1 = Livro("Aprendendo Python", "John Doe", 2022)
livro2 = Livro("Data Science Fundamentals", "Jane Smith", 2020)

print(livro1)
print(livro2)

livro3 = Livro("Python Cookbook", "Samuel Developer", 2019)
print(f"Antes de emprestar: Livro disponível? {livro3.disponivel}")
livro3.emprestar()
print(f"Depois de emprestar: Livro disponível? {livro3.disponivel}")

@staticmethod
def verificar_disponibilidade(ano):
        livros_disponiveis = [livro for livro in Livro.livros if livro.ano_publicacao == ano and livro.disponivel]
        return livros_disponiveis

Livro.livros = [livro1, livro2, livro3]

ano_especifico = 2026
livros_disponiveis_ano = Livro.verificar_disponibilidade(ano_especifico)
print(f"Livros disponíveis em {ano_especifico}: {livros_disponiveis_ano}")