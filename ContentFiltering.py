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
# Headers necessários
headers = {
    'Content-Type': 'application/json',
    'X-Cisco-Meraki-API-Key': 'd15e75a6f1578e190bcdf2c8e6eb9524d75dfd23'
}
# Requisitando todas as networks na organização
responseNet = requests.get(url=netIdUrl, headers=headers)
responseNetJson = json.loads(responseNet.content)

nomes = "MAM_TESTE_01"

conteudoFiltro = {
    "blockedUrlPatterns": [
        "bobs.com.br",
        "habibs.com.br",
        "burgerking.com.br",
        "giraffas.com.br",
        "kfcbrasil.com.br",
        "subway.com",
        "pizzahut.com.br",
        "quartahut.com.br"
    ],
    "blockedUrlCategories": [
            "meraki:contentFiltering/category/10",
            "meraki:contentFiltering/category/11",
            "meraki:contentFiltering/category/19",
            "meraki:contentFiltering/category/31",
            "meraki:contentFiltering/category/32",
            "meraki:contentFiltering/category/33",
            "meraki:contentFiltering/category/43",
            "meraki:contentFiltering/category/48",
            "meraki:contentFiltering/category/49",
            "meraki:contentFiltering/category/53",
            "meraki:contentFiltering/category/56",
            "meraki:contentFiltering/category/59",
            "meraki:contentFiltering/category/62",
            "meraki:contentFiltering/category/64",
            "meraki:contentFiltering/category/67",
            "meraki:contentFiltering/category/68",
            "meraki:contentFiltering/category/70",
            "meraki:contentFiltering/category/71",
            "meraki:contentFiltering/category/72"
    ],
    "urlCategoryListSize": "fullList"
}
conteudoJson = json.dumps(conteudoFiltro)

# Procurando a network cujo está na variavel nomes
for listNetwork in responseNetJson:
    if listNetwork["name"] in nomes:
        print(listNetwork["name"])

        contentURL = mainUrl + "/networks/{}/appliance/contentFiltering".format(listNetwork["id"])

        responseUpdate = requests.put(url=contentURL, headers=headers, data=conteudoJson)
        # Caso o método tenha sucesso, ele é armazenado na variavel responseUpdate com o valor = 200
        if responseUpdate.status_code == 200:
            print("Content Filtering Atualizado com Sucesso !!")
            print("\n")
        else:
            print("Falha ao atualizar ")
            print(responseUpdate.status_code)
            print(responseUpdate.url)
            print(responseUpdate.headers)