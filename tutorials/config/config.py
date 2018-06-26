import configparser


def print_all():
    config = configparser.ConfigParser()
    config.read('config.ini')
    print("Sections: ", config.sections())
    for section in config.sections():
        print_section(config, section)


def print_section(config, name):
    print("For section ", name, " :")
    if name in config:
        for key in config[name]:
            print('key, value: ', key, ", ", config[name][key])


print_all()