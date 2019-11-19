# DefaultApi

All URIs are relative to *http://localhost:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**drive**](DefaultApi.md#drive) | **POST** /api/drive | Drive
[**driveHeading**](DefaultApi.md#driveHeading) | **POST** /api/drive/hdt | Drive Heading
[**driveTime**](DefaultApi.md#driveTime) | **POST** /api/drive/time | Drive Time
[**driveTrack**](DefaultApi.md#driveTrack) | **POST** /api/drive/track | Drive Track
[**getDeviceInformation**](DefaultApi.md#getDeviceInformation) | **GET** /api/device | Get Device Information
[**stop**](DefaultApi.md#stop) | **POST** /api/drive/stop | Stop


<a name="drive"></a>
# **drive**
> List&lt;InlineResponse200&gt; drive(linearVelocity, angularVelocity, inlineObject)

Drive

Drive

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:3000");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Object linearVelocity = null; // Object | 
    Object angularVelocity = null; // Object | 
    InlineObject inlineObject = new InlineObject(); // InlineObject | 
    try {
      List<InlineResponse200> result = apiInstance.drive(linearVelocity, angularVelocity, inlineObject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#drive");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **linearVelocity** | [**Object**](.md)|  | [optional] [default to null]
 **angularVelocity** | [**Object**](.md)|  | [optional] [default to null]
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
**200** | OK |  -  |

<a name="driveHeading"></a>
# **driveHeading**
> List&lt;InlineResponse2001&gt; driveHeading(heading, distance, timeMS, inlineObject2)

Drive Heading

Drive Heading

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:3000");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Object heading = null; // Object | 
    Object distance = null; // Object | 
    Object timeMS = null; // Object | 
    InlineObject2 inlineObject2 = new InlineObject2(); // InlineObject2 | 
    try {
      List<InlineResponse2001> result = apiInstance.driveHeading(heading, distance, timeMS, inlineObject2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#driveHeading");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **heading** | [**Object**](.md)|  | [optional] [default to null]
 **distance** | [**Object**](.md)|  | [optional] [default to null]
 **timeMS** | [**Object**](.md)|  | [optional] [default to null]
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
**200** | OK |  -  |

<a name="driveTime"></a>
# **driveTime**
> List&lt;InlineResponse200&gt; driveTime(linearVelocity, angularVelocity, timeMS, inlineObject3)

Drive Time

Drive Time

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:3000");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Object linearVelocity = null; // Object | 
    Object angularVelocity = null; // Object | 
    Object timeMS = null; // Object | 
    InlineObject3 inlineObject3 = new InlineObject3(); // InlineObject3 | 
    try {
      List<InlineResponse200> result = apiInstance.driveTime(linearVelocity, angularVelocity, timeMS, inlineObject3);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#driveTime");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **linearVelocity** | [**Object**](.md)|  | [optional] [default to null]
 **angularVelocity** | [**Object**](.md)|  | [optional] [default to null]
 **timeMS** | [**Object**](.md)|  | [optional] [default to null]
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
**200** | OK |  -  |

<a name="driveTrack"></a>
# **driveTrack**
> List&lt;InlineResponse200&gt; driveTrack(rightTrackSpeed, leftTrackSpeed, inlineObject1)

Drive Track

Drive Track

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:3000");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Object rightTrackSpeed = null; // Object | 
    Object leftTrackSpeed = null; // Object | 
    InlineObject1 inlineObject1 = new InlineObject1(); // InlineObject1 | 
    try {
      List<InlineResponse200> result = apiInstance.driveTrack(rightTrackSpeed, leftTrackSpeed, inlineObject1);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#driveTrack");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rightTrackSpeed** | [**Object**](.md)|  | [optional] [default to null]
 **leftTrackSpeed** | [**Object**](.md)|  | [optional] [default to null]
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
**200** | OK |  -  |

<a name="getDeviceInformation"></a>
# **getDeviceInformation**
> List&lt;InlineResponse2001&gt; getDeviceInformation()

Get Device Information

Get Device Information

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:3000");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      List<InlineResponse2001> result = apiInstance.getDeviceInformation();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getDeviceInformation");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
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
**200** | OK |  -  |

<a name="stop"></a>
# **stop**
> List&lt;InlineResponse200&gt; stop()

Stop

Stop

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:3000");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      List<InlineResponse200> result = apiInstance.stop();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#stop");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
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
**200** | OK |  -  |

