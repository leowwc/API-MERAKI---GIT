import requests
import json

# Meraki URL API - URL Base de comunicação via API
mainUrl = "https://api.meraki.com/api/v1"

# OrganizationId da ARCOS DOURADOS BR
orgId = "635570497412663072"

# API-KEY - Esta API é de uso individual, onde cada usuário deve registrar a sua
apiKey = "'X-Cisco-Meraki-API-Key': 'd15e75a6f1578e190bcdf2c8e6eb9524d75dfd23'"

# Headers necessários para os métodos
headers = {
    'Content-Type': 'application/json',
    'X-Cisco-Meraki-API-Key': 'd15e75a6f1578e190bcdf2c8e6eb9524d75dfd23'
}

# URL para GET, onde busca todas as Networks na organização
netIdUrl = mainUrl + "/organizations/{}/networks?perPage=100000".format(orgId)

# Nome da regra a ser criada
nome_Regra = "Correção_MCD_CORP"

# Corpo da regra nova ser incluida
corpo_Regra = {
        "groupPolicyId": "105",
        "name": nome_Regra,
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
                    "comment": "",
                    "policy": "deny",
                    "protocol": "any",
                    "destPort": "Any",
                    "destCidr": "193.29.63.203/32"
                },
                {
                    "comment": "",
                    "policy": "deny",
                    "protocol": "any",
                    "destPort": "Any",
                    "destCidr": "37.120.222.100/32"
                },
                {
                    "comment": "",
                    "policy": "deny",
                    "protocol": "any",
                    "destPort": "Any",
                    "destCidr": "138.68.142.174/32"
                },
                {
                    "comment": "",
                    "policy": "deny",
                    "protocol": "any",
                    "destPort": "Any",
                    "destCidr": "178.128.231.241/32"
                },
                {
                    "comment": "",
                    "policy": "deny",
                    "protocol": "any",
                    "destPort": "Any",
                    "destCidr": "46.101.1.135/32"
                },
                {
                    "comment": "",
                    "policy": "deny",
                    "protocol": "any",
                    "destPort": "Any",
                    "destCidr": "99.86.154.138/32"
                },
                {
                    "comment": "",
                    "policy": "deny",
                    "protocol": "any",
                    "destPort": "Any",
                    "destCidr": "99.86.154.183/32"
                },
                {
                    "comment": "",
                    "policy": "deny",
                    "protocol": "any",
                    "destPort": "Any",
                    "destCidr": "142.202.205.130/32"
                },
                {
                    "comment": "",
                    "policy": "deny",
                    "protocol": "any",
                    "destPort": "Any",
                    "destCidr": "198.199.80.185/32"
                },
                {
                    "comment": "",
                    "policy": "deny",
                    "protocol": "any",
                    "destPort": "Any",
                    "destCidr": "185.197.30.195/32"
                },
                {
                    "comment": "",
                    "policy": "deny",
                    "protocol": "any",
                    "destPort": "Any",
                    "destCidr": "54.38.220.85/32"
                },
                {
                    "comment": "",
                    "policy": "deny",
                    "protocol": "any",
                    "destPort": "Any",
                    "destCidr": "31.220.4.74/32"
                },
                {
                    "comment": "",
                    "policy": "deny",
                    "protocol": "any",
                    "destPort": "Any",
                    "destCidr": "185.213.26.29/32"
                },
                {
                    "comment": "",
                    "policy": "deny",
                    "protocol": "any",
                    "destPort": "Any",
                    "destCidr": "64.69.218.112/32"
                },
                {
                    "comment": "",
                    "policy": "deny",
                    "protocol": "any",
                    "destPort": "Any",
                    "destCidr": "97.90.217.63/32"
                },
                {
                    "comment": "",
                    "policy": "deny",
                    "protocol": "any",
                    "destPort": "Any",
                    "destCidr": "64.69.218.104/32"
                },
                {
                    "comment": "",
                    "policy": "deny",
                    "protocol": "any",
                    "destPort": "Any",
                    "destCidr": "70.127.183.9/32"
                }
            ],
            "l7FirewallRules": [
                {
                    "policy": "deny",
                    "type": "host",
                    "value": "nextendpoint.xyz"
                },
                {
                    "policy": "deny",
                    "type": "host",
                    "value": "d2ji0hgex1ho8p.cloudfront.net"
                },
                {
                    "policy": "deny",
                    "type": "host",
                    "value": "arnolddraft.com"
                },
                {
                    "policy": "deny",
                    "type": "host",
                    "value": "choosebudget.com"
                },
                {
                    "policy": "deny",
                    "type": "host",
                    "value": "d23gzt9pw4yryc.cloudfront.net"
                },
                {
                    "policy": "deny",
                    "type": "host",
                    "value": "digitalsecures.xyz"
                },
                {
                    "policy": "deny",
                    "type": "host",
                    "value": "aloogi.com"
                },
                {
                    "policy": "deny",
                    "type": "host",
                    "value": "digitalstockes.xyz"
                },
                {
                    "policy": "deny",
                    "type": "host",
                    "value": "pjylbc.com"
                },
                {
                    "policy": "deny",
                    "type": "host",
                    "value": "dnsmaker.xyz"
                },
                {
                    "policy": "deny",
                    "type": "host",
                    "value": "withupdates.xyz"
                },
                {
                    "policy": "deny",
                    "type": "host",
                    "value": "windowww.xyz"
                },
                {
                    "policy": "deny",
                    "type": "host",
                    "value": "domainstrusts.xyz"
                },
                {
                    "policy": "deny",
                    "type": "host",
                    "value": "d21kx8ntwu4lt5.cloudfront.net"
                },
                {
                    "policy": "deny",
                    "type": "host",
                    "value": "d2idxs80daj9st.cloudfront.net"
                },
                {
                    "policy": "deny",
                    "type": "host",
                    "value": "dc7adsm6tl3s3.cloudfront.net"
                },
                {
                    "policy": "deny",
                    "type": "host",
                    "value": "blaskjar.xyz"
                },
                {
                    "policy": "deny",
                    "type": "host",
                    "value": "transformedposition.xyz"
                },
                {
                    "policy": "deny",
                    "type": "host",
                    "value": "maddys.xyz"
                },
                {
                    "policy": "deny",
                    "type": "host",
                    "value": "logmein.com"
                },
                {
                    "policy": "deny",
                    "type": "host",
                    "value": "vpn.net"
                }
            ]
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

# Corpo da regra WiFi Free a ser atualizada
att_WiFi_Free = {
                   "groupPolicyId": "100",
                   "name": "Filtro de conteúdo - Wifi - Free",
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
                       "trafficShapingRules": [
                           {
                               "definitions": [
                                   {
                                       "type": "applicationCategory",
                                       "value": {
                                           "id": "meraki:layer7/category/3",
                                           "name": "File sharing"

                                       }
                                   },
                                   {
                                       "type": "applicationCategory",
                                       "value": {
                                           "id": "meraki:layer7/category/8",
                                           "name": "Peer-to-peer (P2P)"
                                       }
                                   },
                                   {
                                       "type": "applicationCategory",
                                       "value": {
                                           "id": "meraki:layer7/category/13",
                                           "name": "Video & music"
                                       }
                                   }
                               ],
                               "perClientBandwidthLimits": {
                                   "settings": "network default"
                               },
                               "dscpTagValue": 10,
                               "pcpTagValue": 0
                           }
                       ],
                       "l3FirewallRules": [
                           {
                               "comment": "",
                               "policy": "deny",
                               "protocol": "any",
                               "destPort": "Any",
                               "destCidr": "193.29.63.203/32"
                           },
                           {
                               "comment": "",
                               "policy": "deny",
                               "protocol": "any",
                               "destPort": "Any",
                               "destCidr": "37.120.222.100/32"
                           },
                           {
                               "comment": "",
                               "policy": "deny",
                               "protocol": "any",
                               "destPort": "Any",
                               "destCidr": "138.68.142.174/32"
                           },
                           {
                               "comment": "",
                               "policy": "deny",
                               "protocol": "any",
                               "destPort": "Any",
                               "destCidr": "178.128.231.241/32"
                           },
                           {
                               "comment": "",
                               "policy": "deny",
                               "protocol": "any",
                               "destPort": "Any",
                               "destCidr": "46.101.1.135/32"
                           },
                           {
                               "comment": "",
                               "policy": "deny",
                               "protocol": "any",
                               "destPort": "Any",
                               "destCidr": "99.86.154.138/32"
                           },
                           {
                               "comment": "",
                               "policy": "deny",
                               "protocol": "any",
                               "destPort": "Any",
                               "destCidr": "99.86.154.183/32"
                           },
                           {
                               "comment": "",
                               "policy": "deny",
                               "protocol": "any",
                               "destPort": "Any",
                               "destCidr": "142.202.205.130/32"
                           },
                           {
                               "comment": "",
                               "policy": "deny",
                               "protocol": "any",
                               "destPort": "Any",
                               "destCidr": "198.199.80.185/32"
                           },
                           {
                               "comment": "",
                               "policy": "deny",
                               "protocol": "any",
                               "destPort": "Any",
                               "destCidr": "185.197.30.195/32"
                           },
                           {
                               "comment": "",
                               "policy": "deny",
                               "protocol": "any",
                               "destPort": "Any",
                               "destCidr": "54.38.220.85/32"
                           },
                           {
                               "comment": "",
                               "policy": "deny",
                               "protocol": "any",
                               "destPort": "Any",
                               "destCidr": "31.220.4.74/32"
                           },
                           {
                               "comment": "",
                               "policy": "deny",
                               "protocol": "any",
                               "destPort": "Any",
                               "destCidr": "185.213.26.29/32"
                           },
                           {
                               "comment": "",
                               "policy": "deny",
                               "protocol": "any",
                               "destPort": "Any",
                               "destCidr": "64.69.218.112/32"
                           },
                           {
                               "comment": "",
                               "policy": "deny",
                               "protocol": "any",
                               "destPort": "Any",
                               "destCidr": "97.90.217.63/32"
                           },
                           {
                               "comment": "",
                               "policy": "deny",
                               "protocol": "any",
                               "destPort": "Any",
                               "destCidr": "64.69.218.104/32"
                           },
                           {
                               "comment": "",
                               "policy": "deny",
                               "protocol": "any",
                               "destPort": "Any",
                               "destCidr": "70.127.183.9/32"
                           }
                       ],
                       "l7FirewallRules": [
                           {
                               "policy": "deny",
                               "type": "host",
                               "value": "nextendpoint.xyz"
                           },
                           {
                               "policy": "deny",
                               "type": "host",
                               "value": "d2ji0hgex1ho8p.cloudfront.net"
                           },
                           {
                               "policy": "deny",
                               "type": "host",
                               "value": "arnolddraft.com"
                           },
                           {
                               "policy": "deny",
                               "type": "host",
                               "value": "choosebudget.com"
                           },
                           {
                               "policy": "deny",
                               "type": "host",
                               "value": "d23gzt9pw4yryc.cloudfront.net"
                           },
                           {
                               "policy": "deny",
                               "type": "host",
                               "value": "digitalsecures.xyz"
                           },
                           {
                               "policy": "deny",
                               "type": "host",
                               "value": "aloogi.com"
                           },
                           {
                               "policy": "deny",
                               "type": "host",
                               "value": "digitalstockes.xyz"
                           },
                           {
                               "policy": "deny",
                               "type": "host",
                               "value": "pjylbc.com"
                           },
                           {
                               "policy": "deny",
                               "type": "host",
                               "value": "dnsmaker.xyz"
                           },
                           {
                               "policy": "deny",
                               "type": "host",
                               "value": "withupdates.xyz"
                           },
                           {
                               "policy": "deny",
                               "type": "host",
                               "value": "windowww.xyz"
                           },
                           {
                               "policy": "deny",
                               "type": "host",
                               "value": "domainstrusts.xyz"
                           },
                           {
                               "policy": "deny",
                               "type": "host",
                               "value": "d21kx8ntwu4lt5.cloudfront.net"
                           },
                           {
                               "policy": "deny",
                               "type": "host",
                               "value": "d2idxs80daj9st.cloudfront.net"
                           },
                           {
                               "policy": "deny",
                               "type": "host",
                               "value": "dc7adsm6tl3s3.cloudfront.net"
                           },
                           {
                               "policy": "deny",
                               "type": "host",
                               "value": "blaskjar.xyz"
                           },
                           {
                               "policy": "deny",
                               "type": "host",
                               "value": "transformedposition.xyz"
                           },
                           {
                               "policy": "deny",
                               "type": "host",
                               "value": "maddys.xyz"
                           },
                           {
                               "policy": "deny",
                               "type": "host",
                               "value": "logmein.com"
                           },
                           {
                               "policy": "deny",
                               "type": "host",
                               "value": "vpn.net"
                           }
                       ]
                   },
                   "contentFiltering": {
                       "allowedUrlPatterns": {
                           "settings": "network default",
                           "patterns": []
                       },
                       "blockedUrlPatterns": {
                           "settings": "override",
                           "patterns": [
                               "bobs.com.br",
                               "habibs.com.br",
                               "burgerking.com.br",
                               "giraffas.com.br",
                               "kfcbrasil.com.br",
                               "subway.com",
                               "pizzahut.com.br",
                               "quartahut.com.br"
                           ]
                       },

                       "blockedUrlCategories": {
                           "settings": "override",
                           "categories": [
                               "meraki:contentFiltering/category/68",
                               "meraki:contentFiltering/category/10",
                               "meraki:contentFiltering/category/11",
                               "meraki:contentFiltering/category/76",
                               "meraki:contentFiltering/category/70",
                               "meraki:contentFiltering/category/33",
                               "meraki:contentFiltering/category/46",
                               "meraki:contentFiltering/category/64",
                               "meraki:contentFiltering/category/49",
                               "meraki:contentFiltering/category/56",
                               "meraki:contentFiltering/category/32",
                               "meraki:contentFiltering/category/62",
                               "meraki:contentFiltering/category/31",
                               "meraki:contentFiltering/category/57",
                               "meraki:contentFiltering/category/58",
                               "meraki:contentFiltering/category/71",
                               "meraki:contentFiltering/category/19",
                               "meraki:contentFiltering/category/59",
                               "meraki:contentFiltering/category/43",
                               "meraki:contentFiltering/category/72",
                               "meraki:contentFiltering/category/48"
                           ]
                       }
                   },
                   "splashAuthSettings": "network default",
                   "vlanTagging": {
                       "settings": "custom",
                       "vlanId": "50"
                   },
                   "bonjourForwarding": {
                       "settings": "network default",
                       "rules": []
                   }
               }

# Compacta as variaviaveis em json
corpo_RegraJson = json.dumps(corpo_Regra)
att_WiFi_FreeJson = json.dumps(att_WiFi_Free)

# Requisitando todas as networks na organização
responseNet = requests.get(url=netIdUrl, headers=headers)
responseNetJson = json.loads(responseNet.content)

# Variaveis de controle para execução do script
nomes = "MAM_TESTE_01"
vlans_id = 10,20,30,40,60,80,90,91

# Procurando a network cujo está na variavel nomes
for listNetwork in responseNetJson:
    # Variavel para controlar a quantidade de group polices e ID
    count = 100
    id_count = 0

    if listNetwork["name"] in nomes:
            # Armazena o nome da network
            netName = listNetwork["name"]

            # Armazena o id da network
            netId = listNetwork["id"]

            # Exibe as informações da network para controle
            print("\t")
            print("Network a ser Modificada \t Nome: {}, Network_ID: {} ".format(netName, netId))

            # URL para adicionar a nova regra de Group Policies
            gpPutURL = mainUrl + "/networks/{}/groupPolicies".format(netId)

            # URL para atualizar a regra atual WiFi Free
            updatePoliceURL = mainUrl + "/networks/{}/groupPolicies/100".format(netId)

            # URL para resgatar as Group Policies já existentes
            gpGetURL = mainUrl + "/networks/{}/groupPolicies".format(netId)

            # Armazena as group polices
            gPolices = requests.get(url=gpGetURL, headers=headers)

            # Carrega o conteudo em json
            gPolcesJson = json.loads(gPolices.content)

            # Invocamos o metodo de requisição PUT para atualizar o WiFi Free
            # Necessário primeiro efetuar o update da regra, depois acrescentar a nova, pois caso seja o contrário ocorre sobreposição
            responseUpdate = requests.put(url=updatePoliceURL, headers=headers, data=att_WiFi_FreeJson)

            # Caso o método tenha sucesso, ele é armazenado na variavel responseUpdate com o valor = 200/201
            if responseUpdate.status_code == 200 or 201:
                print("Filtro de conteúdo - Wifi - Free com sucesso!!")
                print("\n")
            else:
                print("Falha ao atualizar ")
                print(responseUpdate.status_code)
                print(responseUpdate.url)
                print(responseUpdate.headers)


            # Invocamos o metodo de requisição PUT para adicionar a regra de Group Police
            responseUpdate = requests.post(url=gpPutURL, headers=headers, data=corpo_RegraJson)

            # Caso o método tenha sucesso, ele é armazenado na variavel responseUpdate com o valor = 200/201
            if responseUpdate.status_code == 200 or 201:
                print("\n")
                print("Adicionado a regra " + nome_Regra + " com sucesso!")
                print("\n")
            else:
                print("Falha ao atualizar ")
                print(responseUpdate.status_code)
                print(responseUpdate.url)
                print(responseUpdate.headers)

            # Percorre a lista, contanto quantas group polices já existem, assim define o ID da nova a ser criada
            for listaTeste in gPolcesJson:
                count = count + 1

            # Atribui o valor a outra variável para poder ser convertida
            id_count = count

            # Compacta em json identado o resultado
            gPolcesJson = json.dumps(gPolcesJson, indent=True)

            # Abre um novo arquivo para salvar a VLAN
            with open('zgp_' + listNetwork["name"] + '_.json', 'w+') as file:
                # Armazena (ESCREVE) os dados da vlan no arquivo aberto
                file.write(gPolcesJson)
                print("\t Group Polices salvas com sucesso !!!!")

                    # Informação da groupPolicie a ser inserida na vlan
            corpoGrupo = {
                        "groupPolicyId": str(id_count)
                    }
            print(id_count)
            # Compacta a variavial em json
            corpoJson = json.dumps(corpoGrupo)

            # Faz uma tentativa, onde caso ocorra um erro, é efetuado o tratamento na captura
            try:
            # Armazena a URL para buscar todas as VLANs da network irformada ( variavel netId )
                vlanUrl = mainUrl + "/networks/{}/appliance/vlans".format(netId)

                # Armazena o resultado da requisição GET
                responseVlans = requests.get(url=vlanUrl, headers=headers)

                # Converte os dados em json para leitura
                vlanJson = json.loads(responseVlans.content)

                # Compacta a variavel vlanArquivo para o formato json, com identação organizada.
                # Info para print de controle
                # vlanArquivo = json.dumps(vlanJson, indent=True)

                # Percorre todas vlans no objeto vlanJson
                for listVlan in vlanJson:

                    # Compacta a variavel vlanArquivo para o formato json, com identação organizada.
                    vlanArquivo = json.dumps(vlanJson, indent=True)

                    # Abre um arquivo com o nome vlan_ Sigla _.json, onde caso exista outro igual, ele subscreve.
                    with open('vlan_' + listNetwork["name"] + '_.json', 'w+') as file:
                        # Armazena (ESCREVE) os dados da vlan no arquivo aberto
                        file.write(vlanArquivo)

                        print("Vlan {} salva com sucesso !!!!".format(listVlan["id"]))

                        if listVlan["id"] in vlans_id:

                        # Armazena a URL para efetuar o UPDATE da VLAN atuante do momento
                            updateUrl = mainUrl + "/networks/{}/appliance/vlans/{}".format(listVlan["networkId"], listVlan["id"])

                            # Invocamos o metodo de requisição PUT para enviar os dados a API
                            responseUpdate = requests.put(url=updateUrl, headers=headers, data=corpoJson)

                            # Caso o método tenha sucesso, ele é armazenado na variavel responseUpdate com o valor = 200
                            if responseUpdate.status_code == 200 or 201:
                                print("VLAN " + str(listVlan["id"]) + " atualizada com sucesso!")
                            else:
                                print("Falha ao atualizar a VLAN")
                                print(responseUpdate.status_code)
            except:
                    # Caso a base não tenha dados ou gere algum tipo de erro na busca.
                    print("Erro ao buscar as VLAN's")



