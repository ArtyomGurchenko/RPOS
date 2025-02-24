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
    Возвращает список всех команд, которые были сгенерированы на основе шаблона
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

    config_lines = []

    for interface, vlan in access.items():
        config_lines.append(f'interface {interface}')
        for command in access_template:
            if command == 'switchport access vlan':
                config_lines.append(f'{command} {vlan}')
            else:
                config_lines.append(command)
        if psecurity:
            config_lines.extend(port_security_template)

    return config_lines


access_dict = {'FastEthernet0/12': 10,
               'FastEthernet0/14': 11,
               'FastEthernet0/16': 17,
               'FastEthernet0/17': 150}

config_without_security = generate_access_config(access_dict)
print("Config without port-security:")
for line in config_without_security:
    print(line)

config_with_security = generate_access_config(access_dict, psecurity=True)
print("\nConfig with port-security:")
for line in config_with_security:
    print(line)
