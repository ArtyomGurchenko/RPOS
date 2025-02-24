ignore = ['duplex', 'alias', 'Current configuration']


def ignore_command(command, ignore):
    """
    Функция проверяет содержится ли в команде слово из списка ignore.
    command - строка. Команда, которую надо проверить
    ignore - список. Список слов
    Возвращает True, если в команде содержится слово из списка ignore, False - если нет
    """
    return any(word in command for word in ignore)


def config_to_dict(config_filename):
    """
    config - имя конфигурационного файла коммутатора
    Возвращает словарь:
    - Все команды верхнего уровня (глобального режима конфигурации), будут ключами.
    - Если у команды верхнего уровня есть подкоманды,
      они должны быть в значении у соответствующего ключа, в виде списка (пробелы вначале можно оставлять).
    - Если у команды верхнего уровня нет подкоманд, то значение будет пустым списком
    """
    config_dict = {}

    with open(config_filename) as file:
        current_command = None
        for line in file:
            line = line.rstrip()
            if line.startswith('!') or ignore_command(line, ignore):
                continue
            if not line.startswith(' '):
                current_command = line
                config_dict[current_command] = []
            else:
                if current_command:
                    config_dict[current_command].append(line)

    return config_dict


config_filename = 'config_sw1.txt'
config_dict = config_to_dict(config_filename)

for command, subcommands in config_dict.items():
    print(f"{command}:")
    for subcommand in subcommands:
        print(f"  {subcommand}")
