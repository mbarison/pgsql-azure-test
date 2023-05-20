"""
File: HealthFacility.py

Author: Marcello Barisonzi (CSBP/CPSE) <marcello.barisonzi@statcan.gc.ca>

Purpose: ORM Schema for LODE Educational Facilities

Date: 2023-05-20         

"""

from meta import *

from .CensusSubDivision import CensusSubDivision

class HealthFacility(Base):
    __tablename__ = "ODHF_1_1"
    __table_args__ = {'extend_existing': True}
    index = Column(String, primary_key=True)
    facility_name = Column(String)
    facility_type = Column(String)
    full_addr = Column(String)     
    unit = Column(String)         
    street_no = Column(String)    
    street_name = Column(String)     
    city = Column(String)           
    province = Column(String)      
    postal_code = Column(String)
    geometry = Column(Geometry(geometry_type='POINT', srid=4326))
    CSD = relationship(
        CensusSubDivision.__name__,
        primaryjoin='func.ST_Contains(foreign(CensusSubDivision.geometry), HealthFacility.geometry).as_comparison(1, 2)',
        #backref=backref('Educational_Facility', uselist=False),
        viewonly=True,
        uselist=False,

    )

"""
    facility_name              7033 non-null   object
 2   source_facility_type       7033 non-null   object
 3   odhf_facility_type         7033 non-null   object
 4   provider                   7033 non-null   object
 5   unit                       7033 non-null   object
 6   street_no                  7033 non-null   object
 7   street_name                7033 non-null   object
 8   postal_code                7033 non-null   object
 9   city                       7033 non-null   object
 10  province                   7033 non-null   object
 11  source_format_str_address  7033 non-null   object
 12  CSDname                    7033 non-null   object
 13  CSDuid                     7033 non-null   object
 14  Pruid                      7033 non-null   int64 
 15  latitude                   7033 non-null   object
 16  longitude  
 """