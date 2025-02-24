def get_int_vlan_map(config_filename):
    access_ports = {}
    trunk_ports = {}

    with open(config_filename) as file:
        for line in file:
            line = line.strip()
            if line.startswith('interface'):
                interface = line.split()[1]
            elif 'switchport mode access' in line:
                access_ports[interface] = None
            elif 'switchport access vlan' in line:
                vlan = int(line.split()[-1])
                access_ports[interface] = vlan
            elif 'switchport mode trunk' in line:
                trunk_ports[interface] = []
            elif 'switchport trunk allowed vlan' in line:
                vlans = line.split()[-1].split(',')
                trunk_ports[interface] = [int(vlan) for vlan in vlans]

    access_ports = {k: v for k, v in access_ports.items() if v is not None}

    return access_ports, trunk_ports


config_filename = 'config_sw1.txt'
access_dict, trunk_dict = get_int_vlan_map(config_filename)

print("Access ports:")
for interface, vlan in access_dict.items():
    print(f"{interface}: {vlan}")

print("\nTrunk ports:")
for interface, vlans in trunk_dict.items():
    print(f"{interface}: {vlans}")
