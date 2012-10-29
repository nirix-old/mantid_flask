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

from db import Base
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship, backref

class Issue(Base):
    __tablename__ = 'issues'

    id = Column(Integer, primary_key=True)
    issue_id = Column(Integer)
    summary = Column(String(255))
    info = Column(Text)
    user_id = Column(Integer, ForeignKey('users.id'))
    project_id = Column(Integer, ForeignKey('projects.id'))
    user = relationship('User')

    def __init__(self, name, slug, info):
        self.name = name
        self.slug = slug
        self.info = info
