## -*- coding: utf-8 -*-
#"""
#Created on Wed Feb  6 11:08:58 2019
#
#@author: polsterc16
#
#==============================================================================
# LICENCE INFORMATION
#==============================================================================
#This Software uses Code (spg4) provided by "Brandon Rhodes" under
#the "MIT License". For more Information see "licence-info.txt".
#
#Diese Software benutzt Code (spg4), welcher von "Brandon Rhodes" unter
#der "MIT License" zur Verfuegung gestellt wird. Fuer weitere Information
#siehe "licence-info.txt".
#==============================================================================
#
#"""
#
#
## ---------------------------------------------------
## IMPORTS
#
#
#import sys
#import os
#import datetime
#import math
#
#
#import TimeSpaceMgr as TSMgr
#from ADDED_FUNCTIONS import math_helper
##import norad_lists
#
#
#
## ---------------------------------------------------
## ---------------------------------------------------
## VARIABLES
#
#
#
#
#
#
## ---------------------------------------------------
## ---------------------------------------------------
## CLASSES
#
#class PlanetMgr:
#    '''   '''
#
#    def __init__(self, xxxxxxx):
#        '''   '''
#
#       
#    # ---------------------------------------------------
#
#
#    def get_idSuccess(self):
#        ''' returns whether the Satellite was created successfully '''
#        return self._idSuccess;
#
#    def get_TSMgrSuccess(self):
#        ''' returns whether the Satellite has valid TSMgr member  variable '''
#        return self._TSMgrSuccess;
#    # ---------------------------------------------------
#
#
#
#    # ---------------------------------------------------
#    # CALCULATIONS
#
#    def _check_time_for_calc(self, utcTime):
#        
##        # check TIME
##        if(utcTime==None):
##            # if None given, then use utcNow
##            self._TSMgr.time_set_utcNow()
##        else:
##            # otherwise use given time and update TSMgr to it
##            self._TSMgr.time_set_utcDateTime(utcTime)
##            
##        
##        time_now = self._TSMgr.time_get_utcDateTime()
##        
##        
##        # check for time difference
##        if(time_now != self._time_previous):
##            # time difference: calculate everything for new time
##            self._calc_all()    # start new calculation
##            self._time_previous = time_now  # update time_prev
#    # -------------
#
#
#
#
#
#
#    def _calc_all(self):
#        """ calculates everything from TSMgr utctime. 
#            To be called by '_check_time_for_calc' """
##        
##        self._propagate()
##        self._calc_geoc_equator_spherical()
##        self._calc_topoc_equator_spherical()
#    
#    # -------------
#    
#    
#    
#    
#    
#    
#    def _calc_topoc_equator_spherical(self):
#    # -------------
#    
#    
#    def _calc_geoc_equator_spherical(self):
#    # -------------
#    
#    
#    
#    def _propagate(self):
#    # -------------
#    
#    
#    # ---------------------------------------------------
#    # GET FUNCTIONS
#    
#    def get_pos_geoc_equator_cartesian(self, utcTimeDate=None):
#        
#
#
#
#    def get_str_satname(self):
#        # returns ID and name of sat as string
#        return "Satellite: ["+str(self.get_satnum())+"] - "+str(
#                self.get_satname())
#
#    def get_str_epoch(self):
#        # returns epoch in "year days"
#        return "Epoch: "+str(self.get_epochyr())+" "+str(self.get_epochdays())
#
#
#
#    def get_satname(self):
#        # Name of Satellite given in the TLE file.
#        return self._sat.satname
#
#    def get_satnum(self):
#        #'satnum'
#        #Unique satellite number given in the TLE file.
#        return self._sat.satnum
#
#    def get_epochyr(self):
#        #'epochyr'
#        #Full four-digit year of this element set's epoch moment.
#        return self._sat.epochyr
#
#    def get_epochdays(self):
#        #'epochdays'
#        #Fractional days into the year of the epoch moment.
#        return self._sat.epochdays
#
#    def get_jdsatepoch(self):
#        #'jdsatepoch'
#        #Julian date of the epoch (computed from 'epochyr' and 'epochdays').
#        return self._sat.jdsatepoch
#
#    def get_ndot(self):
#        #'ndot'
#        #First time derivative of the mean motion (ignored by SGP4).
#        return self._sat.ndot
#
#    def get_nddot(self):
#        #'nddot'
#        #Second time derivative of the mean motion (ignored by SGP4).
#        return self._sat.nddot
#
#    def get_bstar(self):
#        #'bstar'
#        #Ballistic drag coefficient B* in inverse earth radii.
#        return self._sat.bstar
#
#    def get_inclo(self):
#        #'inclo'
#        #Inclination in radians.
#        return self._sat.inclo
#
#    def get_nodeo(self):
#        #'nodeo'
#        #Right ascension of ascending node in radians.
#        return self._sat.nodeo
#
#    def get_ecco(self):
#        #'ecco'
#        #Eccentricity.
#        return self._sat.ecco
#
#    def get_argpo(self):
#        #'argpo'
#        #Argument of perigee in radians.
#        return self._sat.argpo
#
#    def get_mo(self):
#        #'mo'
#        #Mean anomaly in radians.
#        return self._sat.mo
#
#    def get_no(self):
#        #'no'
#        #Mean motion in radians per minute.
#        return self._sat.no
#
#
#
#
