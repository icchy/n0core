from os.path import join, dirname, abspath
import configparser

# read config.ini
config = configparser.ConfigParser()
config.read(join(dirname(abspath(__file__)), 'config.ini'))
