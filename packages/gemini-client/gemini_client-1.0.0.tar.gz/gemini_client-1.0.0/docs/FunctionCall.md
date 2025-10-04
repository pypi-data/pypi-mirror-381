# FunctionCall

A predicted `FunctionCall` returned from the model that contains  a string representing the `FunctionDeclaration.name` with the  arguments and their values.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Optional. The unique id of the function call. If populated, the client to  execute the &#x60;function_call&#x60; and return the response with the matching &#x60;id&#x60;. | [optional] 
**name** | **str** | Required. The name of the function to call.  Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum  length of 63. | 
**args** | **object** | Optional. The function parameters and values in JSON object format. | [optional] 

## Example

```python
from openapi_client.models.function_call import FunctionCall

# TODO update the JSON string below
json = "{}"
# create an instance of FunctionCall from a JSON string
function_call_instance = FunctionCall.from_json(json)
# print the JSON string representation of the object
print(FunctionCall.to_json())

# convert the object into a dict
function_call_dict = function_call_instance.to_dict()
# create an instance of FunctionCall from a dict
function_call_from_dict = FunctionCall.from_dict(function_call_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


