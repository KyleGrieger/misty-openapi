# Org.OpenAPITools.Api.DefaultApi

All URIs are relative to *http://localhost:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**Drive**](DefaultApi.md#drive) | **POST** /api/drive | Drive POST
[**DriveGet**](DefaultApi.md#driveget) | **GET** /api/drive | Drive GET
[**DriveTrack**](DefaultApi.md#drivetrack) | **POST** /api/drive/track | Drive Track Post
[**DriveTrackGet**](DefaultApi.md#drivetrackget) | **GET** /api/drive/track | Drive Track GET
[**GetDeviceInformation**](DefaultApi.md#getdeviceinformation) | **GET** /api/device | Device GET
[**Stop**](DefaultApi.md#stop) | **POST** /api/drive/stop | Drive Stop POST
[**StopGet**](DefaultApi.md#stopget) | **GET** /api/drive/stop | Drive Stop GET



## Drive

> List&lt;InlineResponse200&gt; Drive (InlineObject inlineObject = null)

Drive POST

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
            var inlineObject = new InlineObject(); // InlineObject |  (optional) 

            try
            {
                // Drive POST
                List<InlineResponse200> result = apiInstance.Drive(inlineObject);
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


## DriveGet

> List&lt;InlineResponse200&gt; DriveGet (decimal angularVelocity = null, decimal linearVelocity = null, Object body = null)

Drive GET

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
    public class DriveGetExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "http://localhost:3000";
            var apiInstance = new DefaultApi(Configuration.Default);
            var angularVelocity = 8.14;  // decimal |  (optional) 
            var linearVelocity = 8.14;  // decimal |  (optional) 
            var body = ;  // Object |  (optional) 

            try
            {
                // Drive GET
                List<InlineResponse200> result = apiInstance.DriveGet(angularVelocity, linearVelocity, body);
                Debug.WriteLine(result);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling DefaultApi.DriveGet: " + e.Message );
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
 **angularVelocity** | **decimal**|  | [optional] 
 **linearVelocity** | **decimal**|  | [optional] 
 **body** | **Object**|  | [optional] 

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

> List&lt;InlineResponse200&gt; DriveTrack (InlineObject1 inlineObject1 = null)

Drive Track Post

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
            var inlineObject1 = new InlineObject1(); // InlineObject1 |  (optional) 

            try
            {
                // Drive Track Post
                List<InlineResponse200> result = apiInstance.DriveTrack(inlineObject1);
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


## DriveTrackGet

> List&lt;InlineResponse200&gt; DriveTrackGet (string leftTrackSpeed = null, string rightTrackSpeed = null, Object body = null)

Drive Track GET

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
    public class DriveTrackGetExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "http://localhost:3000";
            var apiInstance = new DefaultApi(Configuration.Default);
            var leftTrackSpeed = leftTrackSpeed_example;  // string |  (optional) 
            var rightTrackSpeed = rightTrackSpeed_example;  // string |  (optional) 
            var body = ;  // Object |  (optional) 

            try
            {
                // Drive Track GET
                List<InlineResponse200> result = apiInstance.DriveTrackGet(leftTrackSpeed, rightTrackSpeed, body);
                Debug.WriteLine(result);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling DefaultApi.DriveTrackGet: " + e.Message );
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
 **leftTrackSpeed** | **string**|  | [optional] 
 **rightTrackSpeed** | **string**|  | [optional] 
 **body** | **Object**|  | [optional] 

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

Device GET

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
                // Device GET
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

Drive Stop POST

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
                // Drive Stop POST
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


## StopGet

> List&lt;InlineResponse200&gt; StopGet ()

Drive Stop GET

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
    public class StopGetExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "http://localhost:3000";
            var apiInstance = new DefaultApi(Configuration.Default);

            try
            {
                // Drive Stop GET
                List<InlineResponse200> result = apiInstance.StopGet();
                Debug.WriteLine(result);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling DefaultApi.StopGet: " + e.Message );
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

