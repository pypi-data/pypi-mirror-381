# FunctionCallingConfig

Configuration for specifying function calling behavior.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **int** | Optional. Specifies the mode in which function calling should execute. If  unspecified, the default value will be set to AUTO. | [optional] 
**allowed_function_names** | **List[str]** | Optional. A set of function names that, when provided, limits the functions  the model will call.   This should only be set when the Mode is ANY. Function names  should match [FunctionDeclaration.name]. With mode set to ANY, model will  predict a function call from the set of function names provided. | [optional] 

## Example

```python
from openapi_client.models.function_calling_config import FunctionCallingConfig

# TODO update the JSON string below
json = "{}"
# create an instance of FunctionCallingConfig from a JSON string
function_calling_config_instance = FunctionCallingConfig.from_json(json)
# print the JSON string representation of the object
print(FunctionCallingConfig.to_json())

# convert the object into a dict
function_calling_config_dict = function_calling_config_instance.to_dict()
# create an instance of FunctionCallingConfig from a dict
function_calling_config_from_dict = FunctionCallingConfig.from_dict(function_calling_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


