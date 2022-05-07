"""
Atributos -> Representam as caracteristicas do objeto. Ou seja, pelos atributos nós conseguimos representar
computacionalmente os estados de um objeto.

Em Python, dividimos os atributos em 3 grupos:
    - Atributos de Instância;
    - Atributos de Classe.
    Atributos Dinâmicos;

    -> Atributos de instância: São atributos declarados dentro do método construtor.

    OBS.: Método contrutor: É um método esoecial utilizado para a construção do objeto.
"""

class Lampada():

    def __init__(self, voltagem, cor, ligada) -> None:
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False


class ContaCorrente():

    def __init__(self, numero, limite, saldo) -> None:
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


class Produto():

    def __init__(self, nome, descricao, valor) -> None:
        self.nome = nome
        self.descricao = descricao
        self.valor = valor

    def descricao_produto(self):
        print(self.nome)


class Usuario():

    def __init__(self, nome, email, senha) -> None:
        self.nome = nome
        self.email = email
        self.senha = senha

    

prod = Produto('Geladeira1', 'Serve para gelar', '1000' )

print(prod.descricao_produto())


