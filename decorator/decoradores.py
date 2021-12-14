"""
Decoradores (Decorators)

- Decorators: São funções;
- Decorators envolvem outras funções e aprimoram seus comportamentos;
- Decorators também são exemplos de Higher Order Functions;

/----------------- Function Decorator --------------------------------------------------/

/----------------- Function Decorator --------------------------------------------------/

"""


def seja_educado(funcao):
    def sendo():
        print('Foi um prazer conhece você')
        funcao()
        print('Tenha um ótimo dia!')
    return sendo


def saudacao():
    print('Seja bem vindo a Pythonlândia')


saudando = seja_educado(saudacao)
saudando()
