from selfdrive.car.subaru.values import CAR, DBC

def create_steering_control(packer, bus, car_fingerprint, idx, steer, checksum):
  if car_fingerprint in (CAR.OUTBACK, CAR.LEGACY):

    values = {
      "Counter": idx,
      "LKAS_Output": steer,
      "LKAS_Active": 1 if steer != 0 else 0,
      "Checksum": checksum
    }
    return packer.make_can_msg("ES_LKAS", 0, values)
'''  if car_fingerprint == CAR.XV2018:
    values = {
      "Checksum": checksum,
      "Byte1": idx,
      "Byte2": steer1,
      "Byte3": byte2
    }
'''

