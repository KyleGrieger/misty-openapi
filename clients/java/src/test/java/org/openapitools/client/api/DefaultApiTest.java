/*
 * Misty API
 * Misty Open API
 *
 * The version of the OpenAPI document: 1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.InlineObject;
import org.openapitools.client.model.InlineObject1;
import org.openapitools.client.model.InlineObject2;
import org.openapitools.client.model.InlineObject3;
import org.openapitools.client.model.InlineResponse200;
import org.openapitools.client.model.InlineResponse2001;
import org.junit.Test;
import org.junit.Ignore;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for DefaultApi
 */
@Ignore
public class DefaultApiTest {

    private final DefaultApi api = new DefaultApi();

    
    /**
     * Drive
     *
     * Drive
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void driveTest() throws ApiException {
        Object linearVelocity = null;
        Object angularVelocity = null;
        InlineObject inlineObject = null;
        List<InlineResponse200> response = api.drive(linearVelocity, angularVelocity, inlineObject);

        // TODO: test validations
    }
    
    /**
     * Drive Heading
     *
     * Drive Heading
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void driveHeadingTest() throws ApiException {
        Object heading = null;
        Object distance = null;
        Object timeMS = null;
        InlineObject2 inlineObject2 = null;
        List<InlineResponse2001> response = api.driveHeading(heading, distance, timeMS, inlineObject2);

        // TODO: test validations
    }
    
    /**
     * Drive Time
     *
     * Drive Time
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void driveTimeTest() throws ApiException {
        Object linearVelocity = null;
        Object angularVelocity = null;
        Object timeMS = null;
        InlineObject3 inlineObject3 = null;
        List<InlineResponse200> response = api.driveTime(linearVelocity, angularVelocity, timeMS, inlineObject3);

        // TODO: test validations
    }
    
    /**
     * Drive Track
     *
     * Drive Track
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void driveTrackTest() throws ApiException {
        Object rightTrackSpeed = null;
        Object leftTrackSpeed = null;
        InlineObject1 inlineObject1 = null;
        List<InlineResponse200> response = api.driveTrack(rightTrackSpeed, leftTrackSpeed, inlineObject1);

        // TODO: test validations
    }
    
    /**
     * Get Device Information
     *
     * Get Device Information
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void getDeviceInformationTest() throws ApiException {
        List<InlineResponse2001> response = api.getDeviceInformation();

        // TODO: test validations
    }
    
    /**
     * Stop
     *
     * Stop
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void stopTest() throws ApiException {
        List<InlineResponse200> response = api.stop();

        // TODO: test validations
    }
    
}
