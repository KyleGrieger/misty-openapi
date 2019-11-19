# Org.OpenAPITools.Api.DefaultApi

All URIs are relative to *http://localhost:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**Drive**](DefaultApi.md#drive) | **POST** /api/drive | Drive
[**DriveHeading**](DefaultApi.md#driveheading) | **POST** /api/drive/hdt | Drive Heading
[**DriveTime**](DefaultApi.md#drivetime) | **POST** /api/drive/time | Drive Time
[**DriveTrack**](DefaultApi.md#drivetrack) | **POST** /api/drive/track | Drive Track
[**GetDeviceInformation**](DefaultApi.md#getdeviceinformation) | **GET** /api/device | Get Device Information
[**Stop**](DefaultApi.md#stop) | **POST** /api/drive/stop | Stop



## Drive

> List&lt;InlineResponse200&gt; Drive (Object linearVelocity = null, Object angularVelocity = null, InlineObject inlineObject = null)

Drive

Drive

### Example

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using Org.OpenAPITools.Api;
using Org.OpenAPITools.Client;
using Org.OpenAPITools.Model;

namespace Example
{
    public class DriveExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "http://localhost:3000";
            var apiInstance = new DefaultApi(Configuration.Default);
            var linearVelocity = new Object(); // Object |  (optional) 
            var angularVelocity = new Object(); // Object |  (optional) 
            var inlineObject = new InlineObject(); // InlineObject |  (optional) 

            try
            {
                // Drive
                List<InlineResponse200> result = apiInstance.Drive(linearVelocity, angularVelocity, inlineObject);
                Debug.WriteLine(result);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling DefaultApi.Drive: " + e.Message );
                Debug.Print("Status Code: "+ e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **linearVelocity** | [**Object**](Object.md)|  | [optional] 
 **angularVelocity** | [**Object**](Object.md)|  | [optional] 
 **inlineObject** | [**InlineObject**](InlineObject.md)|  | [optional] 

### Return type

[**List&lt;InlineResponse200&gt;**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DriveHeading

> List&lt;InlineResponse2001&gt; DriveHeading (Object heading = null, Object distance = null, Object timeMS = null, InlineObject2 inlineObject2 = null)

Drive Heading

Drive Heading

### Example

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using Org.OpenAPITools.Api;
using Org.OpenAPITools.Client;
using Org.OpenAPITools.Model;

namespace Example
{
    public class DriveHeadingExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "http://localhost:3000";
            var apiInstance = new DefaultApi(Configuration.Default);
            var heading = new Object(); // Object |  (optional) 
            var distance = new Object(); // Object |  (optional) 
            var timeMS = new Object(); // Object |  (optional) 
            var inlineObject2 = new InlineObject2(); // InlineObject2 |  (optional) 

            try
            {
                // Drive Heading
                List<InlineResponse2001> result = apiInstance.DriveHeading(heading, distance, timeMS, inlineObject2);
                Debug.WriteLine(result);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling DefaultApi.DriveHeading: " + e.Message );
                Debug.Print("Status Code: "+ e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **heading** | [**Object**](Object.md)|  | [optional] 
 **distance** | [**Object**](Object.md)|  | [optional] 
 **timeMS** | [**Object**](Object.md)|  | [optional] 
 **inlineObject2** | [**InlineObject2**](InlineObject2.md)|  | [optional] 

### Return type

[**List&lt;InlineResponse2001&gt;**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DriveTime

> List&lt;InlineResponse200&gt; DriveTime (Object linearVelocity = null, Object angularVelocity = null, Object timeMS = null, InlineObject3 inlineObject3 = null)

Drive Time

Drive Time

### Example

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using Org.OpenAPITools.Api;
using Org.OpenAPITools.Client;
using Org.OpenAPITools.Model;

namespace Example
{
    public class DriveTimeExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "http://localhost:3000";
            var apiInstance = new DefaultApi(Configuration.Default);
            var linearVelocity = new Object(); // Object |  (optional) 
            var angularVelocity = new Object(); // Object |  (optional) 
            var timeMS = new Object(); // Object |  (optional) 
            var inlineObject3 = new InlineObject3(); // InlineObject3 |  (optional) 

            try
            {
                // Drive Time
                List<InlineResponse200> result = apiInstance.DriveTime(linearVelocity, angularVelocity, timeMS, inlineObject3);
                Debug.WriteLine(result);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling DefaultApi.DriveTime: " + e.Message );
                Debug.Print("Status Code: "+ e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **linearVelocity** | [**Object**](Object.md)|  | [optional] 
 **angularVelocity** | [**Object**](Object.md)|  | [optional] 
 **timeMS** | [**Object**](Object.md)|  | [optional] 
 **inlineObject3** | [**InlineObject3**](InlineObject3.md)|  | [optional] 

### Return type

[**List&lt;InlineResponse200&gt;**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DriveTrack

> List&lt;InlineResponse200&gt; DriveTrack (Object rightTrackSpeed = null, Object leftTrackSpeed = null, InlineObject1 inlineObject1 = null)

Drive Track

Drive Track

### Example

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using Org.OpenAPITools.Api;
using Org.OpenAPITools.Client;
using Org.OpenAPITools.Model;

namespace Example
{
    public class DriveTrackExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "http://localhost:3000";
            var apiInstance = new DefaultApi(Configuration.Default);
            var rightTrackSpeed = new Object(); // Object |  (optional) 
            var leftTrackSpeed = new Object(); // Object |  (optional) 
            var inlineObject1 = new InlineObject1(); // InlineObject1 |  (optional) 

            try
            {
                // Drive Track
                List<InlineResponse200> result = apiInstance.DriveTrack(rightTrackSpeed, leftTrackSpeed, inlineObject1);
                Debug.WriteLine(result);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling DefaultApi.DriveTrack: " + e.Message );
                Debug.Print("Status Code: "+ e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rightTrackSpeed** | [**Object**](Object.md)|  | [optional] 
 **leftTrackSpeed** | [**Object**](Object.md)|  | [optional] 
 **inlineObject1** | [**InlineObject1**](InlineObject1.md)|  | [optional] 

### Return type

[**List&lt;InlineResponse200&gt;**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetDeviceInformation

> List&lt;InlineResponse2001&gt; GetDeviceInformation ()

Get Device Information

Get Device Information

### Example

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using Org.OpenAPITools.Api;
using Org.OpenAPITools.Client;
using Org.OpenAPITools.Model;

namespace Example
{
    public class GetDeviceInformationExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "http://localhost:3000";
            var apiInstance = new DefaultApi(Configuration.Default);

            try
            {
                // Get Device Information
                List<InlineResponse2001> result = apiInstance.GetDeviceInformation();
                Debug.WriteLine(result);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling DefaultApi.GetDeviceInformation: " + e.Message );
                Debug.Print("Status Code: "+ e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**List&lt;InlineResponse2001&gt;**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## Stop

> List&lt;InlineResponse200&gt; Stop ()

Stop

Stop

### Example

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using Org.OpenAPITools.Api;
using Org.OpenAPITools.Client;
using Org.OpenAPITools.Model;

namespace Example
{
    public class StopExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "http://localhost:3000";
            var apiInstance = new DefaultApi(Configuration.Default);

            try
            {
                // Stop
                List<InlineResponse200> result = apiInstance.Stop();
                Debug.WriteLine(result);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling DefaultApi.Stop: " + e.Message );
                Debug.Print("Status Code: "+ e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**List&lt;InlineResponse200&gt;**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

