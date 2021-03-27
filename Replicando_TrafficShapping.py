# Importando os Modulos Necessários
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
#Headers necessários apenas para os métodos GET
headers = {
     'X-Cisco-Meraki-API-Key': 'd15e75a6f1578e190bcdf2c8e6eb9524d75dfd23'
 }
#Headers necessários para os métodos PUT
headersPUT = {
    'Content-Type': 'application/json',
    'X-Cisco-Meraki-API-Key': 'd15e75a6f1578e190bcdf2c8e6eb9524d75dfd23'

}
# Requisitando todas as networks na organização
responseNet = requests.get(url=netIdUrl, headers=headers)
responseNetJson = json.loads(responseNet.content)

# Network Base onde é retirado a configuração LAB = "MCD_BAR_REST"
# Network's onde será incluso as novas configurações.
# Caso necessário efetuar alteração para busca em arquivo.
nomes = "MCD_CSA_REST"

# Procurando a network cujo está na variavel nomes
for listNetwork in responseNetJson:
        if listNetwork["name"] in nomes:
            netName = listNetwork["name"]
            netId = listNetwork["id"]
            print("Network a ser Modificada \t Nome: {}, Network_ID: {} ".format(netName,listNetwork["id"]))
            #Buscando dados da VLAN 10 na network selecionada
            try:
                 vlanUrl = mainUrl + "/networks/{}/appliance/vlans/10".format(netId)
                 responseVlans = requests.get(url=vlanUrl, headers=headers)
                 vlan10Json = json.loads(responseVlans.content)
                 pcGerencia = vlan10Json["applianceIp"]
                 # Após pegar o IP do MX na vlan 10 com final .14, é substituido o mesmo para final .1
                 # Desta forma podemos efetuar a mudança para o IP desejado, que é o PC GERENCIA.
                 pcGerencia = pcGerencia.replace("14","1/32")
                 # Buscando o ID unico da regra ON PROMISSES.
                 # Esta regra contém um ID unico para cada network.
                 try:
                     urlTS = mainUrl + "/networks/{}/appliance/trafficShaping/customPerformanceClasses".format(
                         listNetwork["id"])
                     reponseTS = requests.get(url=urlTS, headers=headers)
                     baseJson = json.loads(reponseTS.content)
                     for performaceList in baseJson:
                     # Corpo base para PUT, o mesmo deve seguir as regras de preenchimento MERAKI-AP
                     # Incluso no mesmo os dados variaveis IP GERENCIA & customPerformanceClassId
                         corpo = {
                             "activeActiveAutoVpnEnabled": True,
                             "defaultUplink": "wan2",
                             "loadBalancingEnabled": True,
                             "wanTrafficUplinkPreferences": [
                                 {
                                     "trafficFilters": [
                                         {
                                             "type": "custom",
                                             "value": {
                                                 "protocol": "any",
                                                 "source": {
                                                     "cidr": str(pcGerencia)
                                                 },
                                                 "destination": {
                                                     "cidr": "any"
                                                 }
                                             }
                                         }
                                     ],
                                     "preferredUplink": "wan2"
                                 },
                                 {
                                     "trafficFilters": [
                                         {
                                             "type": "custom",
                                             "value": {
                                                 "protocol": "any",
                                                 "source": {
                                                     "cidr": "any"
                                                 },
                                                 "destination": {
                                                     "cidr": "any"
                                                 }
                                             }
                                         }
                                     ],
                                     "preferredUplink": "wan1"
                                 }
                             ],
                             "vpnTrafficUplinkPreferences": [
                                 {
                                     "trafficFilters": [
                                         {
                                             "type": "custom",
                                             "value": {
                                                 "protocol": "any",
                                                 "source": {
                                                     "cidr": "any"
                                                 },
                                                 "destination": {
                                                     "cidr": str(pcGerencia)
                                                 }
                                             }
                                         }
                                     ],
                                     "preferredUplink": "wan2",
                                     "failOverCriterion": "poorPerformance",
                                     "performanceClass": {
                                         "type": "custom",
                                         "customPerformanceClassId": str(performaceList["customPerformanceClassId"])
                                     }
                                 },
                                 {
                                     "trafficFilters": [
                                         {
                                             "type": "custom",
                                             "value": {
                                                 "protocol": "any",
                                                 "source": {
                                                     "cidr": "any"
                                                 },
                                                 "destination": {
                                                     "cidr": "10.0.0.0/8"
                                                 }
                                             }
                                         }
                                     ],
                                     "preferredUplink": "wan2",
                                     "failOverCriterion": "poorPerformance",
                                     "performanceClass": {
                                         "type": "custom",
                                         "customPerformanceClassId": str(performaceList["customPerformanceClassId"])
                                     }
                                 },
                                 {
                                     "trafficFilters": [
                                         {
                                             "type": "custom",
                                             "value": {
                                                 "protocol": "any",
                                                 "source": {
                                                     "cidr": "any"
                                                 },
                                                 "destination": {
                                                     "cidr": "172.16.0.0/12"
                                                 }
                                             }
                                         }
                                     ],
                                     "preferredUplink": "wan2",
                                     "failOverCriterion": "poorPerformance",
                                     "performanceClass": {
                                         "type": "custom",
                                         "customPerformanceClassId": str(performaceList["customPerformanceClassId"])
                                     }
                                 },
                                 {
                                     "trafficFilters": [
                                         {
                                             "type": "custom",
                                             "value": {
                                                 "protocol": "any",
                                                 "source": {
                                                     "cidr": "any"
                                                 },
                                                 "destination": {
                                                     "cidr": "158.228.132.214/32"
                                                 }
                                             }
                                         },
                                         {
                                             "type": "custom",
                                             "value": {
                                                 "protocol": "any",
                                                 "source": {
                                                     "cidr": "any"
                                                 },
                                                 "destination": {
                                                     "cidr": "192.175.52.134/32"
                                                 }
                                             }
                                         },
                                         {
                                             "type": "custom",
                                             "value": {
                                                 "protocol": "any",
                                                 "source": {
                                                     "cidr": "any"
                                                 },
                                                 "destination": {
                                                     "cidr": "104.40.26.199/32"
                                                 }
                                             }
                                         },
                                         {
                                             "type": "custom",
                                             "value": {
                                                 "protocol": "any",
                                                 "source": {
                                                     "cidr": "any"
                                                 },
                                                 "destination": {
                                                     "cidr": "51.143.102.21/32"
                                                 }
                                             }
                                         },
                                         {
                                             "type": "custom",
                                             "value": {
                                                 "protocol": "any",
                                                 "source": {
                                                     "cidr": "any"
                                                 },
                                                 "destination": {
                                                     "cidr": "192.168.0.0/16"
                                                 }
                                             }
                                         },
                                         {
                                             "type": "custom",
                                             "value": {
                                                 "protocol": "any",
                                                 "source": {
                                                     "cidr": "any"
                                                 },
                                                 "destination": {
                                                     "cidr": "3.95.46.64/32"
                                                 }
                                             }
                                         },
                                         {
                                             "type": "custom",
                                             "value": {
                                                 "protocol": "any",
                                                 "source": {
                                                     "cidr": "any"
                                                 },
                                                 "destination": {
                                                     "cidr": "142.11.160.0/21"
                                                 }
                                             }
                                         }
                                     ],
                                     "preferredUplink": "wan2",
                                     "failOverCriterion": "poorPerformance",
                                     "performanceClass": {
                                         "type": "custom",
                                         "customPerformanceClassId": str(performaceList["customPerformanceClassId"])
                                     }
                                 }
                             ]
                         }

                 except:
                     # Caso a base não tenha dados ou gere algum tipo de erro na busca do ID.
                     print("BASE SEM DADOS OU ERRO IMPREVISTO ENCONTRADO")
                 # Convertendo as informações armazenadas para JSON
                 corpoJson = json.dumps(corpo)
                 # URL para PUT no UPLINKSELECTION, caso necessário, mudar para config desejada
                 # Update URL = URL MERAKI API + CONFIG DESEJADA + NETWORK ID
                 updateUrl = mainUrl + "/networks/{}/appliance/trafficShaping/uplinkSelection".format(netId)
                 # Armazenando resultado do PUT, onde caso retorno seja 200, o mesmo funcionou.
                 responseUpdate = requests.put(url=updateUrl, headers=headersPUT, data=corpoJson)
                 # Mostrando resultado do armazenamento ( Apenas para controle )
                 if responseUpdate.status_code == 200: print ("TrafficShapping atualizada com sucesso!")
                 else:print("Houve um problema em seu PUT, favor verificar o método requisitado e suas variaveis !!")
            # Caso ocorra um erro de processamento em metodos GET ou erro de armazenamento do PUT;
            # O mesmo exibe a seguinte mensagem
            except:
                print("Ocorreu algum erro em seu GET ou PUT. Metodo canelado para a Network: \t " + netName)
