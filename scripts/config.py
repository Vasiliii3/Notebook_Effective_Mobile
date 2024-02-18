import os
from pathlib import Path
import configparser

file = os.path.join(Path(__file__).parent.parent, 'settings.ini')

config = configparser.ConfigParser()
config.read(file)
COUNTLIENS = int(config['DEFAULT']['CountLines'])
NAME = config['DEFAULT']['Name']

FILE = "notebook.txt"
ENCODING = "utf-8-sig"
DELIMITER = ";"


