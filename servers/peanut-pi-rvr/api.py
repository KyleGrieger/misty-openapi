import connexion
import os
import sys
import time
#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from sphero_sdk import SpheroRvrObserver
from sphero_sdk import RawMotorModesEnum


rvr = SpheroRvrObserver()
rvr.wake()

# Give RVR time to wake up
time.sleep(2)

rvr.reset_yaw()
default_response = [{'result': True, 'status':'Success'}]
default_device_response = [{'robotId': 12345, 'serialNumber': 12345}]

def device_get(**kwargs):
    #TODO: implement
    print(kwargs)
    return default_device_response, 200

def drive_get(**kwargs):
    #TODO: implement
    print(kwargs)
    return default_response, 200

def drive_post(**kwargs):
    #TODO: implement
    print(kwargs)
    return default_response, 200

def drive_stop_get(**kwargs):
    #TODO: implement
    print(kwargs)
    return default_response, 200

def drive_stop_post(**kwargs):
    #TODO: implement
    print(kwargs)
    return default_response, 200 

def drive_track_get(**kwargs):
    print(kwargs)
    try:
        rvr.raw_motors(
            left_mode=RawMotorModesEnum.forward.value,
            left_speed=int((kwargs.LeftTrackSpeed/100) * 255),  # Valid speed values are 0-255
            right_mode=RawMotorModesEnum.forward.value,
            right_speed=int((kwargs.LeftTrackSpeed/100) * 255)  # Valid speed values are 0-255
        )

    except KeyboardInterrupt:
        print('\nProgram terminated with keyboard interrupt.')
        rvr.close()

    # finally:
    #     rvr.close()
    return default_response, 200

def drive_track_post(**kwargs):
    print(kwargs)
    try:
        rvr.raw_motors(
            left_mode=RawMotorModesEnum.forward.value,
            left_speed=int((kwargs.LeftTrackSpeed/100) * 255),  # Valid speed values are 0-255
            right_mode=RawMotorModesEnum.forward.value,
            right_speed=int((kwargs.LeftTrackSpeed/100) * 255)  # Valid speed values are 0-255
        )

    except KeyboardInterrupt:
        print('\nProgram terminated with keyboard interrupt.')
        rvr.close()

    # finally:
    #     rvr.close()
    return default_response, 200
