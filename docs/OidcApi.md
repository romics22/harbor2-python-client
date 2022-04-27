# swagger_client.OidcApi

All URIs are relative to *http://rmiharbor.ch/api/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ping_oidc**](OidcApi.md#ping_oidc) | **POST** /system/oidc/ping | Test the OIDC endpoint.


# **ping_oidc**
> ping_oidc(endpoint, x_request_id=x_request_id)

Test the OIDC endpoint.

Test the OIDC endpoint, the setting of the endpoint is provided in the request.  This API can only be called by system admin. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.OidcApi(swagger_client.ApiClient(configuration))
endpoint = swagger_client.Endpoint() # Endpoint | Request body for OIDC endpoint to be tested.
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Test the OIDC endpoint.
    api_instance.ping_oidc(endpoint, x_request_id=x_request_id)
except ApiException as e:
    print("Exception when calling OidcApi->ping_oidc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint** | [**Endpoint**](Endpoint.md)| Request body for OIDC endpoint to be tested. | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

