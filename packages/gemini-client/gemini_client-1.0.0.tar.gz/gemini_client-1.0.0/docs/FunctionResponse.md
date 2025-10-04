# FunctionResponse

The result output from a `FunctionCall` that contains a string  representing the `FunctionDeclaration.name` and a structured JSON  object containing any output from the function is used as context to  the model. This should contain the result of a`FunctionCall` made  based on model prediction.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Optional. The id of the function call this response is for. Populated by  the client to match the corresponding function call &#x60;id&#x60;. | [optional] 
**name** | **str** | Required. The name of the function to call.  Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum  length of 63. | 
**response** | **object** | Required. The function response in JSON object format. | 
**will_continue** | **bool** | Optional. Signals that function call continues, and more responses will be  returned, turning the function call into a generator.  Is only applicable to NON_BLOCKING function calls, is ignored otherwise.  If set to false, future responses will not be considered.  It is allowed to return empty &#x60;response&#x60; with &#x60;will_continue&#x3D;False&#x60; to  signal that the function call is finished. This may still trigger the model  generation. To avoid triggering the generation and finish the function  call, additionally set &#x60;scheduling&#x60; to &#x60;SILENT&#x60;. | [optional] 
**scheduling** | **int** | Optional. Specifies how the response should be scheduled in the  conversation. Only applicable to NON_BLOCKING function calls, is ignored  otherwise. Defaults to WHEN_IDLE. | [optional] 

## Example

```python
from openapi_client.models.function_response import FunctionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FunctionResponse from a JSON string
function_response_instance = FunctionResponse.from_json(json)
# print the JSON string representation of the object
print(FunctionResponse.to_json())

# convert the object into a dict
function_response_dict = function_response_instance.to_dict()
# create an instance of FunctionResponse from a dict
function_response_from_dict = FunctionResponse.from_dict(function_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


