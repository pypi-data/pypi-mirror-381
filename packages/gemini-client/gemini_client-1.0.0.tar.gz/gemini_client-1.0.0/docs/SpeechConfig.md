# SpeechConfig

The speech generation config.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**voice_config** | [**VoiceConfig**](VoiceConfig.md) | The configuration in case of single-voice output. | [optional] 
**multi_speaker_voice_config** | [**MultiSpeakerVoiceConfig**](MultiSpeakerVoiceConfig.md) | Optional. The configuration for the multi-speaker setup.  It is mutually exclusive with the voice_config field. | [optional] 
**language_code** | **str** | Optional. Language code (in BCP 47 format, e.g. \&quot;en-US\&quot;) for speech  synthesis.   Valid values are: de-DE, en-AU, en-GB, en-IN, en-US, es-US, fr-FR, hi-IN,  pt-BR, ar-XA, es-ES, fr-CA, id-ID, it-IT, ja-JP, tr-TR, vi-VN, bn-IN,  gu-IN, kn-IN, ml-IN, mr-IN, ta-IN, te-IN, nl-NL, ko-KR, cmn-CN, pl-PL,  ru-RU, and th-TH. | [optional] 

## Example

```python
from openapi_client.models.speech_config import SpeechConfig

# TODO update the JSON string below
json = "{}"
# create an instance of SpeechConfig from a JSON string
speech_config_instance = SpeechConfig.from_json(json)
# print the JSON string representation of the object
print(SpeechConfig.to_json())

# convert the object into a dict
speech_config_dict = speech_config_instance.to_dict()
# create an instance of SpeechConfig from a dict
speech_config_from_dict = SpeechConfig.from_dict(speech_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


