import numpy as np
from cereal import car
from selfdrive.can.parser import CANParser
from selfdrive.car.subaru.values import DBC, CAR

def get_obstacle_can_parser(CP, canbus):
  # this function generates lists for signal, messages and initial values
  signals = [
    # sig_name, sig_address, default
    ("Cruise_Activated", "ES_Status", 0),
    ("Cruise_On", "ES_Status", 0),
    ("Message", "ES_Status", 0),
    ("Message", "ES_Brake", 0),
    ("Message", "ES_RPM", 0),
    ("Message", "ES_LDW", 0),
    ("Message", "ES_CruiseThrottle", 0),
  ]
  
  checks = [
    # sig_address, frequency
    ("ES_Status", 20),
    ("ES_Brake", 20),
    ("ES_RPM", 20),
    ("ES_LDW", 20),
    ("ES_CruiseThrottle", 20),
  ]

  return CANParser(DBC[CP.carFingerprint]['pt'], signals, checks, canbus.obstacle)
  
class CamState(object):
  def __init__(self, CP, canbus):
    # initialize can parser
    self.car_fingerprint = CP.carFingerprint
    self.es_status = 0
    self.es_brake = 0
    self.es_rpm = 0
    self.es_ldw = 0
    self.es_cruisethrottle = 0
    self.acc_active = 0
    self.main_on = False
      
  def update(self, pt_cp):

    self.can_valid = pt_cp.can_valid
    self.can_valid = True
    
    if self.car_fingerprint == CAR.OUTBACK:
      self.es_status = pt_cp.vl["ES_Status"]['Message']
      self.es_brake = pt_cp.vl["ES_Brake"]['Message']
      self.es_rpm = pt_cp.vl["ES_RPM"]['Message']
      self.es_ldw = pt_cp.vl["ES_LDW"]['Message']
      self.es_cruisethrottle = pt_cp.vl["ES_CruiseThrottle"]['Message']
      self.acc_active = pt_cp.vl["ES_Status"]['Cruise_Activated']
      self.main_on = pt_cp.vl["ES_Status"]['Cruise_On']