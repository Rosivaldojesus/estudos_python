import json
import os



pessoas = [
    {
        "nome": "Rosivaldo",
        "Sobrenone": "Jesus",
        "idade": 32,

        "telefones": {
            "residencial": "00 0000-0000",
            "Celular": "00 00000-0000",
        }
    
    },
    {
        "nome": "Rosivaldo",
        "Sobrenone": "Jesus",
        "idade": 32,

        "telefones": {
            "residencial": "00 0000-0000",
            "Celular": "00 00000-0000",
        }
    
    }

]


# Para salvar
BASE_DIR = os.path.dirname(__file__), 
SAVE_TO = os.path.join(BASE_DIR, 'caminho_do_arquivo.json')

with open(SAVE_TO, 'w') as file:
    json.dump(pessoas, file, indent=2)

