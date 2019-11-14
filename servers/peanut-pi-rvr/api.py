import connexion
import os
import sys
#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

import asyncio
from sphero_sdk import SpheroRvrAsync
from sphero_sdk import SerialAsyncDal
from sphero_sdk import RawMotorModesEnum

loop = asyncio.get_event_loop()

rvr = SpheroRvrAsync(
    dal=SerialAsyncDal(
        loop
    )
)
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
        loop.run_until_complete(
            drive_track(kwargs)
        )

    except KeyboardInterrupt:
        print('\nProgram terminated with keyboard interrupt.')

        loop.run_until_complete(
            rvr.close()
        )

    finally:
        if loop.is_running():
            loop.close()
    return default_response, 200

def drive_track_post(**kwargs):
    print(kwargs)
    try:
        loop.run_until_complete(
            drive_track(kwargs)
        )

    except KeyboardInterrupt:
        print('\nProgram terminated with keyboard interrupt.')

        loop.run_until_complete(
            rvr.close()
        )

    finally:
        if loop.is_running():
            loop.close()
    return default_response, 200

async def drive_track(kwargs):
    """ This program has RVR drive around in different directions.
    """

    await rvr.wake()

    # Give RVR time to wake up
    await asyncio.sleep(2)
    await rvr.reset_yaw()
    await rvr.raw_motors(
        left_mode=RawMotorModesEnum.forward.value,
        left_speed=int((kwargs.LeftTrackSpeed/100) * 255),  # Valid speed values are 0-255
        right_mode=RawMotorModesEnum.forward.value,
        right_speed=int((kwargs.LeftTrackSpeed/100) * 255)  # Valid speed values are 0-255
    )
    await rvr.close()
