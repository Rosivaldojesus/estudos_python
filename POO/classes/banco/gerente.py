from funcionario import Funcionario

class Gerente(Funcionario):
    def __init__(self, nome, endereco, cpf, data_nascimento, cargo, matricula, senha, salario, qnt_funcionarios):
        super().__init__(nome, endereco, cpf, data_nascimento, cargo, matricula, senha, salario)
        self._qnt_funcionarios = qnt_funcionarios

    def calcular_gratificacao(self):
        return self._salario * 0.15