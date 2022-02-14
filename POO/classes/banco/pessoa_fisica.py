from pessoa import Pessoa

class PessoaFisica(Pessoa):
    def __init__(self, nome, endereco, cpf, data_nascimento):
        super().__init__(nome, endereco)
        self.cpf = cpf
        self.data_nascimento = data_nascimento

    def validar_cpf(cpf=None):
        if cpf is not None:
            return
        return False

