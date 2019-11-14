import connexion

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
    #TODO: implement
    print(kwargs)
    return default_response, 200

def drive_track_post(**kwargs):
    #TODO: implement
    print(kwargs)
    return default_response, 200
