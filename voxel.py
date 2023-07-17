# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 10:33:29 2023

@author: Max
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from declarative_base import Base

class Voxel(Base):
   __tablename__ = 'voxel'

   id = Column(Integer, primary_key=True)
   fila = Column(Integer)
   columna = Column(Integer)
   
   metabolitos = relationship('Metabolito')
   imagen_id = Column(Integer, ForeignKey('imagen.id'))
   imagen = relationship('Imagen', back_populates='voxeles')
   region_id = Column(Integer, ForeignKey('region.id'))
   region = relationship('Region', back_populates='voxeles')  

   def __init__(self, fila, columna, imagen):
      self.fila = fila
      self.columna = columna
      self.imagen = imagen
      
   def __str__(self):
      return f'voxel: ({self.fila}, {self.columna})'
  
   
   