"""
Métodos (funções) -> Representam os comportamentos de objeto, ou seja, ações que este objeto pode realizar
no seu sistema.

Em python, dividimos os métodos em 2 grupos: Métodos de instância e Métodos de Classes


# Métodos de Instância: São métodos que só vai funcionar no objeto instanciado

# O método dunder init __init__ é um método especial chamado de construtor e sua função é construir
o objeto a partir da classe

OBS: Todo elemento em Python que inicia e finaliza com o duplo underline é chamado
de dunder (Double Underline)

OBS: Os métodos/funções dunder em Python, são chamados de de métodos mágicos


produto1 = Produto('Redmi note 9', 'Aparelho celular', 1000)
print(produto1.desconto(10))
"""

class Lampada:

    def __init__(self, cor, voltagem, luminosidade) -> None:
        self.__cor = cor
        self.__luminosidade = luminosidade
        self.__ligada = False


class ContaCorrente: 

    contador = 4999 #Atributo de classe
    
    def __init__(self,  limite, saldo) -> None:
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Produto:

    contador = 0 # Atributo de classe

    def __init__(self, nome, descricao, valor) -> None:
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        return (self.__valor * (100 - porcentagem)) /100  


from passlib.hash import pbkdf2_sha256 as cryp
class Usuario:

    def __init__(self, nome, sobrenome, email, senha) -> None:
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)

    def nome_completo(self): # Aqui é um método
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False



user1 = Usuario('Rosivaldo', 'de Jesus', 'email@email.com', '12345')
user2 = Usuario('Maria', 'de Jesus', 'maria@email.com', '54321')

print(user1.nome_completo())
print(Usuario.nome_completo(user1))

print(user2.nome_completo())


# Métodos de classes