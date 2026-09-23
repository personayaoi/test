class Aluno:
    def __init__(self, nome, turma):
        self.nome = nome
        self.turma = turma

    def apresentar(self):
        print(f"Oi eu sou aluno {self.nome} e sou da turma {self.turma}")

alunos = []
alunos.append(Aluno("Amanda", "ProgWeb"))
alunos.append(Aluno("trump", "ProgWeb"))
alunos.append(Aluno("kirk", "ProgWeb"))

#aluno1=Aluno("minion")
#aluno1.estudar()

#aluno2=Aluno("papoi")
#aluno2.estudar()


#lista.append() #-insere um valor em uma lista
#lista.pop() #-remove o valor de uma lista