#importamos la funcion manager de la biblioteca ncclient
from ncclient import manager

#definimos plantillaNetconf como el archivo de configuracion 
plantillaNetconf = open("config-temp-ietf-interfaces.xml").read()

if __name__ == '__main__':

    #payloadNetconf es equivalente a la configuración que deseamos cambiar 
    payloadNetconf = plantillaNetconf.format(int_name="GigabitEthernet2",
                                              int_desc="Configurado por Germán mediante NETCONF",
                                              ip_address="10.255.255.1",
                                              subnet_mask="255.255.255.0"
                                              )
    print("Nueva configuración:")

    #imprimimos en el servidor la 
    print(payloadNetconf)
    with manager.connect(host="ios-xe-mgmt.cisco.com", port=10000,
                         username="root",
                         password="D_Vay!_10&",
                         hostkey_verify=False) as m:

        #imprimimos la nueva configuración, nada mas cambiarla
        respuestaNetconf = m.edit_config(payloadNetconf, target="running")

        print(respuestaNetconf)
