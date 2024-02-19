#Using data file sample-data.json, create output that resembles the following by parsing the included JSON file.
"""
Interface Status
================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------
topology/pod-1/node-201/sys/phys-[eth1/33]                              inherit   9150 
topology/pod-1/node-201/sys/phys-[eth1/34]                              inherit   9150 
topology/pod-1/node-201/sys/phys-[eth1/35]                              inherit   9150 
"""
import json
with open('file.json') as f:
    data = json.load(f)
    
interface=data['imdata']
print("Interface Status")
print("=" *80)
print("DN                                                 Description           Speed    MTU  ")
print("-" *50, '-'*20,  '-'*8,  '-'*5)
for x in interface:
    dn = x['l1PhysIf']['attributes']['dn']
    speed = x['l1PhysIf']['attributes']['speed']
    mtu = x['l1PhysIf']['attributes']['mtu']
    print(f"{dn:<72} inherit   {mtu:<6}")

