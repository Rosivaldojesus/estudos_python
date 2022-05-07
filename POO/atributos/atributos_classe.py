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

    

# Atributos de Classe
# ---------------------------------------------------------------------

# Atributos de classe, são atributos, claro, que são declarados diretamente na classe, ou seja,
# fora do construtor. Geralmente já inicializamos um valor, e este valor é compartilhado entre 
# todas as instâncias da classe. Ou seja, ao invés de cada instância da classe ter seus próprios
# valores como é o caso dos atributos de instância, com os atributos de classe todas as instãncia
# terão o mesmo valor para este atributo.


# Atributos Dinâmicos --> Um atributo de instância que pode ser criado em tempo de execução
# ------> obs.: O atributo dinâmico será exclusivo da instãncia que o criou

# Refatorar a classe Produto

class Produto:

    # Atributo de classe
    imposto = 1.05
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id

p1 = Produto('Consul', 'Fogão', 2350)
p2 = Produto('LG', 'Televisão', 1500)
print(Produto.imposto)

print(p1.id)
print(p2.id)


# Adicionado um atributo dinâmico no p3
p3 = Produto('Motorola', 'Celular', 1500)
p3.cor = 'Preto'
print(f'Produto: {p3.nome}, Descrição: {p3.descricao}, Valor: {p3.valor} Cor: {p3.cor}')

print(p3.__dict__)

