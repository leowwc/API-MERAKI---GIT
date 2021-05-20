import csv

nomes = ""
with open('Networks.csv', 'r') as entrada_dados:
    dados = csv.reader(entrada_dados)
    next(dados)
    for linha in dados:
        nomes = nomes + "," + "'" + linha[0] + "'"
        with open('zzzTODAS_NETWORK_.json', 'w+') as file:
            # Armazena (ESCREVE) os dados da vlan no arquivo aberto
            file.write(nomes)


