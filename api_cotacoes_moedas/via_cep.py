import requests


def main():
    cep = input("Digite o cep desejado: ")

    while len(cep) != 8:
        print(f'O cep {cep} é inválido')
        cep = input("Digite um CEP válido Ex.: 0000000: ")

    cep = requests.get("https://viacep.com.br/ws/{}/json/".format(cep))
    address_data = cep.json()

    if 'erro' not in address_data:
        print("==> O cep localizado <==")
        # print(address_data)
        print("CEP: {}".format(address_data['cep']))
        print("Logradouro: {}".format(address_data['logradouro']))
        print("Bairro: {}".format(address_data['bairro']))
        print("Localidade: {}".format(address_data['localidade']))
        print("Estado: {}".format(address_data['uf']))
    else:
        print("CEP Inválido!!!")

    print("===================================================")

    option = input("Deseja realiza uma nova consulta?: \n1. Sim\n2. Não\n")
    if option == 1:
        main()
    else:
        print("Finalizado...")

if __name__ == '__main__':
    main()
