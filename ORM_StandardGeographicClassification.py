"""
File: ORM_StandardGeographicClassification.py

Author: Marcello Barisonzi (CSBP/CPSE) <marcello.barisonzi@statcan.gc.ca>

Purpose: ORM Schema for the Standard Geographic Classification

Date: 2023-05-17         

"""

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Float
from geoalchemy2 import Geometry

Base = declarative_base()

class CSD(Base):
    __tablename__ = "CSD_DBF_2021"
    DGUID = Column(String, primary_key=True)
    CSDUID = Column(Integer)
    CSDNAME = Column(String)
    CSDTYPE = Column(String)
    LANDAREA = Column(Float)
    geometry = Column(Geometry(geometry_type='GEOMETRY', srid=4326)) # GEOMETRY type allows for POLYGON and MULTIPOLYGON to coexist