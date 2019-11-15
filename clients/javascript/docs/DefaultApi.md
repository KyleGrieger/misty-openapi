# MistyApi.DefaultApi

All URIs are relative to *http://localhost:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**drive**](DefaultApi.md#drive) | **POST** /api/drive | Drive POST
[**driveGet**](DefaultApi.md#driveGet) | **GET** /api/drive | Drive GET
[**driveTrack**](DefaultApi.md#driveTrack) | **POST** /api/drive/track | Drive Track Post
[**driveTrackGet**](DefaultApi.md#driveTrackGet) | **GET** /api/drive/track | Drive Track GET
[**getDeviceInformation**](DefaultApi.md#getDeviceInformation) | **GET** /api/device | Device GET
[**stop**](DefaultApi.md#stop) | **POST** /api/drive/stop | Drive Stop POST
[**stopGet**](DefaultApi.md#stopGet) | **GET** /api/drive/stop | Drive Stop GET



## drive

> [InlineResponse200] drive(opts)

Drive POST

Drive

### Example

```javascript
import MistyApi from 'misty_api';

let apiInstance = new MistyApi.DefaultApi();
let opts = {
  'inlineObject': new MistyApi.InlineObject() // InlineObject | 
};
apiInstance.drive(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inlineObject** | [**InlineObject**](InlineObject.md)|  | [optional] 

### Return type

[**[InlineResponse200]**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## driveGet

> [InlineResponse200] driveGet(opts)

Drive GET

Drive

### Example

```javascript
import MistyApi from 'misty_api';

let apiInstance = new MistyApi.DefaultApi();
let opts = {
  'angularVelocity': 3.4, // Number | 
  'linearVelocity': 3.4, // Number | 
  'body': null // Object | 
};
apiInstance.driveGet(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **angularVelocity** | **Number**|  | [optional] 
 **linearVelocity** | **Number**|  | [optional] 
 **body** | **Object**|  | [optional] 

### Return type

[**[InlineResponse200]**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## driveTrack

> [InlineResponse200] driveTrack(opts)

Drive Track Post

Drive Track

### Example

```javascript
import MistyApi from 'misty_api';

let apiInstance = new MistyApi.DefaultApi();
let opts = {
  'inlineObject1': new MistyApi.InlineObject1() // InlineObject1 | 
};
apiInstance.driveTrack(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inlineObject1** | [**InlineObject1**](InlineObject1.md)|  | [optional] 

### Return type

[**[InlineResponse200]**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## driveTrackGet

> [InlineResponse200] driveTrackGet(opts)

Drive Track GET

Drive Track

### Example

```javascript
import MistyApi from 'misty_api';

let apiInstance = new MistyApi.DefaultApi();
let opts = {
  'leftTrackSpeed': "leftTrackSpeed_example", // String | 
  'rightTrackSpeed': "rightTrackSpeed_example", // String | 
  'body': null // Object | 
};
apiInstance.driveTrackGet(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **leftTrackSpeed** | **String**|  | [optional] 
 **rightTrackSpeed** | **String**|  | [optional] 
 **body** | **Object**|  | [optional] 

### Return type

[**[InlineResponse200]**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getDeviceInformation

> [InlineResponse2001] getDeviceInformation()

Device GET

Get Device Information

### Example

```javascript
import MistyApi from 'misty_api';

let apiInstance = new MistyApi.DefaultApi();
apiInstance.getDeviceInformation((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[InlineResponse2001]**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## stop

> [InlineResponse200] stop()

Drive Stop POST

Stop

### Example

```javascript
import MistyApi from 'misty_api';

let apiInstance = new MistyApi.DefaultApi();
apiInstance.stop((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[InlineResponse200]**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## stopGet

> [InlineResponse200] stopGet()

Drive Stop GET

Stop

### Example

```javascript
import MistyApi from 'misty_api';

let apiInstance = new MistyApi.DefaultApi();
apiInstance.stopGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[InlineResponse200]**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

