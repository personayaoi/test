import json

class Aluno:
    def __init__(self, nome, turma):
        self.nome = nome
        self.turma = turma

    def apresentar(self):
        print(f"Oi eu sou aluno {self.nome} e sou da turma {self.turma}")

lista_alunos = []

jsonS = [
    {
        "nome" : aluno.nome,
        "turma" : aluno.turma
    } for aluno in lista_alunos
]

def salvarJson(dados_json):
    with open(file="arq.json", mode='w') as morgana:
        morgana.write(json.dumps(dados_json, indent=4))
#salvarJson(jsonS)

def carregarJson():
    with open(file="arq.json", mode='r') as morgana:
        return json.load(morgana)

dados_alunos = carregarJson()
for aluno in dados_alunos:
    lista_alunos.append(Aluno(aluno["nome"], aluno["turma"]))

for aluno in lista_alunos:
    aluno.apresentar()