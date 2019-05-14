from ncclient import manager
import xmltodict


netconf_filter = open("filter-ietf-interfaces.xml").read()

if __name__ == '__main__':
    with manager.connect(host="ios-xe-mgmt.cisco.com", port=10000,
                         username="root",
                         password="D_Vay!_10&",
                         hostkey_verify=False) as m:


        netconf_reply = m.get(netconf_filter)


        intf_details = xmltodict.parse(netconf_reply.xml)["rpc-reply"]["data"]
        intf_config = intf_details["interfaces"]["interface"]
        intf_info = intf_details["interfaces-state"]["interface"]

        print("Detalles de la interfaz:")
        print("  Nombre: {}".format(intf_config["name"]["#text"]))
        print("  Descripción: {}".format(intf_config["description"]))
        print("  Tipo: {}".format(intf_config["type"]["#text"]))
        print("  Dirección MAC: {}".format(intf_info["phys-address"]))
        print("  Entrada de packets: {}".format(intf_info["statistics"]["in-unicast-pkts"]))
        print("  Salida de packets: {}".format(intf_info["statistics"]["out-unicast-pkts"]))
