# PrebuiltVoiceConfig

The configuration for the prebuilt speaker to use.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**voice_name** | **str** | The name of the preset voice to use. | [optional] 

## Example

```python
from openapi_client.models.prebuilt_voice_config import PrebuiltVoiceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of PrebuiltVoiceConfig from a JSON string
prebuilt_voice_config_instance = PrebuiltVoiceConfig.from_json(json)
# print the JSON string representation of the object
print(PrebuiltVoiceConfig.to_json())

# convert the object into a dict
prebuilt_voice_config_dict = prebuilt_voice_config_instance.to_dict()
# create an instance of PrebuiltVoiceConfig from a dict
prebuilt_voice_config_from_dict = PrebuiltVoiceConfig.from_dict(prebuilt_voice_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


