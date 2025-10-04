# VoiceConfig

The configuration for the voice to use.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prebuilt_voice_config** | [**PrebuiltVoiceConfig**](PrebuiltVoiceConfig.md) | The configuration for the prebuilt voice to use. | [optional] 

## Example

```python
from openapi_client.models.voice_config import VoiceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of VoiceConfig from a JSON string
voice_config_instance = VoiceConfig.from_json(json)
# print the JSON string representation of the object
print(VoiceConfig.to_json())

# convert the object into a dict
voice_config_dict = voice_config_instance.to_dict()
# create an instance of VoiceConfig from a dict
voice_config_from_dict = VoiceConfig.from_dict(voice_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


