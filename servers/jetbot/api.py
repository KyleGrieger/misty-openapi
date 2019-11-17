import connexion
import socket    

hostname = socket.gethostname()    
ip_address = socket.gethostbyname(hostname)  

default_response = [{'result': True, 'status':'Not implemented'}]
device_information = [{'result':{'robotId': '12345', 'serialNumber': '12345', 'ipAddress': str(ip_address)}}]

# Drive 
def drive(**kwargs):
    #TODO: implement
    print(kwargs)
    return default_response, 200

# Stop
def stop(**kwargs):
    #TODO: implement
    print(kwargs)
    return default_response, 200 

# Get Device Information
def get_device_information(**kwargs):
    #TODO: implement
    print(kwargs)
    return device_information, 200

# Drive Track
def drive_track(**kwargs):
    #TODO: implement
    print(kwargs)
    return default_response, 200

# Drive Heading
def drive_heading(**kwargs):
    #TODO: implement
    print(kwargs)
    return default_response, 200

# Drive Time
def drive_time(**kwargs):
    #TODO: implement
    print(kwargs)
    return default_response, 200



