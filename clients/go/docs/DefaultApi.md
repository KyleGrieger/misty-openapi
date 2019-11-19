# \DefaultApi

All URIs are relative to *http://localhost:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**Drive**](DefaultApi.md#Drive) | **Post** /api/drive | Drive
[**DriveHeading**](DefaultApi.md#DriveHeading) | **Post** /api/drive/hdt | Drive Heading
[**DriveTime**](DefaultApi.md#DriveTime) | **Post** /api/drive/time | Drive Time
[**DriveTrack**](DefaultApi.md#DriveTrack) | **Post** /api/drive/track | Drive Track
[**GetDeviceInformation**](DefaultApi.md#GetDeviceInformation) | **Get** /api/device | Get Device Information
[**Stop**](DefaultApi.md#Stop) | **Post** /api/drive/stop | Stop



## Drive

> []InlineResponse200 Drive(ctx, optional)

Drive

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
 **linearVelocity** | [**optional.Interface of map[string]interface{}**](.md)|  | 
 **angularVelocity** | [**optional.Interface of map[string]interface{}**](.md)|  | 
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


## DriveHeading

> []InlineResponse2001 DriveHeading(ctx, optional)

Drive Heading

Drive Heading

### Required Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
 **optional** | ***DriveHeadingOpts** | optional parameters | nil if no parameters

### Optional Parameters

Optional parameters are passed through a pointer to a DriveHeadingOpts struct


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **heading** | [**optional.Interface of map[string]interface{}**](.md)|  | 
 **distance** | [**optional.Interface of map[string]interface{}**](.md)|  | 
 **timeMS** | [**optional.Interface of map[string]interface{}**](.md)|  | 
 **inlineObject2** | [**optional.Interface of InlineObject2**](InlineObject2.md)|  | 

### Return type

[**[]InlineResponse2001**](inline_response_200_1.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DriveTime

> []InlineResponse200 DriveTime(ctx, optional)

Drive Time

Drive Time

### Required Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
 **optional** | ***DriveTimeOpts** | optional parameters | nil if no parameters

### Optional Parameters

Optional parameters are passed through a pointer to a DriveTimeOpts struct


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **linearVelocity** | [**optional.Interface of map[string]interface{}**](.md)|  | 
 **angularVelocity** | [**optional.Interface of map[string]interface{}**](.md)|  | 
 **timeMS** | [**optional.Interface of map[string]interface{}**](.md)|  | 
 **inlineObject3** | [**optional.Interface of InlineObject3**](InlineObject3.md)|  | 

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

Drive Track

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
 **rightTrackSpeed** | [**optional.Interface of map[string]interface{}**](.md)|  | 
 **leftTrackSpeed** | [**optional.Interface of map[string]interface{}**](.md)|  | 
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


## GetDeviceInformation

> []InlineResponse2001 GetDeviceInformation(ctx, )

Get Device Information

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

Stop

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

