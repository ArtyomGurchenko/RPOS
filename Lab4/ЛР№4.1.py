def generate_access_config(access):
    """
    access - словарь access-портов,
    для которых необходимо сгенерировать конфигурацию, вида:
    { 'FastEthernet0/12':10,
    'FastEthernet0/14':11,
    'FastEthernet0/16':17}
    Возвращает список всех портов в режиме access с конфигурацией на основе шаблона
    """
    access_template = [
        'switchport mode access',
        'switchport access vlan',
        'switchport nonegotiate',
        'spanning-tree portfast',
        'spanning-tree bpduguard enable'
    ]

    config_lines = []

    for interface, vlan in access.items():
        config_lines.append(f'interface {interface}')
        for command in access_template:
            if command == 'switchport access vlan':
                config_lines.append(f'{command} {vlan}')
            else:
                config_lines.append(command)

    return config_lines


access_dict = {'FastEthernet0/12': 10,
               'FastEthernet0/14': 11,
               'FastEthernet0/16': 17,
               'FastEthernet0/17': 150}

config = generate_access_config(access_dict)
for line in config:
    print(line)

