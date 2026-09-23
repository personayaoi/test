import json

class Aluno:
    def __init__(self, nome, dinheiro):
        self.nome = nome
        self.dinheiro = dinheiro

    def apresentar(self):
        print(f"Oi eu sou aluno {self.nome} e ganho {self.dinheiro} de salario")


alunos = []
alunos.append(Aluno("Yu", "R$10000"))
alunos.append(Aluno("Yosuke", "R$2"))
alunos.append(Aluno("Chie", "R$3"))

jsonS = [
    {
        "nome" : aluno.nome,
        "dinheiro" : aluno.dinheiro
    } for aluno in alunos
]

def salvarJson(dados_json):
    with open(file="arq.json", mode='w') as pew:
        pew.write(json.dumps(dados_json, indent=4))
salvarJson(jsonS)

def carregarJson():
    with open(file="arq.json", mode='r') as pew:
        return json.load(pew)

dados_alunos = carregarJson()
for aluno in dados_alunos:
    alunos.append(Aluno(aluno["nome"], aluno["dinheiro"]))

for aluno in alunos:
    aluno.apresentar()

    carregarJson()