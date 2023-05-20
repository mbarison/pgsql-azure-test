"""
File: EducationalFacility.py

Author: Marcello Barisonzi (CSBP/CPSE) <marcello.barisonzi@statcan.gc.ca>

Purpose: ORM Schema for LODE Educational Facilities

Date: 2023-05-20         

"""

from meta import *

from .CensusSubDivision import CensusSubDivision

class EducationalFacility(Base):
    __tablename__ = "ODEF_2_1"
    __table_args__ = {'extend_existing': True}
    index = Column(String, primary_key=True)
    Facility_Name = Column(String)
    Full_Addr = Column(String)     
    Unit = Column(String)         
    Street_No = Column(String)    
    Street_Name = Column(String)     
    City = Column(String)           
    Prov_Terr = Column(String)      
    Postal_Code = Column(String)
    geometry = Column(Geometry(geometry_type='POINT', srid=4326))
    CSD = relationship(
        CensusSubDivision.__name__,
        primaryjoin='func.ST_Contains(foreign(CensusSubDivision.geometry), EducationalFacility.geometry).as_comparison(1, 2)',
        #backref=backref('Educational_Facility', uselist=False),
        viewonly=True,
        uselist=False,

    )