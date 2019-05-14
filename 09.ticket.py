import json
import requests
requests.packages.urllib3.disable_warnings()

api_url = "https://SandBoxAPICEM.cisco.com/api/v1/ticket"
headers = {
    "content-type": "application/json"
}
jsonAuth = {
    "username": "devnetuser",
    "password": "Cisco123!"
}

respuesta=requests.post(api_url,json.dumps(jsonAuth),headers=headers,verify=False)

print("El estado del ticket es: ", respuesta.status_code)

respuesta_json = respuesta.json()
Ticket = respuesta_json["response"]["serviceTicket"] 
print("El numero de ticket es: ", Ticket)