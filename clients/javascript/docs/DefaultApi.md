# MistyApi.DefaultApi

All URIs are relative to *http://localhost:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**drive**](DefaultApi.md#drive) | **POST** /api/drive | Drive
[**driveHeading**](DefaultApi.md#driveHeading) | **POST** /api/drive/hdt | Drive Heading
[**driveTime**](DefaultApi.md#driveTime) | **POST** /api/drive/time | Drive Time
[**driveTrack**](DefaultApi.md#driveTrack) | **POST** /api/drive/track | Drive Track
[**getDeviceInformation**](DefaultApi.md#getDeviceInformation) | **GET** /api/device | Get Device Information
[**stop**](DefaultApi.md#stop) | **POST** /api/drive/stop | Stop



## drive

> [InlineResponse200] drive(opts)

Drive

Drive

### Example

```javascript
import MistyApi from 'misty_api';

let apiInstance = new MistyApi.DefaultApi();
let opts = {
  'linearVelocity': null, // Object | 
  'angularVelocity': null, // Object | 
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
 **linearVelocity** | [**Object**](.md)|  | [optional] 
 **angularVelocity** | [**Object**](.md)|  | [optional] 
 **inlineObject** | [**InlineObject**](InlineObject.md)|  | [optional] 

### Return type

[**[InlineResponse200]**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## driveHeading

> [InlineResponse2001] driveHeading(opts)

Drive Heading

Drive Heading

### Example

```javascript
import MistyApi from 'misty_api';

let apiInstance = new MistyApi.DefaultApi();
let opts = {
  'heading': null, // Object | 
  'distance': null, // Object | 
  'timeMS': null, // Object | 
  'inlineObject2': new MistyApi.InlineObject2() // InlineObject2 | 
};
apiInstance.driveHeading(opts, (error, data, response) => {
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
 **heading** | [**Object**](.md)|  | [optional] 
 **distance** | [**Object**](.md)|  | [optional] 
 **timeMS** | [**Object**](.md)|  | [optional] 
 **inlineObject2** | [**InlineObject2**](InlineObject2.md)|  | [optional] 

### Return type

[**[InlineResponse2001]**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## driveTime

> [InlineResponse200] driveTime(opts)

Drive Time

Drive Time

### Example

```javascript
import MistyApi from 'misty_api';

let apiInstance = new MistyApi.DefaultApi();
let opts = {
  'linearVelocity': null, // Object | 
  'angularVelocity': null, // Object | 
  'timeMS': null, // Object | 
  'inlineObject3': new MistyApi.InlineObject3() // InlineObject3 | 
};
apiInstance.driveTime(opts, (error, data, response) => {
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
 **linearVelocity** | [**Object**](.md)|  | [optional] 
 **angularVelocity** | [**Object**](.md)|  | [optional] 
 **timeMS** | [**Object**](.md)|  | [optional] 
 **inlineObject3** | [**InlineObject3**](InlineObject3.md)|  | [optional] 

### Return type

[**[InlineResponse200]**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## driveTrack

> [InlineResponse200] driveTrack(opts)

Drive Track

Drive Track

### Example

```javascript
import MistyApi from 'misty_api';

let apiInstance = new MistyApi.DefaultApi();
let opts = {
  'rightTrackSpeed': null, // Object | 
  'leftTrackSpeed': null, // Object | 
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
 **rightTrackSpeed** | [**Object**](.md)|  | [optional] 
 **leftTrackSpeed** | [**Object**](.md)|  | [optional] 
 **inlineObject1** | [**InlineObject1**](InlineObject1.md)|  | [optional] 

### Return type

[**[InlineResponse200]**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getDeviceInformation

> [InlineResponse2001] getDeviceInformation()

Get Device Information

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

Stop

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

