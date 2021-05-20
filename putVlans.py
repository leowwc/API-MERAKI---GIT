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
# Headers
headers = {
    'Content-Type': 'application/json',
    'X-Cisco-Meraki-API-Key': 'd15e75a6f1578e190bcdf2c8e6eb9524d75dfd23'

}

# Armazena a network que deseja baixar as vlans
inputName = input("Digite o nome da Loja desejada: ")
nomes = inputName
# Converte em String
str(nomes)

# Abre um arquivo salvo cujo o nome é vlan_ SIGLA _.json e lê todos os dados, sem possibilidade de editar
with open("vlan_"+nomes+"_.json", "r") as file:
      # Armazeno todos os dados do arquivo em uma variavel
      vlanJson = file.read()
      # Carrego os dados armazenados no objeto em JSON
      vlanJson = json.loads(vlanJson)

      # Percorre as vlans contidas na variavel, onde cada linha é uma listVlan
      for listVlan in vlanJson:
          # Armazena a URL para efetuar o UPDATE da VLAN atuante do momento
          updateUrl = mainUrl + "/networks/{}/appliance/vlans/{}".format(listVlan["networkId"],listVlan["id"])
          # Adicionamos a vlan atuante em um objeto separado
          corpoListaVlan = listVlan
          # Compactamos o objeto em formato json
          corpoJson = json.dumps(corpoListaVlan)
          # Invocamos o metodo de requisição PUT para enviar os dados a API
          responseUpdate = requests.put(url=updateUrl, headers=headers, data=corpoJson)
          # Caso o método tenha sucesso, ele é armazenado na variavel responseUpdate com o valor = 200
          if responseUpdate.status_code == 200:
              print("VLAN "+str(listVlan["id"])+" atualizada com sucesso!")
          else:
              print("Falha ao atualizar a VLAN")
