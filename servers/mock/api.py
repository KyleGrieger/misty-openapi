import connexion

default_response = [{'result': True, 'status':'Not implemented'}]
device_information = [{'result':{'robotId': 12345, 'serialNumber': 12345}}]

# Get Device Information
def get_device_information(**kwargs):
    #TODO: implement
    print(kwargs)
    return device_information, 200

# Drive 
def drive(**kwargs):
    #TODO: implement
    print(kwargs)
    return default_response, 200

def drive_get(**kwargs):
    #TODO: implement
    print(kwargs)
    return default_response, 200

# Stop
def stop(**kwargs):
    #TODO: implement
    print(kwargs)
    return default_response, 200

def stop_get(**kwargs):
    #TODO: implement
    print(kwargs)
    return default_response, 200

#Drive Track
def drive_track(**kwargs):
    #TODO: implement
    print(kwargs)
    return default_response, 200

def drive_track_get(**kwargs):
    #TODO: implement
    print(kwargs)
    return default_response, 200



