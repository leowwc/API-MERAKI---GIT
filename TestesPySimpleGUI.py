import PySimpleGUI as sg
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
user = "80737220"
str(user)

class getVlans:
    def __init__(self,nome):
        self.nome = nome

    def execGetVlans(self):
        # Requisitando todas as networks na organização
        responseNet = requests.get(url=netIdUrl, headers=headers)
        responseNetJson = json.loads(responseNet.content)

        # Armazena a network que deseja baixar as vlans
        nomes = self.nome
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
                print("Network cujo Vlans serão baixadas:")
                print("\n")
                print("Nome: {}".format(netName))
                print("Network ID: {} ".format(netId))
                print("\n")
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
                    print("Salvando Arquivo...")
                    print("\n")
                    with open('vlan_' + listNetwork["name"] + '_.json', 'w+') as file:
                        # Armazena (ESCREVE) os dados da vlan no arquivo aberto
                        file.write(vlanArquivo)
                    print("Vlans salvas com sucesso !!!!")
                except:
                    # Caso a base não tenha dados ou gere algum tipo de erro na busca.
                    print("Erro ao buscar as VLAN's")

class putVlans:
    def __init__(self,nome):
        self.nome = nome

    def execPutVlans(self):
        # Armazena a network que deseja baixar as vlans
        nomes = self.nome
        # Converte em String
        str(nomes)
        # Abre um arquivo salvo cujo o nome é vlan_ SIGLA _.json e lê todos os dados, sem possibilidade de editar
        with open("vlan_" + nomes + "_.json", "r") as file:
            # Armazeno todos os dados do arquivo em uma variavel
            vlanJson = file.read()
            # Carrego os dados armazenados no objeto em JSON
            vlanJson = json.loads(vlanJson)

            print("Lendo Arquivo.....")
            print("\n")
            print("\n")
            # Percorre as vlans contidas na variavel, onde cada linha é uma listVlan
            for listVlan in vlanJson:
                # Armazena a URL para efetuar o UPDATE da VLAN atuante do momento
                updateUrl = mainUrl + "/networks/{}/appliance/vlans/{}".format(listVlan["networkId"], listVlan["id"])
                # Adicionamos a vlan atuante em um objeto separado
                corpoListaVlan = listVlan
                # Compactamos o objeto em formato json
                corpoJson = json.dumps(corpoListaVlan)
                # Invocamos o metodo de requisição PUT para enviar os dados a API
                responseUpdate = requests.put(url=updateUrl, headers=headers, data=corpoJson)
                # Caso o método tenha sucesso, ele é armazenado na variavel responseUpdate com o valor = 200
                if responseUpdate.status_code == 200:
                    print("VLAN " + str(listVlan["id"]) + " atualizada com sucesso!")
                else:
                    print("Falha ao atualizar a VLAN")


class TelaPython:
    def __init__(self):
        #Muda o tema da tela
        sg.change_look_and_feel('Reddit')
        #Layout
        layout = [
            [sg.Text("Selecione a opção desejada:")],
            [sg.Radio('Coletar dados da Network','config',key='coletarVLANS'),sg.Radio('Configurar os IPs','config',key='configurarVLANS')],
            [sg.Text('Nome da Network: '),sg.Input(key='rest')],
            [sg.Button('Enviar Dados')],
            [sg.Output(size=(60,20))]

        ]
        #Janela
        self.janela = sg.Window("User: "+user+" - Config Aut IP's Template").layout(layout)


    def Iniciar(self):
        while True:
            # Extrair dados
            self.button, self.values = self.janela.read()
            #print(self.values)

            rest = self.values['rest']
            coletarVLANS = self.values['coletarVLANS']
            configurarVLANS = self.values['configurarVLANS']

            if coletarVLANS == True:
                teste = getVlans(rest)
                teste.execGetVlans()
                print("\n")
                print ("Execução finalizada...")
            if configurarVLANS == True:
                teste = putVlans(rest)
                teste.execPutVlans()
                print("\n")
                print ("Execução finalizada...")

tela = TelaPython()
tela.Iniciar()



