# openapi_client.DefaultApi

All URIs are relative to *http://localhost:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_drive_get**](DefaultApi.md#api_drive_get) | **GET** /api/drive | Your GET endpoint
[**api_drive_post**](DefaultApi.md#api_drive_post) | **POST** /api/drive | 
[**api_drive_stop_get**](DefaultApi.md#api_drive_stop_get) | **GET** /api/drive/stop | Your GET endpoint
[**api_drive_stop_post**](DefaultApi.md#api_drive_stop_post) | **POST** /api/drive/stop | 


# **api_drive_get**
> list[object] api_drive_get(angular_velocity=angular_velocity, linear_velocity=linear_velocity, body=body)

Your GET endpoint

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
body = openapi_client.Null() # Null |  (optional)

try:
    # Your GET endpoint
    api_response = api_instance.api_drive_get(angular_velocity=angular_velocity, linear_velocity=linear_velocity, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_drive_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **angular_velocity** | **float**|  | [optional] 
 **linear_velocity** | **float**|  | [optional] 
 **body** | **Null**|  | [optional] 

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_drive_post**
> list[object] api_drive_post(inline_object=inline_object)



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
    api_response = api_instance.api_drive_post(inline_object=inline_object)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_drive_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object** | [**InlineObject**](InlineObject.md)|  | [optional] 

### Return type

**list[object]**

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

# **api_drive_stop_get**
> list[object] api_drive_stop_get()

Your GET endpoint

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
    # Your GET endpoint
    api_response = api_instance.api_drive_stop_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_drive_stop_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[object]**

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

# **api_drive_stop_post**
> list[object] api_drive_stop_post()



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
    api_response = api_instance.api_drive_stop_post()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_drive_stop_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[object]**

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

