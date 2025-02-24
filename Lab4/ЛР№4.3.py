def generate_access_config(access, psecurity=False):
    """
    access - словарь access-портов,
    для которых необходимо сгенерировать конфигурацию, вида:
    { 'FastEthernet0/12':10,
      'FastEthernet0/14':11,
      'FastEthernet0/16':17 }
    psecurity - контролирует нужна ли настройка Port Security. По умолчанию значение False
        - если значение True, то настройка выполняется с добавлением шаблона port_security
        - если значение False, то настройка не выполняется
    Функция возвращает словарь:
    - ключи: имена интерфейсов, вида 'FastEthernet0/1'
    - значения: список команд, который надо выполнить на этом интерфейсе
    """
    access_template = [
        'switchport mode access',
        'switchport access vlan',
        'switchport nonegotiate',
        'spanning-tree portfast',
        'spanning-tree bpduguard enable'
    ]

    port_security_template = [
        'switchport port-security maximum 2',
        'switchport port-security violation restrict',
        'switchport port-security'
    ]

    config_dict = {}

    for interface, vlan in access.items():
        commands = [f'interface {interface}']
        for command in access_template:
            if command == 'switchport access vlan':
                commands.append(f'{command} {vlan}')
            else:
                commands.append(command)
        if psecurity:
            commands.extend(port_security_template)
        config_dict[interface] = commands

    return config_dict


access_dict = {'FastEthernet0/12': 10,
               'FastEthernet0/14': 11,
               'FastEthernet0/16': 17,
               'FastEthernet0/17': 150}

config_without_security = generate_access_config(access_dict)
print("Config without port-security:")
for interface, commands in config_without_security.items():
    print(f"{interface}:")
    for command in commands:
        print(command)

config_with_security = generate_access_config(access_dict, psecurity=True)
print("\nConfig with port-security:")
for interface, commands in config_with_security.items():
    print(f"{interface}:")
    for command in commands:
        print(command)
