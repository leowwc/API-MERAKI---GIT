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

# Requisitando todas as networks na organização
responseNet = requests.get(url=netIdUrl, headers=headers)
responseNetJson = json.loads(responseNet.content)

# Variaveis de controle para execução do script
nomes = "MCD_AAC_REST","MCD_ACM_REST","MCD_AFP_REST","MCD_APD_REST","MCD_ASS_REST","MCD_B40_REST","MCD_BBH_REST","MCD_BUR_REST","MCD_BVE_REST","MCD_CAS_REST","MCD_CDE_REST","MCD_CMV_REST","MCD_DIA_REST","MCD_DRE_REST","MCD_AAE_REST","MCD_AAH_REST","MCD_ABA_REST","MCD_ABC_REST","MCD_ABM_REST","MCD_ABR_REST","MCD_ACC_REST","MCD_ACL_REST","MCD_AE2_REST","MCD_AEM_REST","MCD_AFD_REST","MCD_AFM_REST","MCD_AFO_REST","MCD_AFT_REST","MCD_AGA_REST","MCD_AGT_REST","MCD_AIA_REST"


vlans_id = 20,60,80

# Procurando a network cujo está na variavel nomes
for listNetwork in responseNetJson:
    # Variavel para controlar a quantidade de group polices e ID
    id_gp = 0

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

            for listaTeste in gPolcesJson:
                if listaTeste['name'] == 'ACL_VLANs_20_60_80':
                    id_gp = listaTeste['groupPolicyId']


            corpoGrupo = {
                "groupPolicyId": str(id_gp)
            }
            print(id_gp)

            # Faz uma tentativa, onde caso ocorra um erro, é efetuado o tratamento na captura
            try:
                # Armazena a URL para buscar todas as VLANs da network irformada ( variavel netId )
                vlanUrl = mainUrl + "/networks/{}/appliance/vlans".format(netId)

                # Armazena o resultado da requisição GET
                responseVlans = requests.get(url=vlanUrl, headers=headers)

                # Converte os dados em json para leitura
                vlanJson = json.loads(responseVlans.content)

                # Compacta a variavial em json
                corpoJson = json.dumps(corpoGrupo)

                # Percorre todas vlans no objeto vlanJson
                for listVlan in vlanJson:
                        if listVlan["id"] in vlans_id:

                            # Armazena a URL para efetuar o UPDATE da VLAN atuante do momento
                            updateUrl = mainUrl + "/networks/{}/appliance/vlans/{}".format(netId, listVlan["id"])

                            # Invocamos o metodo de requisição PUT para enviar os dados a API
                            responseUpdate = requests.put(url=updateUrl, headers=headers, data=corpoJson)

                            # Caso o método tenha sucesso, ele é armazenado na variavel responseUpdate com o valor = 200
                            if responseUpdate.status_code == 200:
                                print("VLAN " + str(listVlan["id"]) + " atualizada com sucesso!")
                            else:
                                print("Falha ao atualizar a VLAN")
                                print(responseUpdate.status_code)
            except:
                # Caso a base não tenha dados ou gere algum tipo de erro na busca.
                print("Erro ao buscar as VLAN's")
