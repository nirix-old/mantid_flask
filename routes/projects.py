"""
Mantid
Copyright (C) 2012 Nirix
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

from base import Base
from db import session
from models import Project

class Projects(Base):
    def index(self):
        projects = session.query(Project).all()
        return self.render('projects/index', projects=projects)

    def view(self, slug):
        project = session.query(Project).filter_by(slug=slug).first()
        return self.render('projects/view', project=project)
