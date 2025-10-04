# MultiSpeakerVoiceConfig

The configuration for the multi-speaker setup.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**speaker_voice_configs** | [**List[SpeakerVoiceConfig]**](SpeakerVoiceConfig.md) | Required. All the enabled speaker voices. | 

## Example

```python
from openapi_client.models.multi_speaker_voice_config import MultiSpeakerVoiceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of MultiSpeakerVoiceConfig from a JSON string
multi_speaker_voice_config_instance = MultiSpeakerVoiceConfig.from_json(json)
# print the JSON string representation of the object
print(MultiSpeakerVoiceConfig.to_json())

# convert the object into a dict
multi_speaker_voice_config_dict = multi_speaker_voice_config_instance.to_dict()
# create an instance of MultiSpeakerVoiceConfig from a dict
multi_speaker_voice_config_from_dict = MultiSpeakerVoiceConfig.from_dict(multi_speaker_voice_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


