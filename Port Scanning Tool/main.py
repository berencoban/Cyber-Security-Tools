import socket
from socket import *
import argparse
import pyfiglet as pyfiglet
from tabulate import tabulate
from socket import getservbyport


portList = []
serviceList = []
stateList = []
allPortsList = [*range(1,65535)]
allServicesList = []
allStatesList = []

def portsScan():
    targetPort = portList
    
        try:
            connectionSocket = socket(AF_INET, SOCK_STREAM)
            connectionSocket.connect((targetHost, targetPort))
            portList.append(targetPort)
            connectionSocket.close()
        except:
            portList.append(targetPort)

def serviceScan():
    string = portList[0]
    word = string.split(',')
    for a in range(0,len(word)):
        word[a] = int(word[a])
    protocolname = 'tcp'
    for port in word:
        results = getservbyport(port, protocolname)
        serviceList.append(results)

def stateScan():
    string = portList[0]
    word = string.split(',')
    for a in range(0, len(word)):
        word[a] = int(word[a])
    for targetPort in word:
        connectionSocket = socket(AF_INET, SOCK_STREAM)
        connectionSocket.settimeout(2)
        result = connectionSocket.connect_ex((targetHost, targetPort))
        if result == 0:
            stateList.append("open")
            connectionSocket.close()
        else:
            stateList.append("close")



parser = argparse.ArgumentParser()
parser.add_argument("-t", "--target IP", dest='targetIP', required=True, help="Target IP")
parser.add_argument("-sV", "--services", dest="services", required=False, action="store_true")
parser.add_argument("-p", "--ports", dest="ports", required=False, help="Target ports list")
parser.add_argument("-p-", "--all ports", dest="allPorts", required=False, action="store_true")

args = parser.parse_args()
targetHost = args.targetIP

if _name_ == '_main_':
    asciiBanner = pyfiglet.figlet_format("PORT SCANNER")
    print(asciiBanner)
    targetHost = args.targetIP



    if args.ports != None:
        portList.append(args.ports)
        for port in portList:
             c = port.replace(",", "\n")
        portsScan()
    else:
        print("No ports specified")


    if args.services == True:
        serviceScan()
        a = "\n".join(serviceList)


    if args.ports != None:
        stateScan()
        b = "\n".join(stateList)





    data = [[c, a, b]]
    print(tabulate(data, headers=["PORT", "SERVICE", "STATE"]))
