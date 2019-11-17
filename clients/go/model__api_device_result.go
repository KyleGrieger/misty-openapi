/*
 * Misty API
 *
 * Misty Open API
 *
 * API version: 1.0
 * Generated by: OpenAPI Generator (https://openapi-generator.tech)
 */

package openapi
// ApiDeviceResult struct for ApiDeviceResult
type ApiDeviceResult struct {
	RobotId map[string]interface{} `json:"robotId,omitempty"`
	SerialNumber map[string]interface{} `json:"serialNumber,omitempty"`
	CurrentProfileName map[string]interface{} `json:"currentProfileName,omitempty"`
	HardwareInfo map[string]interface{} `json:"hardwareInfo,omitempty"`
	IpAddress map[string]interface{} `json:"ipAddress,omitempty"`
	BatteryLevel map[string]interface{} `json:"batteryLevel,omitempty"`
	OccipitalDeviceInfo map[string]interface{} `json:"occipitalDeviceInfo,omitempty"`
	OutputCapabilities []map[string]interface{} `json:"outputCapabilities,omitempty"`
	RobotVersion map[string]interface{} `json:"robotVersion,omitempty"`
	SensoryServiceAppVersion map[string]interface{} `json:"sensoryServiceAppVersion,omitempty"`
	WindowsOSVersion map[string]interface{} `json:"windowsOSVersion,omitempty"`
	SensorCapabilities []map[string]interface{} `json:"sensorCapabilities,omitempty"`
}