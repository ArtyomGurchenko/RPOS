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
    config - имя конфигурационного файла
    Возвращает вложенный словарь с командами и подкомандами
    """
    config_dict = {}
    with open(config_filename) as file:
        current_command = None
        current_subcommand = None
        for line in file:
            line = line.rstrip()
            if line.startswith('!') or ignore_command(line, ignore):
                continue
            if not line.startswith(' '):
                current_command = line
                config_dict[current_command] = {}
                current_subcommand = None
            elif line.startswith(' ') and not line.startswith('  '):
                current_subcommand = line
                if current_command:
                    config_dict[current_command][current_subcommand] = []
            elif line.startswith('  '):
                if current_command and current_subcommand:
                    config_dict[current_command][current_subcommand].append(line.strip())

    return config_dict


config_filename = 'config_r1.txt'
config_dict = config_to_dict(config_filename)

for command, subcommands in config_dict.items():
    print(f"{command}:")
    if isinstance(subcommands, dict):
        for subcommand, subsubcommands in subcommands.items():
            print(f"  {subcommand}")
            for subsubcommand in subsubcommands:
                print(f"    {subsubcommand}")
    else:
        for subcommand in subcommands:
            print(f"  {subcommand}")
