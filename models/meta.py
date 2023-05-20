from sqlalchemy import Boolean, BigInteger, Column, DateTime, Float, ForeignKey, BigInteger, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from geoalchemy2 import Geometry

Base = declarative_base()
