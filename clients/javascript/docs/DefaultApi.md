# MistyApi.DefaultApi

All URIs are relative to *http://localhost:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiDriveGet**](DefaultApi.md#apiDriveGet) | **GET** /api/drive | Your GET endpoint
[**apiDrivePost**](DefaultApi.md#apiDrivePost) | **POST** /api/drive | 
[**apiDriveStopGet**](DefaultApi.md#apiDriveStopGet) | **GET** /api/drive/stop | Your GET endpoint
[**apiDriveStopPost**](DefaultApi.md#apiDriveStopPost) | **POST** /api/drive/stop | 



## apiDriveGet

> [Object] apiDriveGet(opts)

Your GET endpoint

Drive

### Example

```javascript
import MistyApi from 'misty_api';

let apiInstance = new MistyApi.DefaultApi();
let opts = {
  'angularVelocity': 3.4, // Number | 
  'linearVelocity': 3.4, // Number | 
  'body': new MistyApi.ModelNull() // ModelNull | 
};
apiInstance.apiDriveGet(opts, (error, data, response) => {
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
 **body** | **ModelNull**|  | [optional] 

### Return type

**[Object]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, application/xml


## apiDrivePost

> [Object] apiDrivePost(opts)



Drive

### Example

```javascript
import MistyApi from 'misty_api';

let apiInstance = new MistyApi.DefaultApi();
let opts = {
  'inlineObject': new MistyApi.InlineObject() // InlineObject | 
};
apiInstance.apiDrivePost(opts, (error, data, response) => {
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

**[Object]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## apiDriveStopGet

> [Object] apiDriveStopGet()

Your GET endpoint

Stop

### Example

```javascript
import MistyApi from 'misty_api';

let apiInstance = new MistyApi.DefaultApi();
apiInstance.apiDriveStopGet((error, data, response) => {
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

**[Object]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiDriveStopPost

> [Object] apiDriveStopPost()



Stop

### Example

```javascript
import MistyApi from 'misty_api';

let apiInstance = new MistyApi.DefaultApi();
apiInstance.apiDriveStopPost((error, data, response) => {
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

**[Object]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

