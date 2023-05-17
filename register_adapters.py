"""
File: register_adapters.py

Author: Marcello Barisonzi (CSBP/CPSE) <marcello.barisonzi@statcan.gc.ca>

Purpose: Adapt psycopg2 to import numpy and geoalchemy2 data types
         References: 
         - https://stackoverflow.com/questions/39564755/programmingerror-psycopg2-programmingerror-cant-adapt-type-numpy-ndarray
         - https://github.com/geoalchemy/geoalchemy2/issues/132#issuecomment-270290483

Date: 2023-05-17         

"""

import numpy as np
from psycopg2.extensions import register_adapter, AsIs, adapt
from geoalchemy2.elements import WKBElement

def WKBElementAdapter(element):
    return AsIs(adapt(element.desc).getquoted())

def adapt_numpy_float64(numpy_float64):
    return AsIs(numpy_float64)

def adapt_numpy_int64(numpy_int64):
    return AsIs(numpy_int64)

def adapt_numpy_float32(numpy_float32):
    return AsIs(numpy_float32)

def adapt_numpy_int32(numpy_int32):
    return AsIs(numpy_int32)

def adapt_numpy_array(numpy_array):
    return AsIs(tuple(numpy_array))

def register_adapters():
    register_adapter(WKBElement, WKBElementAdapter)
    register_adapter(np.float64, adapt_numpy_float64)
    register_adapter(np.int64, adapt_numpy_int64)
    register_adapter(np.float32, adapt_numpy_float32)
    register_adapter(np.int32, adapt_numpy_int32)
    register_adapter(np.ndarray, adapt_numpy_array)   