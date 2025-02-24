def generate_trunk_config(trunk):
    """
    trunk - словарь trunk-портов для которых необходимо сгенерировать конфигурацию.
    Возвращает список всех команд, которые были сгенерированы на основе шаблона
    """
    trunk_template = [
        'switchport trunk encapsulation dot1q',
        'switchport mode trunk',
        'switchport trunk native vlan 999',
        'switchport trunk allowed vlan'
    ]

    config_lines = []

    for interface, vlans in trunk.items():
        config_lines.append(f'interface {interface}')
        for command in trunk_template:
            if command == 'switchport trunk allowed vlan':
                vlans_str = ','.join(str(vlan) for vlan in vlans)
                config_lines.append(f'{command} {vlans_str}')
            else:
                config_lines.append(command)

    return config_lines


trunk_dict = {'FastEthernet0/1': [10, 20, 30],
              'FastEthernet0/2': [11, 30],
              'FastEthernet0/4': [17]}

config = generate_trunk_config(trunk_dict)
for line in config:
    print(line)
