import requests
import json
from tabulate import *

def obtenerTicket():
    requests.packages.urllib3.disable_warnings()

    api_url = "https://SandBoxAPICEM.cisco.com/api/v1/ticket"
    headers = {
        "content-type": "application/json"
    }
    body_json = {
        "username": "devnetuser",
        "password": "Cisco123!"
    }

    respuesta=requests.post(api_url,json.dumps(body_json),headers=headers,verify=False)

    print("El estado del ticket es: ", respuesta.status_code)

    respuesta_json = respuesta.json()
    Ticket = respuesta_json["response"]["serviceTicket"] 
    print("El numero de ticket es: ", Ticket)
    return Ticket


api_url = "https://sandboxapicem.cisco.com/api/v1/network-device"
ticket = obtenerTicket()
headers = {
 "content-type": "application/json",
 "X-Auth-Token": ticket
}

respuesta = requests.get(api_url, headers=headers, verify=False)
print("Estado del Host: ", respuesta.status_code)
if respuesta.status_code != 200:
    raise Exception("El codigo no es igual a 200 y hay un error. El texto de error es el sigueinte: " + resp.text)
respuestaEnJson = respuesta.json()

listaHosts = []
i = 0
for item in respuestaEnJson["response"]:
     i+=1
     host = [
             i,
             item["serialNumber"],
             item["family"],
             item["type"] ,
             item["macAddress"],
             item["hostname"],
             item["memorySize"],
             item["managementIpAddress"]
            ]
     listaHosts.append( host )
cabeceras = ["Número", "Familia", "Tipo", "Dirección MAC","Nombre", "Espacio de memoria", "IP"]
print( tabulate(listaHosts, cabeceras) )