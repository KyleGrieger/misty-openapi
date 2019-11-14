import connexion
import os
import sys
import time
#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))
from sphero_sdk import SpheroRvrObserver
from sphero_sdk import RawMotorModesEnum

# Initialize rvr
rvr = SpheroRvrObserver()
rvr.wake()
rvr.reset_yaw()

success_response = [{'result': True, 'status':'Success'}]
device_information = [{'result': {'robotId': 12345, 'serialNumber': 12345}}]

# Get Device Information
def get_device_information(**kwargs):
    print(kwargs)
    return device_information, 200

# Drive 
def drive(**kwargs):
    print(kwargs)
    try:
        k=1
        left_mode = RawMotorModesEnum.forward.value
        right_mode = RawMotorModesEnum.forward.value
        x = kwargs['AngularVelocity']
        y = kwargs['LinearVelocity']

        left_speed = int(((y-(k*x))/100) * 255)
        right_speed = int(((y+(k*x))/100) * 255)

        if left_speed < 0:
            left_mode = RawMotorModesEnum.backward.value
        if right_speed < 0:
            right_mode = RawMotorModesEnum.backward.value

        rvr.raw_motors(
            left_mode=left_mode,
            left_speed=left_speed,  # Valid speed values are 0-255
            right_mode=right_mode,
            right_speed=right_speed  # Valid speed values are 0-255
        )
    except Exception as e:
        print(str(e))
        rvr.close()
        return [{'result': False, 'status': 'Failure', 'message': str(e)}], 500
    finally:
        return success_response, 200

def drive_get(**kwargs):
    print(kwargs)
    try:
        k=1
        left_mode = RawMotorModesEnum.forward.value
        right_mode = RawMotorModesEnum.forward.value
        x = kwargs['AngularVelocity']
        y = kwargs['LinearVelocity']

        left_speed = int(((y-(k*x))/100) * 255)
        right_speed = int(((y+(k*x))/100) * 255)

        if left_speed < 0:
            left_mode = RawMotorModesEnum.backward.value
        if right_speed < 0:
            right_mode = RawMotorModesEnum.backward.value

        rvr.raw_motors(
            left_mode=left_mode,
            left_speed=left_speed,  # Valid speed values are 0-255
            right_mode=right_mode,
            right_speed=right_speed  # Valid speed values are 0-255
        )
    except Exception as e:
        print(str(e))
        rvr.close()
        return [{'result': False, 'status': 'Failure', 'message': str(e)}], 500
    finally:
        return success_response, 200

# Stop
def stop(**kwargs):
    print(kwargs)
    try:
        rvr.raw_motors(
            left_mode=RawMotorModesEnum.forward.value,
            left_speed=0,  # Valid speed values are 0-255
            right_mode=RawMotorModesEnum.forward.value,
            right_speed=0  # Valid speed values are 0-255
        )
    except Exception as e:
        print(str(e))
        rvr.close()
        return [{'result': False, 'status': 'Failure', 'message': str(e)}], 500
    finally:
        return success_response, 200

def stop_get(**kwargs):
    print(kwargs)
    try:
        rvr.raw_motors(
            left_mode=RawMotorModesEnum.forward.value,
            left_speed=0,  # Valid speed values are 0-255
            right_mode=RawMotorModesEnum.forward.value,
            right_speed=0  # Valid speed values are 0-255
        )
    except Exception as e:
        print(str(e))
        rvr.close()
        return [{'result': False, 'status': 'Failure', 'message': str(e)}], 500
    finally:
        return success_response, 200

#Drive Track
def drive_track(**kwargs):
    print(kwargs)
    try:
        left_mode = RawMotorModesEnum.forward.value
        right_mode = RawMotorModesEnum.forward.value

        left_speed = int((kwargs['LeftTrackSpeed']/100) * 255)
        right_speed = int((kwargs['RightTrackSpeed']/100) * 255)

        if left_speed < 0:
            left_mode = RawMotorModesEnum.backward.value
        if right_speed < 0:
            right_mode = RawMotorModesEnum.backward.value

        rvr.raw_motors(
            left_mode=left_mode,
            left_speed=left_speed,  # Valid speed values are 0-255
            right_mode=right_mode,
            right_speed=right_speed  # Valid speed values are 0-255
        )
    except Exception as e:
        print(str(e))
        rvr.close()
        return [{'result': False, 'status': 'Failure', 'message': str(e)}], 500
    finally:
        return success_response, 200

def drive_track_get(**kwargs):
    print(kwargs)
    try:
        left_mode = RawMotorModesEnum.forward.value
        right_mode = RawMotorModesEnum.forward.value

        left_speed = int((kwargs['LeftTrackSpeed']/100) * 255)
        right_speed = int((kwargs['RightTrackSpeed']/100) * 255)

        if left_speed < 0:
            left_mode = RawMotorModesEnum.backward.value
        if right_speed < 0:
            right_mode = RawMotorModesEnum.backward.value

        rvr.raw_motors(
            left_mode=left_mode,
            left_speed=left_speed,  # Valid speed values are 0-255
            right_mode=right_mode,
            right_speed=right_speed  # Valid speed values are 0-255
        )
    except Exception as e:
        print(str(e))
        rvr.close()
        return [{'result': False, 'status': 'Failure', 'message': str(e)}], 500
    finally:
        return success_response, 200
