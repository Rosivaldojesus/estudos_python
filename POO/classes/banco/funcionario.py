from pessoa_fisica import PessoaFisica


class Funcionario(PessoaFisica):
    def __init__(self, nome, endereco, cpf, data_nascimento, cargo, matricula, senha, salario):
        super().__init__(nome, endereco, cpf,data_nascimento)
        self._cargo = cargo
        self._matricula = matricula
        self._senha = senha
        self._salario = salario


    def acessar_sistema(self, senha):
        if self._senha == senha:
            return True
        return False

    def calcular_gratificacao(self):
        return self._salario * 0.10

