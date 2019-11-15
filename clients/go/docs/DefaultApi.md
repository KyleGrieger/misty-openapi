# \DefaultApi

All URIs are relative to *http://localhost:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**Drive**](DefaultApi.md#Drive) | **Post** /api/drive | Drive POST
[**DriveGet**](DefaultApi.md#DriveGet) | **Get** /api/drive | Drive GET
[**DriveTrack**](DefaultApi.md#DriveTrack) | **Post** /api/drive/track | Drive Track Post
[**DriveTrackGet**](DefaultApi.md#DriveTrackGet) | **Get** /api/drive/track | Drive Track GET
[**GetDeviceInformation**](DefaultApi.md#GetDeviceInformation) | **Get** /api/device | Device GET
[**Stop**](DefaultApi.md#Stop) | **Post** /api/drive/stop | Drive Stop POST
[**StopGet**](DefaultApi.md#StopGet) | **Get** /api/drive/stop | Drive Stop GET



## Drive

> []InlineResponse200 Drive(ctx, optional)

Drive POST

Drive

### Required Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
 **optional** | ***DriveOpts** | optional parameters | nil if no parameters

### Optional Parameters

Optional parameters are passed through a pointer to a DriveOpts struct


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inlineObject** | [**optional.Interface of InlineObject**](InlineObject.md)|  | 

### Return type

[**[]InlineResponse200**](inline_response_200.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DriveGet

> []InlineResponse200 DriveGet(ctx, optional)

Drive GET

Drive

### Required Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
 **optional** | ***DriveGetOpts** | optional parameters | nil if no parameters

### Optional Parameters

Optional parameters are passed through a pointer to a DriveGetOpts struct


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **angularVelocity** | **optional.Float32**|  | 
 **linearVelocity** | **optional.Float32**|  | 
 **body** | **optional.Map[string]interface{}**|  | 

### Return type

[**[]InlineResponse200**](inline_response_200.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DriveTrack

> []InlineResponse200 DriveTrack(ctx, optional)

Drive Track Post

Drive Track

### Required Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
 **optional** | ***DriveTrackOpts** | optional parameters | nil if no parameters

### Optional Parameters

Optional parameters are passed through a pointer to a DriveTrackOpts struct


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inlineObject1** | [**optional.Interface of InlineObject1**](InlineObject1.md)|  | 

### Return type

[**[]InlineResponse200**](inline_response_200.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DriveTrackGet

> []InlineResponse200 DriveTrackGet(ctx, optional)

Drive Track GET

Drive Track

### Required Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
 **optional** | ***DriveTrackGetOpts** | optional parameters | nil if no parameters

### Optional Parameters

Optional parameters are passed through a pointer to a DriveTrackGetOpts struct


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **leftTrackSpeed** | **optional.String**|  | 
 **rightTrackSpeed** | **optional.String**|  | 
 **body** | **optional.Map[string]interface{}**|  | 

### Return type

[**[]InlineResponse200**](inline_response_200.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetDeviceInformation

> []InlineResponse2001 GetDeviceInformation(ctx, )

Device GET

Get Device Information

### Required Parameters

This endpoint does not need any parameter.

### Return type

[**[]InlineResponse2001**](inline_response_200_1.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## Stop

> []InlineResponse200 Stop(ctx, )

Drive Stop POST

Stop

### Required Parameters

This endpoint does not need any parameter.

### Return type

[**[]InlineResponse200**](inline_response_200.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## StopGet

> []InlineResponse200 StopGet(ctx, )

Drive Stop GET

Stop

### Required Parameters

This endpoint does not need any parameter.

### Return type

[**[]InlineResponse200**](inline_response_200.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

