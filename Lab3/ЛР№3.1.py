with open('ospf.txt') as f:
    lines = f.readlines()

for line in lines:
    line = line.strip()
    parts = line.split()

    protocol = "OSPF"
    prefix = parts[1]
    ad_metric = parts[2].strip('[]')
    next_hop = parts[4].strip(',')
    last_update = parts[5].strip(',')
    outbound_interface = parts[6]

    print(f"Protocol: {protocol}")
    print(f"Prefix: {prefix}")
    print(f"AD/Metric: {ad_metric}")
    print(f"Next-Hop: {next_hop}")
    print(f"Last update: {last_update}")
    print(f"Outbound Interface: {outbound_interface}\n")
