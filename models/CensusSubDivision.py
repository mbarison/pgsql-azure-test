"""
File: CensusSubDivision.py

Author: Marcello Barisonzi (CSBP/CPSE) <marcello.barisonzi@statcan.gc.ca>

Purpose: ORM Schema for Census Subdivisions

Date: 2023-05-17         

"""

from meta import *

class CensusSubDivision(Base):
    __tablename__ = "CSD_DBF_2021"
    DGUID = Column(String, primary_key=True)
    CSDUID = Column(Integer)
    name = Column(String)
    type = Column(String)
    geometry = Column(Geometry(geometry_type='GEOMETRY', srid=4326)) # GEOMETRY type allows for POLYGON and MULTIPOLYGON to coexist