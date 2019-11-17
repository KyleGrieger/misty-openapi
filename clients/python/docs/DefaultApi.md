# openapi_client.DefaultApi

All URIs are relative to *http://localhost:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**drive**](DefaultApi.md#drive) | **POST** /api/drive | Drive
[**drive_heading**](DefaultApi.md#drive_heading) | **POST** /api/drive/hdt | Drive Heading
[**drive_time**](DefaultApi.md#drive_time) | **POST** /api/drive/time | Drive Time
[**drive_track**](DefaultApi.md#drive_track) | **POST** /api/drive/track | Drive Track
[**get_device_information**](DefaultApi.md#get_device_information) | **GET** /api/device | Get Device Information
[**stop**](DefaultApi.md#stop) | **POST** /api/drive/stop | Stop


# **drive**
> list[InlineResponse200] drive(inline_object=inline_object)

Drive

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
    # Drive
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

# **drive_heading**
> list[InlineResponse2001] drive_heading(inline_object2=inline_object2)

Drive Heading

Drive Heading

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.DefaultApi()
inline_object2 = openapi_client.InlineObject2() # InlineObject2 |  (optional)

try:
    # Drive Heading
    api_response = api_instance.drive_heading(inline_object2=inline_object2)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->drive_heading: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object2** | [**InlineObject2**](InlineObject2.md)|  | [optional] 

### Return type

[**list[InlineResponse2001]**](InlineResponse2001.md)

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

# **drive_time**
> list[InlineResponse200] drive_time(inline_object3=inline_object3)

Drive Time

Drive Time

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.DefaultApi()
inline_object3 = openapi_client.InlineObject3() # InlineObject3 |  (optional)

try:
    # Drive Time
    api_response = api_instance.drive_time(inline_object3=inline_object3)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->drive_time: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object3** | [**InlineObject3**](InlineObject3.md)|  | [optional] 

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

Drive Track

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
    # Drive Track
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

# **get_device_information**
> list[InlineResponse2001] get_device_information()

Get Device Information

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
    # Get Device Information
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

Stop

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
    # Stop
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

