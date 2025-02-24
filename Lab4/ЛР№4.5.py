def generate_trunk_config(trunk):
    """
    trunk - словарь trunk-портов,
    для которых необходимо сгенерировать конфигурацию, вида:
    { 'FastEthernet0/1': [10, 20],
      'FastEthernet0/2': [11, 30],
      'FastEthernet0/4': [17] }
    Возвращает словарь:
    - ключи: имена интерфейсов, вида 'FastEthernet0/1'
    - значения: список команд, который надо выполнить на этом интерфейсе
    """
    trunk_template = [
        'switchport trunk encapsulation dot1q',
        'switchport mode trunk',
        'switchport trunk native vlan 999',
        'switchport trunk allowed vlan'
    ]

    config_dict = {}

    for interface, vlans in trunk.items():
        commands = [f'interface {interface}']
        for command in trunk_template:
            if command == 'switchport trunk allowed vlan':
                vlans_str = ','.join(str(vlan) for vlan in vlans)
                commands.append(f'{command} {vlans_str}')
            else:
                commands.append(command)
        config_dict[interface] = commands

    return config_dict


trunk_dict = {'FastEthernet0/1': [10, 20, 30],
              'FastEthernet0/2': [11, 30],
              'FastEthernet0/4': [17]}

config = generate_trunk_config(trunk_dict)

for interface, commands in config.items():
    print(f"{interface}:")
    for command in commands:
        print(f"  {command}")
