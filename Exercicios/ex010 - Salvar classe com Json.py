#Salve sua classe com Json, salve os dados da sua classe em jasoon e depois crie novamente as instâncias da classe com os dados salvos, faça em arquivos separados

import json

CAMINHO_ARQUIVO = 'ex010.json'

class Pessoa:
    def __init__(self,nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa('Bianca', 20)
p2 = Pessoa('Alan', 23)
p3 = Pessoa('Amanda', 20)
bd = [vars(p1), p2.__dict__,vars(p3)]

with open(CAMINHO_ARQUIVO, 'w') as arquivo:
    json.dump(bd, arquivo, ensure_ascii=False, indent=2)
    