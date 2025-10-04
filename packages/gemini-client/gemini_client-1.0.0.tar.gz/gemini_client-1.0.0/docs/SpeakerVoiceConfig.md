# SpeakerVoiceConfig

The configuration for a single speaker in a multi speaker setup.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**speaker** | **str** | Required. The name of the speaker to use. Should be the same as in the  prompt. | 
**voice_config** | [**VoiceConfig**](VoiceConfig.md) | Required. The configuration for the voice to use. | 

## Example

```python
from openapi_client.models.speaker_voice_config import SpeakerVoiceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of SpeakerVoiceConfig from a JSON string
speaker_voice_config_instance = SpeakerVoiceConfig.from_json(json)
# print the JSON string representation of the object
print(SpeakerVoiceConfig.to_json())

# convert the object into a dict
speaker_voice_config_dict = speaker_voice_config_instance.to_dict()
# create an instance of SpeakerVoiceConfig from a dict
speaker_voice_config_from_dict = SpeakerVoiceConfig.from_dict(speaker_voice_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


