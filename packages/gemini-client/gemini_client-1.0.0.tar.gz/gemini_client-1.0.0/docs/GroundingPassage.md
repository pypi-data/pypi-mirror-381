# GroundingPassage

Passage included inline with a grounding configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifier for the passage for attributing this passage in grounded  answers. | [optional] 
**content** | [**Content**](Content.md) | Content of the passage. | [optional] 

## Example

```python
from openapi_client.models.grounding_passage import GroundingPassage

# TODO update the JSON string below
json = "{}"
# create an instance of GroundingPassage from a JSON string
grounding_passage_instance = GroundingPassage.from_json(json)
# print the JSON string representation of the object
print(GroundingPassage.to_json())

# convert the object into a dict
grounding_passage_dict = grounding_passage_instance.to_dict()
# create an instance of GroundingPassage from a dict
grounding_passage_from_dict = GroundingPassage.from_dict(grounding_passage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


