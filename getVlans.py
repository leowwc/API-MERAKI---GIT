import requests
import json


# Meraki URL API - URL Base de comunicação via API
mainUrl = "https://api.meraki.com/api/v1"
# OrganizationId da ARCOS DOURADOS BR
orgId = "635570497412663072"
# API-KEY - Esta API é de uso individual, onde cada usuário deve registrar a sua
apiKey = "'X-Cisco-Meraki-API-Key': 'd15e75a6f1578e190bcdf2c8e6eb9524d75dfd23'"
# URL para GET, onde busca todas as Networks na organização
netIdUrl = mainUrl + "/organizations/{}/networks".format(orgId)
# Criando os headers - Todo cabeçalho deve seguir de acordo com o proposto pela Meraki-API
payload = {}
# Headers necessários apenas para os métodos.
headers = {

    'Content-Type': 'application/json',
    'X-Cisco-Meraki-API-Key': 'd15e75a6f1578e190bcdf2c8e6eb9524d75dfd23'

}
# Requisitando todas as networks na organização
responseNet = requests.get(url=netIdUrl, headers=headers)
responseNetJson = json.loads(responseNet.content)

# Armazena a network que deseja baixar as vlans
inputName = input("Digite o nome da Loja desejada: ")
nomes = inputName
# Converte em string
str(nomes)

# Procurando a network cujo está na variavel nomes
for listNetwork in responseNetJson:
    # Percorre todas as linhas no objeto responseNetJson armazenando cada uma na variavel listNetwork
    if listNetwork["name"] in nomes:
        # Armazena o nome da network
        netName = listNetwork["name"]
        # Armazena o id da network
        netId = listNetwork["id"]
        print("Network a ser Modificada \t Nome: {}, Network_ID: {} ".format(netName, netId))
        # Faz uma tentativa, onde caso ocorra um erro, é efetuado o tratamento na captura
        try:
            # Armazena a URL para buscar todas as VLANs da network irformada ( variavel netId )
            vlanUrl = mainUrl + "/networks/{}/appliance/vlans".format(netId)
            # Armazena o resultado da requisição GET
            responseVlans = requests.get(url=vlanUrl, headers=headers)
            # Converte os dados em json para leitura
            vlanJson = json.loads(responseVlans.content)
            # Compacta a variavel vlanArquivo para o formato json, com identação organizada.
            vlanArquivo = json.dumps(vlanJson, indent=True)
            # Abre um arquivo com o nome vlan_ Sigla _.json, onde caso exista outro igual, ele subscreve.
            with open('vlan_'+listNetwork["name"]+'_.json', 'w+') as file:
                # Armazena (ESCREVE) os dados da vlan no arquivo aberto
                file.write(vlanArquivo)
            print("Vlans salvas com sucesso !!!!")
        except:
                # Caso a base não tenha dados ou gere algum tipo de erro na busca.
                print("Erro ao buscar as VLAN's")
