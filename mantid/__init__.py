"""
Mantid
Copyright (C) 2012-2013 Nirix
https://github.com/nirix

Mantid is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; version 3 only.

Mantid is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Mantid. If not, see <http://www.gnu.org/licenses/>.
"""

import yaml
from flask import Flask
app = Flask(__name__, static_folder="../public", static_path="", template_folder="templates")

# Attempt to load the settings file
try:
    conf_file = open('settings.yml')
    conf = yaml.load(conf_file)
    conf_file.close()
except:
    raise Exception('Error loading settings.yml')

#app.config['db'] = conf['database']
#app.config['port'] = conf['port']

for (index, value) in conf.items():
    app.config[index] = value
