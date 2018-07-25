import configparser
import os

# loop through config file
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


# write and read config file
command_config_file_path = 'config/config.ini'
path = os.path.join(os.getcwd(), command_config_file_path)

section_name = "AUTHORS"
item_name = "names"


def write_config():
    config = configparser.ConfigParser()
    config[section_name] = {}
    config[section_name][item_name] = 'Sam, Peter, John, Albert'
    with open(path, 'w') as configfile:
        config.write(configfile)


def read_config():
    config = configparser.ConfigParser()
    config.read(path)
    print(config.sections())
    if section_name in config:
        if item_name in config[section_name]:
            value = config[section_name][item_name]
            print(value)

def read_config_with_file_open():
    config = configparser.ConfigParser()
    with open(path, 'r') as configfile:
        config.read_file(configfile)
        print(config.sections())
        if section_name in config:
            if item_name in config[section_name]:
                value = config[section_name][item_name]
                print(value)

write_config()
read_config()
read_config_with_file_open()
