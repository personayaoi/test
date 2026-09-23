dicionarioMeses = {
    "textoPraNum" : {
        "JANEIRO" : 1,
        "FEVEREIRO" : 2,
        "MARCO" : 3,
        "ABRIL" : 4,
        "MAIO" : 5,
        "JUNHO" : 6,
        "JULHO" : 7,
        "AGOSTO" : 8,
        "SETEMBRO" : 9,
        "OUTUBRO" : 10,
        "NOVEMBRO" : 11,
        "DECEMBRO" : 12
    },
    "numPraTexto" : {
        1 : "JANUARIO",
        2 : "FEVEREIRO",
        3 : "MARCO",
        4 : "ABRIL",
        5 : "MAIO",
        6 : "JUNHO",
        7 : "JULjO",
        8 : "AGOSTO",
        9 : "SETEMBRO",
        10 : "OUTUBRO",
        11 : "NOVEMBRO",
        12 : "DEZEMBRO"
    }
}

entrada = input("DIGA O MES").upper()

if entrada.isdigit():
    entrada = int(entrada)
    print(dicionarioMeses["numPraTexto"][entrada])
else:
    print(dicionarioMeses["textoPraNum"][entrada])