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
#Headers necessários para os métodos GET e PUT
headers = {
    'Content-Type': 'application/json',
    'X-Cisco-Meraki-API-Key': 'd15e75a6f1578e190bcdf2c8e6eb9524d75dfd23'

}
# Requisitando todas as networks na organização
responseNet = requests.get(url=netIdUrl, headers=headers)
responseNetJson = json.loads(responseNet.content)

# Network's onde será incluso as novas configurações.
# Caso necessário efetuar alteração para busca em arquivo.
nomes = "MCD_PAM_REST","MCD_PGS_REST","MCD_PHI_REST","MCD_MIR_REST","MCD_GVD_REST","MCD_PIC_REST","MCD_CAD_REST","MCD_LOB_REST","MCD_JPM_REST","MCD_PKE_REST","MCD_SJO_REST","MCD_SSJ_REST","MCD_LEO_REST"

# Procurando a network cujo está na variavel nomes
for listNetwork in responseNetJson:

    #if listNetwork["name"] in nomes:
        tamanho = len(listNetwork["name"])
#       netId = listNetwork["id"]
#       print("Network a ser Modificada \t Nome: {}, Network_ID: {} ".format(netName,listNetwork["id"]))
        if tamanho == 12:
            try:
                splashURL = mainUrl + "/networks/{}/wireless/ssids/0/splash/settings".format(listNetwork["id"])
                responseSplash = requests.get(url=splashURL, headers=headers)
                SplashJson = json.loads(responseSplash.content)
                #print(SplashJson)
                if SplashJson["splashMethod"] == "None":
                    print("SPLASH PAGE DESATIVADA" + "\t" + listNetwork["name"] + "\t" +listNetwork["id"])
                else:
                    if SplashJson["useSplashUrl"] == True :
                        print( "SIM" + "\t" +listNetwork["name"] +"\t"+ listNetwork["id"] +"\t"+ SplashJson["splashUrl"])
                    else:
                        print("NÃO" + "\t" + listNetwork["name"] +"\t"+ listNetwork["id"])

                #tofile = []
                #with open("SplashPage" + ".json", "a") as f:
                    #for vlans in responseVlansJson:
                        #vlanId = str(vlans['id'])
                        #tofile.append({
                          #  "id": vlanId,
                          #  "name": vlans['name'],
                          #  "subnet": vlans['subnet'],
                          #  "applianceIp": vlans['applianceIp']
                        #})
                    #json.dump(tofile, f, indent=4, ensure_ascii=False)
                #f.close()
                #print("Arquivo salvo com sucesso!")
            except:
                print("Não temos SplashPage para a network:" + listNetwork["name"])