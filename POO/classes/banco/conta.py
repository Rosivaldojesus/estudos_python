
class Conta:
    def __init__(self, numero, agencia, cliente, saldo):
        self._numero = numero
        self._agencia = agencia
        self._cliente = cliente
        self._saldo = saldo


    def pegar_cliente(self):
        return self._cliente._nome