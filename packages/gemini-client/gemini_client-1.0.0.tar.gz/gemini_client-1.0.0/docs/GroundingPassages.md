# GroundingPassages

A repeated list of passages.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**passages** | [**List[GroundingPassage]**](GroundingPassage.md) | List of passages. | [optional] 

## Example

```python
from openapi_client.models.grounding_passages import GroundingPassages

# TODO update the JSON string below
json = "{}"
# create an instance of GroundingPassages from a JSON string
grounding_passages_instance = GroundingPassages.from_json(json)
# print the JSON string representation of the object
print(GroundingPassages.to_json())

# convert the object into a dict
grounding_passages_dict = grounding_passages_instance.to_dict()
# create an instance of GroundingPassages from a dict
grounding_passages_from_dict = GroundingPassages.from_dict(grounding_passages_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


