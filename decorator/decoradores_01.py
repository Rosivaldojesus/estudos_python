"""
Decoradores (Decorators)

- Decorators: São funções;
- Decorators envolvem outras funções e aprimoram seus comportamentos;
- Decorators também são exemplos de Higher Order Functions;

/----------------- Function Decorator --------------------------------------------------/

/----------------- Function Decorator --------------------------------------------------/

"""


def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print('Foi um przaer conhecer você!')
        funcao()
        print('Tenha um excelente dia!')

    return sendo_mesmo


@seja_educado_mesmo
def apresentando():
    print('Meu nome é João')


apresentando()


@seja_educado_mesmo
def dormir():
    print('Quero dormir....')


dormir()


