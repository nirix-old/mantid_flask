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

from flask import render_template
from mantid import app
import mantid.routes as routes

@app.route('/')
def root():
    return routes.Projects().index()

@app.route('/register')
def register():
    return routes.Users().register()

@app.route('/p/<project>')
def project(project):
    return routes.Projects().view(project)

@app.route('/p/<project>/issues')
def issues(project):
    return routes.Issues().index(project)

@app.errorhandler(404)
def not_found(error):
    return render_template('errors/404.html')
