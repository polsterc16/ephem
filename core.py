# -*- coding: utf-8 -*-
"""
Created on Thu Feb 12 13:09:46 2019

@author: polsterc16
"""


import datetime

import EPH_CORE_SkyObjectMgr as SOMgr
import EPH_CORE_TimeSpaceMgr as TSMgr


def main():
    
    tnow = datetime.datetime(2019, 2, 18, 0)
    #tnow = datetime.datetime.utcnow()
    
    # GREENWICH
    tele = (("N",51+28/60+40.12/3600), ("E",5.31/3600), 0)
    
    skyObj = None
    pos={} # leeres dict für positionen
    
    
    
    
    # erstelle TSMgr Objekt
    myTS = TSMgr.TimeSpaceMgr(tnow, tele[0], tele[1], tele[2])
    
    # setze auf utcNow
    myTS.time_set_utcNow()
    
    
    
    # -------------------------
    # dieser prozess kann zeit dauern!
    # benötigt internet verbindung und dass die celestrak website
    # noch existiert.
    maxAge = 0.5
    print("\nTLE age: {:.4f} days".format(myTS.norad_get_age_in_days()))
    print("(update TLE if older than {:.2f} days)".format(maxAge))
    myTS.norad_update_if_older_than_days(maxAge)
    # -------------------------
    
    
    # testliste
    objList = [
            ["planet","mars"],
            ["sat", "25544"], #ISS
            ["star","Alpheratz"],
            ["star","BD+28°4"],
            ["star","HR:8998"],
            ["star","HR:8999"]
            ]
    
    
    for obj in objList:
        #erstelle skyObject
        skyObj = SOMgr.SkyObjectMgr(myTS,obj[0],obj[1])
        
        # hole aktuelle postion in "pos"
        skyObj.write_pos_to_dict(pos)
        
        # AUSGABE
        print("")
        print(myTS.time_get_utcDateTime()) #utc zeit
        
        # typ: name
        print(str(skyObj.get_type())+": "+str(skyObj.get_name()))
        
        # position
        print(pos)
        
    

# exectute, if this is the main file
if __name__ == "__main__":
    main()





