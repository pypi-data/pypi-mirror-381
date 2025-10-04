# ThinkingConfig

Config for thinking features.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_thoughts** | **bool** | Indicates whether to include thoughts in the response.  If true, thoughts are returned only when available. | [optional] 
**thinking_budget** | **int** | The number of thoughts tokens that the model should generate. | [optional] 

## Example

```python
from openapi_client.models.thinking_config import ThinkingConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ThinkingConfig from a JSON string
thinking_config_instance = ThinkingConfig.from_json(json)
# print the JSON string representation of the object
print(ThinkingConfig.to_json())

# convert the object into a dict
thinking_config_dict = thinking_config_instance.to_dict()
# create an instance of ThinkingConfig from a dict
thinking_config_from_dict = ThinkingConfig.from_dict(thinking_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


