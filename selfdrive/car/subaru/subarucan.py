def create_steering_control(packer, bus, idx, steer1, byte2, lkas_request, checksum):

  values = {
    "Byte0": idx,
    "Byte1": steer1,
    "Byte2": byte2,
    "Byte3": lkas_request,
    "Checksum": checksum,
  }

  return packer.make_can_msg("ES_LKAS", bus, values)
'''
def create_es_brake(packer, bus, message_brake):

  values = {
    "Message": message_brake,
  }

  return packer.make_can_msg("ES_Brake", bus, values)

def create_es_rpm(packer, bus, message_rpm):

  values = {
    "Message": message_rpm,
  }

  return packer.make_can_msg("ES_RPM", bus, values)

def create_es_ldw(packer, bus, message_ldw):

  values = {
    "Message": message_ldw,
  }

  return packer.make_can_msg("ES_LDW", bus, values)

def create_es_cruisethrottle(packer, bus, message_ct):

  values = {
    "Message": message_ct,
  }

  return packer.make_can_msg("ES_CruiseThrottle", bus, values)

def create_es_status(packer, bus, message_status):

  values = {
    "Message": message_status,
  }

  return packer.make_can_msg("ES_Status", bus, values)

def create_wheel(packer, bus, message_wheel):

  values = {
    "Message": message_wheel,
  }

  return packer.make_can_msg("WHEEL_SPEEDS", bus, values)
'''