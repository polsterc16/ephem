# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 12:46:00 2019

@author: polsterc16

==============================================================================
 LICENCE INFORMATION
==============================================================================
This Software uses Code (spg4) provided by "Brandon Rhodes" under
the "MIT License". For more Information see "licence-info.txt".

Diese Software benutzt Code (spg4), welcher von "Brandon Rhodes" unter
der "MIT License" zur Verfuegung gestellt wird. Fuer weitere Information
siehe "licence-info.txt".
==============================================================================

"""

import math
import sgp4.ext as sgp4_ext







def vector_add(v1=[0,0,0], v2=[0,0,0]):
    """ v1 + v2 """
    return [v1[0]+v2[0], v1[1]+v2[1], v1[2]+v2[2]]

def vector_sub(v1=[0,0,0], v2=[0,0,0]):
    """ v1 - v2 """
    return [v1[0]-v2[0], v1[1]-v2[1], v1[2]-v2[2]]

def vector_cross(v1=[0,0,0], v2=[0,0,0]):
    """ v1 x v2 """
    temp=[0,0,0]
    sgp4_ext.cross(v1,v2,temp)
    return temp

def vector_dot(v1=[0,0,0], v2=[0,0,0]):
    """ v1 • v2 """
    return sgp4_ext.dot(v1,v2)

def vector_angle(v1=[1,0,0], v2=[1,0,0]):
    return sgp4_ext.angle(v1,v2)

def vector_abs(v=[0,0,0]):
    return sgp4_ext.mag(v)



def sin_deg(angle_deg):
    """ returns sin for angle in degrees """
    return math.sin(math.radians(angle_deg))

def cos_deg(angle_deg):
    """ returns cos for angle in degrees """
    return math.cos(math.radians(angle_deg))

def tan_deg(angle_deg):
    """ returns tan for angle in degrees """
    return math.tan(math.radians(angle_deg))


def asin_deg(value):
    """ returns asin as angle in degrees """
    return math.degrees(math.asin(value) )

def acos_deg(value):
    """ returns acos as angle in degrees """
    return math.degrees(math.acos(value) )

def atan_deg(value):
    """ returns atan as angle in degrees """
    return math.degrees(math.atan(value) )

def atan2_deg(val1,val2):
    """ returns atan2 as angle in degrees """
    return math.degrees(math.atan2(val1,val2) )




