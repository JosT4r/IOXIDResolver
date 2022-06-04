#!/usr/bin/python

import sys, getopt

from impacket.dcerpc.v5 import transport
from impacket.dcerpc.v5.rpcrt import RPC_C_AUTHN_LEVEL_NONE
from impacket.dcerpc.v5.dcomrt import IObjectExporter

def main(ipadd):

    target_ip = ipadd

    authLevel = RPC_C_AUTHN_LEVEL_NONE

    stringBinding = r'ncacn_ip_tcp:%s' % target_ip
    rpctransport = transport.DCERPCTransportFactory(stringBinding)

    portmap = rpctransport.get_dce_rpc()
    portmap.set_auth_level(authLevel)
    portmap.connect()

    objExporter = IObjectExporter(portmap)
    bindings = objExporter.ServerAlive2()

    print "[*] Retrieving network interface of " + target_ip

    #NetworkAddr = bindings[0]['aNetworkAddr']
    for binding in bindings:
        NetworkAddr = binding['aNetworkAddr']
        print "Address: " + NetworkAddr
def read_ip():
    f = open("C:\\Git\\IOXIDResolver\\ip.txt","r") 
    lines = f.readlines()
    #main('140.114.60.76')
    for line in lines:
        ip=line.replace("\n",'')
        try:
            main(ip)
        except:
            print 'error'

if __name__ == "__main__":
   # main(sys.argv[1:])
    read_ip()