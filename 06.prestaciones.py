#Importamos la funcion manager de la biblioteca ncclient
from ncclient import manager

#inicia la funcion main
if __name__ == '__main__':

#Realizamos la conexion y la llamamos m
    with manager.connect(host="ios-xe-mgmt.cisco.com", port=10000,
                         username="root",
                         password="D_Vay!_10&",
                         hostkey_verify=False) as m:

        print("Estas son las capabilities:")

        #por cada linea de capabilities en m, la imprimimos en una linea aparte.
        for capability in m.server_capabilities:
            print(capability)