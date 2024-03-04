import configparser
import os
from pathlib import Path

file = os.path.join(Path(__file__).parent.parent, 'settings.ini')

config = configparser.ConfigParser()
config.read(file, encoding="utf-8")
COUNTLIENS = int(config['DEFAULT']['CountLines'])
NAME = config['DEFAULT']['Name']

FILE = "notebook.txt"
ENCODING = "utf-8-sig"
DELIMITER = ";"
