# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 10:23:11 2023

@author: Max
"""

from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship

from declarative_base import Base

class Metabolito(Base):
    
    __tablename__ = 'metabolito'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    concentracion = Column(Float)
    voxel_id = Column(Integer, ForeignKey('voxel.id'))
    voxel = relationship('Voxel', back_populates='metabolitos')