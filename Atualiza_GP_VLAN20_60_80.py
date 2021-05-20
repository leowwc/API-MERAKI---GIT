import requests
import json


# Meraki URL API - URL Base de comunicação via API
mainUrl = "https://api.meraki.com/api/v1"
# OrganizationId da ARCOS DOURADOS BR
orgId = "635570497412663072"
# API-KEY - Esta API é de uso individual, onde cada usuário deve registrar a sua
apiKey = "'X-Cisco-Meraki-API-Key': 'd15e75a6f1578e190bcdf2c8e6eb9524d75dfd23'"
# URL para GET, onde busca todas as Networks na organização
netIdUrl = mainUrl + "/organizations/{}/networks?perPage=100000".format(orgId)
# Criando os headers - Todo cabeçalho deve seguir de acordo com o proposto pela Meraki-API
# Headers necessários apenas para os métodos GET

# Headers necessários para os métodos PUT
headers = {
    'Content-Type': 'application/json',
    'X-Cisco-Meraki-API-Key': 'd15e75a6f1578e190bcdf2c8e6eb9524d75dfd23'

}
# Requisitando todas as networks na organização
responseNet = requests.get(url=netIdUrl, headers=headers)
responseNetJson = json.loads(responseNet.content)

x_y = ""

nomes = 'MCD_RVE_REST'

# Procurando a network cujo está na variavel nomes
for listNetwork in responseNetJson:

    if listNetwork["name"] in nomes:

            # Armazena o nome da network
            netName = listNetwork["name"]

            # Armazena o id da network
            netId = listNetwork["id"]

            # Exibe as informações da network para controle
            print("Network a ser Modificada \t Nome: {}, Network_ID: {} ".format(netName, netId))

            # URL para resgatar as Group Policies já existentes
            gpGetURL = mainUrl + "/networks/{}/groupPolicies".format(netId)

            # Armazena as group polices
            gPolices = requests.get(url=gpGetURL, headers=headers)

            # Carrega o conteudo em json
            gPolcesJson = json.loads(gPolices.content)

            #vlanUrl = mainUrl + "/networks/{}/appliance/vlans/60".format(netId)
            #responseVlans = requests.get(url=vlanUrl, headers=headers)
            #vlan10Json = json.loads(responseVlans.content)
            #pcGerencia = vlan10Json["applianceIp"]
            # Após pegar o IP do MX na vlan 10 com final .14, é substituido o mesmo para final .1
            # Desta forma podemos efetuar a mudança para o IP desejado, que é o PC GERENCIA.
            # Primeiro separamos os 4 octetos do IP retirado
            #parte = pcGerencia.split('.')
            #print(parte[1] + "." + parte[2])
            #x_y = parte[1] + "." + parte[2]
            #str(x_y)
            ACL_VLAN_20_60_80 = {
        "groupPolicyId": "103",
        "name": "ACL_VLANs_20_60_80",
        "scheduling": {
            "enabled": False,
            "monday": {
                "active": True,
                "from": "00:00",
                "to": "24:00"
            },
            "tuesday": {
                "active": True,
                "from": "00:00",
                "to": "24:00"
            },
            "wednesday": {
                "active": True,
                "from": "00:00",
                "to": "24:00"
            },
            "thursday": {
                "active": True,
                "from": "00:00",
                "to": "24:00"
            },
            "friday": {
                "active": True,
                "from": "00:00",
                "to": "24:00"
            },
            "saturday": {
                "active": True,
                "from": "00:00",
                "to": "24:00"
            },
            "sunday": {
                "active": True,
                "from": "00:00",
                "to": "24:00"
            }
        },
        "bandwidth": {
            "settings": "network default",
            "bandwidthLimits": {
                "limitUp": None,
                "limitDown": None
            }
        },
        "firewallAndTrafficShaping": {
            "settings": "custom",
            "trafficShapingRules": [],
            "l3FirewallRules": [
                {
                    "comment": "Block Cameras_Seg",
                    "policy": "deny",
                    "protocol": "any",
                    "destPort": "Any",
                    "destCidr": "192.168.92.0/29"
                },
                {
                    "comment": "Block Wifi Free",
                    "policy": "deny",
                    "protocol": "any",
                    "destPort": "Any",
                    "destCidr": "192.168.0.0/24"
                },
                {
                    "comment": "Tango",
                    "policy": "allow",
                    "protocol": "tcp",
                    "destPort": "7778",
                    "destCidr": "192.168.21.37/32"
                },
                {
                    "comment": "Datacenter",
                    "policy": "allow",
                    "protocol": "any",
                    "destPort": "Any",
                    "destCidr": "10.195.0.0/8"
                },
                {
                    "comment": "Datacenter",
                    "policy": "allow",
                    "protocol": "any",
                    "destPort": "Any",
                    "destCidr": "172.16.0.0/12"
                },
                {
                    "comment": "License Microsoft",
                    "policy": "allow",
                    "protocol": "any",
                    "destPort": "Any",
                    "destCidr": "142.11.161.84/32"
                },
                {
                    "comment": "License Microsoft",
                    "policy": "allow",
                    "protocol": "any",
                    "destPort": "Any",
                    "destCidr": "142.11.161.110/32"
                },
                {
                    "comment": "License Microsoft",
                    "policy": "allow",
                    "protocol": "any",
                    "destPort": "Any",
                    "destCidr": "142.11.163.171/32"
                },
                {
                    "comment": "License Microsoft",
                    "policy": "allow",
                    "protocol": "any",
                    "destPort": "Any",
                    "destCidr": "142.11.163.173/32"
                },
                {
                    "comment": "License Microsoft",
                    "policy": "allow",
                    "protocol": "any",
                    "destPort": "Any",
                    "destCidr": "10.195.42.46/32"
                },
                {
                    "comment": "Sefaz CE",
                    "policy": "allow",
                    "protocol": "tcp",
                    "destPort": "443",
                    "destCidr": "191.232.176.16/32"
                },
                {
                    "comment": "Sefaz CE",
                    "policy": "allow",
                    "protocol": "tcp",
                    "destPort": "443",
                    "destCidr": "191.232.216.52/32"
                },
                {
                    "comment": "Sefaz NTP",
                    "policy": "allow",
                    "protocol": "udp",
                    "destPort": "123",
                    "destCidr": "200.144.121.33/32"
                },
                {
                    "comment": "Sefaz NTP",
                    "policy": "allow",
                    "protocol": "udp",
                    "destPort": "123",
                    "destCidr": "200.160.0.8/32"
                },
                {
                    "comment": "NP6 Multicast",
                    "policy": "allow",
                    "protocol": "any",
                    "destPort": "Any",
                    "destCidr": "233.0.0.176/32"
                },
                {
                    "comment": "NP6 Multicast",
                    "policy": "allow",
                    "protocol": "any",
                    "destPort": "Any",
                    "destCidr": "239.255.255.250/32"
                },
                {
                    "comment": "Restaurantes e Kiosks",
                    "policy": "allow",
                    "protocol": "any",
                    "destPort": "Any",
                    "destCidr": "10.100.0.0/16"
                },
                {
                    "comment": "Restaurantes e Kiosks",
                    "policy": "allow",
                    "protocol": "any",
                    "destPort": "Any",
                    "destCidr": "10.101.0.0/16"
                },
                {
                    "comment": "Restaurantes e Kiosks",
                    "policy": "allow",
                    "protocol": "any",
                    "destPort": "Any",
                    "destCidr": "10.102.0.0/16"
                },
                {
                    "comment": "Restaurantes e Kiosks",
                    "policy": "allow",
                    "protocol": "any",
                    "destPort": "Any",
                    "destCidr": "10.194.0.0/16"
                },
                {
                    "comment": "Restaurantes e Kiosks",
                    "policy": "allow",
                    "protocol": "any",
                    "destPort": "Any",
                    "destCidr": "10.51.0.0/16"
                },
                {
                    "comment": "Cisco DNS",
                    "policy": "allow",
                    "protocol": "any",
                    "destPort": "Any",
                    "destCidr": "208.67.222.222/32"
                },
                {
                    "comment": "Cisco DNS",
                    "policy": "allow",
                    "protocol": "any",
                    "destPort": "Any",
                    "destCidr": "208.67.220.220/32"
                },
                {
                    "comment": "SCCM-Azure",
                    "policy": "allow",
                    "protocol": "any",
                    "destPort": "Any",
                    "destCidr": "152.140.0.0/16"
                },
                {
                    "comment": "SCCM-Azure",
                    "policy": "allow",
                    "protocol": "any",
                    "destPort": "Any",
                    "destCidr": "152.142.0.0/16"
                },
                {
                    "comment": "DNS para Meraki Cloud",
                    "policy": "allow",
                    "protocol": "udp",
                    "destPort": "53",
                    "destCidr": "8.8.8.8/32"
                },
                {
                    "comment": "Meraki Cloud",
                    "policy": "allow",
                    "protocol": "any",
                    "destPort": "Any",
                    "destCidr": "35.161.241.24/32"
                },
                {
                    "comment": "Meraki Cloud",
                    "policy": "allow",
                    "protocol": "any",
                    "destPort": "Any",
                    "destCidr": "35.162.58.56/32"
                },
                {
                    "comment": "Meraki Cloud",
                    "policy": "allow",
                    "protocol": "any",
                    "destPort": "Any",
                    "destCidr": "35.162.58.76/32"
                },
                {
                    "comment": "Meraki Cloud",
                    "policy": "allow",
                    "protocol": "any",
                    "destPort": "Any",
                    "destCidr": "52.33.92.73/32"
                },
                {
                    "comment": "Meraki Cloud",
                    "policy": "allow",
                    "protocol": "any",
                    "destPort": "Any",
                    "destCidr": "52.39.236.233/32"
                },
                {
                    "comment": "Meraki Cloud",
                    "policy": "allow",
                    "protocol": "any",
                    "destPort": "Any",
                    "destCidr": "52.208.175.132/32"
                },
                {
                    "comment": "Meraki Cloud",
                    "policy": "allow",
                    "protocol": "any",
                    "destPort": "Any",
                    "destCidr": "64.62.142.2/32"
                },
                {
                    "comment": "Meraki Cloud",
                    "policy": "allow",
                    "protocol": "any",
                    "destPort": "Any",
                    "destCidr": "64.62.142.12/32"
                },
                {
                    "comment": "Meraki Cloud",
                    "policy": "allow",
                    "protocol": "any",
                    "destPort": "Any",
                    "destCidr": "64.165.192.245/32"
                },
                {
                    "comment": "Meraki Cloud",
                    "policy": "allow",
                    "protocol": "any",
                    "destPort": "Any",
                    "destCidr": "108.161.147.0/24"
                },
                {
                    "comment": "Meraki Cloud",
                    "policy": "allow",
                    "protocol": "any",
                    "destPort": "Any",
                    "destCidr": "199.231.78.0/24"
                },
                {
                    "comment": "Meraki Cloud",
                    "policy": "allow",
                    "protocol": "any",
                    "destPort": "Any",
                    "destCidr": "209.206.48.0/24"
                },
                {
                    "comment": "Meraki Cloud",
                    "policy": "allow",
                    "protocol": "any",
                    "destPort": "Any",
                    "destCidr": "3.210.175.34/32"
                },
                {
                    "comment": "Meraki Cloud",
                    "policy": "allow",
                    "protocol": "any",
                    "destPort": "Any",
                    "destCidr": "13.52.29.190/32"
                },
                {
                    "comment": "Meraki Cloud",
                    "policy": "allow",
                    "protocol": "any",
                    "destPort": "Any",
                    "destCidr": "13.54.51.60/32"
                },
                {
                    "comment": "Meraki Cloud",
                    "policy": "allow",
                    "protocol": "any",
                    "destPort": "Any",
                    "destCidr": "17.0.0.0/8"
                },
                {
                    "comment": "Meraki Cloud",
                    "policy": "allow",
                    "protocol": "any",
                    "destPort": "Any",
                    "destCidr": "50.18.100.0/32"
                },
                {
                    "comment": "Meraki Cloud",
                    "policy": "allow",
                    "protocol": "any",
                    "destPort": "Any",
                    "destCidr": "52.57.34.238/32"
                },
                {
                    "comment": "Meraki Cloud",
                    "policy": "allow",
                    "protocol": "any",
                    "destPort": "Any",
                    "destCidr": "52.59.68.120/32"
                },
                {
                    "comment": "Meraki Cloud",
                    "policy": "allow",
                    "protocol": "any",
                    "destPort": "Any",
                    "destCidr": "52.84.77.0/24"
                },
                {
                    "comment": "Meraki Cloud",
                    "policy": "allow",
                    "protocol": "any",
                    "destPort": "Any",
                    "destCidr": "198.27.154.12/32"
                },
                {
                    "comment": "Meraki Cloud",
                    "policy": "allow",
                    "protocol": "any",
                    "destPort": "Any",
                    "destCidr": "198.27.154.14/32"
                },
                {
                    "comment": "Meraki Cloud",
                    "policy": "allow",
                    "protocol": "any",
                    "destPort": "Any",
                    "destCidr": "199.231.78.0/24"
                },
                {
                    "comment": "Meraki Cloud",
                    "policy": "allow",
                    "protocol": "any",
                    "destPort": "Any",
                    "destCidr": "209.206.51.87/32"
                },
                {
                    "comment": "Meraki Cloud",
                    "policy": "allow",
                    "protocol": "any",
                    "destPort": "Any",
                    "destCidr": "209.206.52.0/24"
                },
                {
                    "comment": "Meraki Cloud",
                    "policy": "allow",
                    "protocol": "any",
                    "destPort": "Any",
                    "destCidr": "209.206.53.89/32"
                },
                {
                    "comment": "Meraki Cloud",
                    "policy": "allow",
                    "protocol": "any",
                    "destPort": "Any",
                    "destCidr": "209.206.55.0/24"
                },
                {
                    "comment": "ICMP",
                    "policy": "allow",
                    "protocol": "icmp",
                    "destPort": "Any",
                    "destCidr": "Any"
                },
                {
                    "comment": "Bloqueia Restante",
                    "policy": "deny",
                    "protocol": "tcp",
                    "destPort": "Any",
                    "destCidr": "Any"
                }
            ],
            "l7FirewallRules": []
        },
        "contentFiltering": {
            "allowedUrlPatterns": {
                "settings": "network default",
                "patterns": []
            },
            "blockedUrlPatterns": {
                "settings": "network default",
                "patterns": []
            },
            "blockedUrlCategories": {
                "settings": "network default",
                "categories": []
            }
        },
        "splashAuthSettings": "network default",
        "vlanTagging": {
            "settings": "network default"
        },
        "bonjourForwarding": {
            "settings": "network default",
            "rules": []
        }
    }

            corpo_RegraJson = json.dumps(ACL_VLAN_20_60_80)

            for listaTeste in gPolcesJson:
                #print(listaTeste)
                if listaTeste['name'] == 'ACL_VLANs_20_60_80':
                    updatePoliceURL = mainUrl + "/networks/{}/groupPolicies/{}".format(netId,listaTeste['groupPolicyId'])
                    responseUpdate = requests.put(url=updatePoliceURL, headers=headers, data=corpo_RegraJson)
                    # Caso o método tenha sucesso, ele é armazenado na variavel responseUpdate com o valor = 200/201
                    if responseUpdate.status_code == 200:
                        print("Atualizada Regra de ACL_VLANs_20_60_80!!")
                        #print("\n")
                    else:
                        print("Falha ao atualizar ")
                        print(responseUpdate.status_code)
                        print(responseUpdate.url)
                        print(responseUpdate.headers)





