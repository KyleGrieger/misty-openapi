# openapi_client.DefaultApi

All URIs are relative to *http://localhost:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**drive**](DefaultApi.md#drive) | **POST** /api/drive | Drive POST
[**drive_get**](DefaultApi.md#drive_get) | **GET** /api/drive | Drive GET
[**drive_track**](DefaultApi.md#drive_track) | **POST** /api/drive/track | Drive Track Post
[**drive_track_get**](DefaultApi.md#drive_track_get) | **GET** /api/drive/track | Drive Track GET
[**get_device_information**](DefaultApi.md#get_device_information) | **GET** /api/device | Device GET
[**stop**](DefaultApi.md#stop) | **POST** /api/drive/stop | Drive Stop POST
[**stop_get**](DefaultApi.md#stop_get) | **GET** /api/drive/stop | Drive Stop GET


# **drive**
> list[InlineResponse200] drive(inline_object=inline_object)

Drive POST

Drive

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.DefaultApi()
inline_object = openapi_client.InlineObject() # InlineObject |  (optional)

try:
    # Drive POST
    api_response = api_instance.drive(inline_object=inline_object)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->drive: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object** | [**InlineObject**](InlineObject.md)|  | [optional] 

### Return type

[**list[InlineResponse200]**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **drive_get**
> list[InlineResponse200] drive_get(angular_velocity=angular_velocity, linear_velocity=linear_velocity, body=body)

Drive GET

Drive

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.DefaultApi()
angular_velocity = 3.4 # float |  (optional)
linear_velocity = 3.4 # float |  (optional)
body = None # object |  (optional)

try:
    # Drive GET
    api_response = api_instance.drive_get(angular_velocity=angular_velocity, linear_velocity=linear_velocity, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->drive_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **angular_velocity** | **float**|  | [optional] 
 **linear_velocity** | **float**|  | [optional] 
 **body** | **object**|  | [optional] 

### Return type

[**list[InlineResponse200]**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **drive_track**
> list[InlineResponse200] drive_track(inline_object1=inline_object1)

Drive Track Post

Drive Track

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.DefaultApi()
inline_object1 = openapi_client.InlineObject1() # InlineObject1 |  (optional)

try:
    # Drive Track Post
    api_response = api_instance.drive_track(inline_object1=inline_object1)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->drive_track: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object1** | [**InlineObject1**](InlineObject1.md)|  | [optional] 

### Return type

[**list[InlineResponse200]**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **drive_track_get**
> list[InlineResponse200] drive_track_get(left_track_speed=left_track_speed, right_track_speed=right_track_speed, body=body)

Drive Track GET

Drive Track

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.DefaultApi()
left_track_speed = 'left_track_speed_example' # str |  (optional)
right_track_speed = 'right_track_speed_example' # str |  (optional)
body = None # object |  (optional)

try:
    # Drive Track GET
    api_response = api_instance.drive_track_get(left_track_speed=left_track_speed, right_track_speed=right_track_speed, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->drive_track_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **left_track_speed** | **str**|  | [optional] 
 **right_track_speed** | **str**|  | [optional] 
 **body** | **object**|  | [optional] 

### Return type

[**list[InlineResponse200]**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_information**
> list[InlineResponse2001] get_device_information()

Device GET

Get Device Information

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.DefaultApi()

try:
    # Device GET
    api_response = api_instance.get_device_information()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_device_information: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[InlineResponse2001]**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop**
> list[InlineResponse200] stop()

Drive Stop POST

Stop

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.DefaultApi()

try:
    # Drive Stop POST
    api_response = api_instance.stop()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->stop: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[InlineResponse200]**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_get**
> list[InlineResponse200] stop_get()

Drive Stop GET

Stop

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.DefaultApi()

try:
    # Drive Stop GET
    api_response = api_instance.stop_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->stop_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[InlineResponse200]**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

