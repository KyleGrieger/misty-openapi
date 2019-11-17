import connexion
import os
import sys
import time
import socket 
#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))
from sphero_sdk import SpheroRvrObserver
from sphero_sdk import RawMotorModesEnum
from sphero_sdk import DriveFlagsBitmask

hostname = socket.gethostname()    
ip_address = socket.gethostbyname(hostname)  

# Initialize RVR
rvr = SpheroRvrObserver()
rvr.wake()
rvr.reset_yaw()

# Vars
configs = {}
success_response = [{'result': True, 'status':'Success'}]
device_information = [{'result':{'robotId': '12345', 'serialNumber': '12345', 'ipAddress': str(ip_address)}}]

# Drive 
def drive(**kwargs):
    print(kwargs)
    try:
        k=1
        left_mode = RawMotorModesEnum.forward.value
        right_mode = RawMotorModesEnum.forward.value
        x = float(kwargs['body']['AngularVelocity'])
        y = float(kwargs['body']['LinearVelocity'])
        print(x)
        print(y)
        left_speed = int(((y-(k*x))/100) * 255)
        right_speed = int(((y+(k*x))/100) * 255)
        print('left_speed')
        print(left_speed)
        print('right_speed')
        print(right_speed)
        if left_speed < 0:
            left_mode = RawMotorModesEnum.reverse.value
            left_speed = left_speed * -1
        if right_speed < 0:
            right_mode = RawMotorModesEnum.reverse.value
            right_speed = right_speed * -1

        # Hack so that values do not go over max 255
        if right_speed > 255:
            right_speed = 255
        if left_speed > 255:
            left_speed = 255

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

# Get Device Information
def get_device_information(**kwargs):
    print(kwargs)
    return device_information, 200

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

        # Hack so that values do not go over max 255
        if right_speed > 255:
            right_speed = 255
        if left_speed > 255:
            left_speed = 255

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

# Drive Heading
def drive_heading(**kwargs):
    print(kwargs)
    try:
        heading = int(kwargs['Heading'])
        distance = int(kwargs['Distance'])
        time_ms = int(kwargs['TimeMS'])

        rvr.drive_with_heading(
            speed=100,
            heading=heading,  # Valid heading values are 0-359
            flags=DriveFlagsBitmask.none.value,
            target=distance,
            timeout=time_ms
        )
    except Exception as e:
        print(str(e))
        rvr.close()
        return [{'result': False, 'status': 'Failure', 'message': str(e)}], 500
    finally:
        return success_response, 200

#Drive Time
def drive_time(**kwargs):
    print(kwargs)
    try:
        left_mode = RawMotorModesEnum.forward.value
        right_mode = RawMotorModesEnum.forward.value

        left_speed = int((kwargs['LeftTrackSpeed']/100) * 255)
        right_speed = int((kwargs['RightTrackSpeed']/100) * 255)
        time_ms = int(kwargs['TimeMS'])

        if left_speed < 0:
            left_mode = RawMotorModesEnum.backward.value
        if right_speed < 0:
            right_mode = RawMotorModesEnum.backward.value

        # Hack so that values do not go over max 255
        if right_speed > 255:
            right_speed = 255
        if left_speed > 255:
            left_speed = 255

        rvr.raw_motors(
            left_mode=left_mode,
            left_speed=left_speed,  # Valid speed values are 0-255
            right_mode=right_mode,
            right_speed=right_speed,  # Valid speed values are 0-255
            timeout = time_ms
        )
    except Exception as e:
        print(str(e))
        rvr.close()
        return [{'result': False, 'status': 'Failure', 'message': str(e)}], 500
    finally:
        return success_response, 200
