class musica:
    nome = ""
    artista = ""
    duração = int

musica1 = musica()
musica1.nome = "capitãod de praia"
musica1.artista = matue
musica1,duração = 140

musica2 = musica()
musica2.nome = 'me lambe'
musica2.artista = 'raimundos'
musica2.duração = 183

musica3 = Musica()
musica3.nome = 'Shape of You'
musica3.artista = 'Ed Sheeran'
musica3.duracao = 234

restaurante_praca.categoria = "italiana"

nome_do_restaurante = restaurante_praca.nome

if restaurante_praca.ativo:
    print("o restaurante esta ativo.")
else:
    print("o restaurante esta inativo.")

categoria = restaurante_praca.categoria

restaurante_praca.nome = "Bistrô"

restaurante_pizza = Restaurante ()
restaurante_pizaz.nome = "pizza place
restaurante_pizza.categoria ="fast food"

print (restaurante_pizza.categoria)

restaurante_pizza.ativo = True

print(f"restaurante: {restaurante_praca.nome}, catehoria: {restaurante_praca.categoria}")

class Musica:
    def __init__(self, nome="", artista="", duracao=0):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao

musica1 = Musica(nome='Under Pressure', artista='Queen & David Bowie', duracao=248)
musica2 = Musica(nome='The Trooper', artista='Iron Maiden', duracao=245)
musica3 = Musica(nome='Hotel California', artista='Eagles', duracao=390)


# 1) Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano.
#    Crie uma instância dessa classe e atribua valores aos seus atributos.


class Carro:
    def __init__(self, marca = "", modelo = "", ano = "", cor = ""):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

carro1 = Carro(modelo=Fusca', cor='Azul', ano=1970)

class Restaurante:
    def __init__(self, nome, categoria, capacidade, nota_avaliacao, ativo=False):
        self.nome = nome
        self.categoria = categoria
        self.capacidade = capacidade
        self.nota_avaliacao = nota_avaliacao
        self.ativo = ativo

# Instanciando um restaurante e atribuindo valores aos seus atributos
restaurante_exemplo = Restaurante(
    nome='Comida Boa',
    categoria='Gourmet',
    capacidade=50,
    nota_avaliacao=4.5,
    ativo=True
)



# 3) Modifique a classe Restaurante adicionando um construtor que aceita nome e categoria como parâmetros
#    e inicia ativo como False por padrão. Crie uma instância utilizando o construtor.

class Restaurante:
    def __init__(self, nome, categoria, capacidade=0, nota_avaliacao=0.0, ativo=False):
        self.nome = nome
        self.categoria = categoria
        self.capacidade = capacidade
        self.nota_avaliacao = nota_avaliacao
        self.ativo = ativo

# Instanciando um restaurante utilizando o construtor
novo_restaurante = Restaurante(nome='Santa Marmita', categoria='Fast Food')



# 4) Adicione um método especial __str__ à classe Restaurante para que, ao imprimir uma instância,
#    seja exibida uma mensagem formatada com o nome e a categoria. Exiba essa mensagem para uma instância de restaurante.

class Restaurante:
    def __init__(self, nome, categoria, capacidade=0, nota_avaliacao=0.0, ativo=False):
        self.nome = nome
        self.categoria = categoria
        self.capacidade = capacidade
        self.nota_avaliacao = nota_avaliacao
        self.ativo = ativo

    def __str__(self):
        return f'{self.nome} | {self.categoria}'

# Exibindo uma instância do restaurante formatada
restaurante_formatado = Restaurante(nome='Bom Sabor', categoria='Tradicional')
print(restaurante_formatado)



# 5) Crie uma classe chamada Cliente e pense em 4 atributos.
#    Em seguida, instancie 3 objetos desta classe e atribua valores aos seus atributos através de um método construtor.

class Cliente:
    def __init__(self, nome, idade, email, telefone):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.telefone = telefone

# Instanciando três objetos da classe Cliente e atribuindo valores aos seus atributos através do construtor
cliente1 = Cliente(nome='Alice', idade=25, email='alice@gmail.com', telefone='123-456-7890')
cliente2 = Cliente(nome='Bob', idade=30, email='bob@gmail.com', telefone='987-654-3210')
cliente3 = Cliente(nome='Charlie', idade=22, email='charlie@gmail.com', telefone='555-123-4567')

class pessoa:
    def __init__(self, nome = "", idade ="", profissao = ""):
        self,nome = nome
        self.idade = idade
        self.profissao = profissao

    def __str__(self):
        return f"{self.nome}, {self.idade}, {self.profissao}"

    def aniversario(self):
        self.idade +=1

    @property
    def saudacao(self):
        if self profissao:
            return "ola, trabalho como {self.profissao}"
        else:
            return f"ola, me chamo {self.nome}"

pessoa1 = Pessoa(nome='Alice', idade=25, profissao='Engenheira')
pessoa2 = Pessoa(nome='Luiza', idade=30, profissao='Desenvolvedor')
pessoa3 = Pessoa(nome='Jaque', idade=22)

print("Informações Iniciais:")
print(pessoa1)
print(pessoa2)
print(pessoa3)
print()

pessoa1.aniversario()
pessoa3.aniversario()

print("Informações após aniversário:")
print(pessoa1)
print(pessoa3)
print()

print(pessoa1.saudacao)
print(pessoa2.saudacao)
print(pessoa3.saudacao)

class conta_bancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        self._ativo = False