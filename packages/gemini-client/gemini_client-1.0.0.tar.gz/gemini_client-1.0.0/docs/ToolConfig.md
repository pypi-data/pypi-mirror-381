# ToolConfig

The Tool configuration containing parameters for specifying `Tool` use  in the request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**function_calling_config** | [**FunctionCallingConfig**](FunctionCallingConfig.md) | Optional. Function calling config. | [optional] 

## Example

```python
from openapi_client.models.tool_config import ToolConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ToolConfig from a JSON string
tool_config_instance = ToolConfig.from_json(json)
# print the JSON string representation of the object
print(ToolConfig.to_json())

# convert the object into a dict
tool_config_dict = tool_config_instance.to_dict()
# create an instance of ToolConfig from a dict
tool_config_from_dict = ToolConfig.from_dict(tool_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


