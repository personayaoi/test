#ano = 2026
#year = 2010

#print (f"Quantos anos você tem?")
#print (f"Você tem {ano - year} anos")



#a = 2026
#b = 2010

#def descobre_idade(anoA, anoN):
#    idade = anoA - anoN
#    print(idade)

#descobre_idade(anoA= a, anoN = b)

anoNasc = int(input("Que ano o sahurzinho nasceu?")) #pergunta que ano o sahurzinho nasceu (a)
anoAtual = int(input("Que ano estamos?")) #pergunta qual ano estamos (b)

def descobre_idade(anoA, anoN): #define a função descobre_idade
    idade = anoA - anoN #conta pra calcular a idade (a+b)
#    print(f"Então o sahurzinho tem {idade} anos")
    return idade #encerra a execução de uma função e envia um resultado de volta pro código

print(f"Então o sahurzinho tem {descobre_idade(anoA= anoAtual, anoN = anoNasc)} anos") #define oq é o AnoA e AnoN, e também a idade do sahurzinho

#descobre_idade(anoA= anoAtual, anoN = anoNasc)