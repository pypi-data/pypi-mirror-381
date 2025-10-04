# ModalityTokenCount

Represents token counting info for a single modality.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**modality** | **int** | The modality associated with this token count. | [optional] 
**token_count** | **int** | Number of tokens. | [optional] 

## Example

```python
from openapi_client.models.modality_token_count import ModalityTokenCount

# TODO update the JSON string below
json = "{}"
# create an instance of ModalityTokenCount from a JSON string
modality_token_count_instance = ModalityTokenCount.from_json(json)
# print the JSON string representation of the object
print(ModalityTokenCount.to_json())

# convert the object into a dict
modality_token_count_dict = modality_token_count_instance.to_dict()
# create an instance of ModalityTokenCount from a dict
modality_token_count_from_dict = ModalityTokenCount.from_dict(modality_token_count_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


