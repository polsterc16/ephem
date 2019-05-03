# -*- coding: utf-8 -*-
"""
Created on Thu Feb 12 13:09:46 2019

@author: polsterc16
"""


import datetime

import EPH_CORE_SkyObjectMgr as SOMgr
import EPH_CORE_TimeSpaceMgr as TSMgr
import EPH_ADD_math_helper as MH


def main():
    
    tnow = datetime.datetime.utcnow()
    tnow = datetime.datetime(tnow.year, tnow.month, tnow.day) # heute 00:00
    
    
    # GREENWICH
    # telescope = (("N",51+28/60+40.12/3600), ("E",0), 0)
    
    # GRAZ
    telescope = (('N',47+4/60),('E',15+26/60),353)
    
    
    # erstelle TSMgr Objekt
    myTS = TSMgr.TimeSpaceMgr(tnow, telescope[0], telescope[1], telescope[2])
    
    
    # -------------------------
    # AKTUALISIERUNG
    # dieser prozess kann zeit dauern!
    # benötigt internet verbindung und dass die celestrak website
    # noch existiert.
    maxAge = 0.5
    print("\nTLE age: {}".format(myTS.norad_get_age_in_days_str()))
    print("(update TLE if older than {:.2f} days)".format(maxAge))
    myTS.norad_update_if_older_than_days(maxAge)
    # -------------------------
    
    
    myTS.time_set_utcDateTime(tnow)
    skyObj = SOMgr.SkyObjectMgr(myTS,"moon",None)
    print("\n"+str(myTS.time_get_utcDateTime()))
    print(str(skyObj.get_type())+": "+str(skyObj.get_name()))
    print(skyObj.get_pos_spherical())
    
    myTS.time_set_utcDateTime(tnow)
    skyObj = SOMgr.SkyObjectMgr(myTS,"planet", "mars")
    print("\n"+str(myTS.time_get_utcDateTime()))
    print(str(skyObj.get_type())+": "+str(skyObj.get_name()))
    print(skyObj.get_pos_spherical())
    
    myTS.time_set_utcDateTime(tnow)
    skyObj = SOMgr.SkyObjectMgr(myTS,"Star", "Sirius")
    print("\n"+str(myTS.time_get_utcDateTime()))
    print(str(skyObj.get_type())+": "+str(skyObj.get_name()))
    print(skyObj.get_pos_spherical())
    
    myTS.time_set_utcNow()    
    skyObj = SOMgr.SkyObjectMgr(myTS,"sat", "25544")
    print("\n"+str(myTS.time_get_utcDateTime()))
    print(str(skyObj.get_type())+": "+str(skyObj.get_name()))
    print(skyObj.get_pos_spherical())
    
    
    
    

    
    

# exectute, if this is the main file
if __name__ == "__main__":
    main()





