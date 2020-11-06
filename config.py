"""this is config file read info from settings.ini."""

import configparser


# create a parser object
config = configparser.ConfigParser()
# read the config
config.read('E:/Python/books_parser/settings.ini')

PATH = config['PATH']['PATH']
HEADERS = {'user-agent': config['user-agent']['user-agent'],
           'accept': config['accept']['accept']}
HOST = config['HOST']['HOST']
PATH_TO_OUTPUT_FILE = config['PATH_TO_OUTPUT_FILE']['PATH_TO_OUTPUT_FILE']
