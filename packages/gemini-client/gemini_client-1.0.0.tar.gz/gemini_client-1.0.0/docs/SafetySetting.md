# SafetySetting

Safety setting, affecting the safety-blocking behavior.   Passing a safety setting for a category changes the allowed probability that  content is blocked.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **int** | Required. The category for this setting. | 
**threshold** | **int** | Required. Controls the probability threshold at which harm is blocked. | 

## Example

```python
from openapi_client.models.safety_setting import SafetySetting

# TODO update the JSON string below
json = "{}"
# create an instance of SafetySetting from a JSON string
safety_setting_instance = SafetySetting.from_json(json)
# print the JSON string representation of the object
print(SafetySetting.to_json())

# convert the object into a dict
safety_setting_dict = safety_setting_instance.to_dict()
# create an instance of SafetySetting from a dict
safety_setting_from_dict = SafetySetting.from_dict(safety_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


