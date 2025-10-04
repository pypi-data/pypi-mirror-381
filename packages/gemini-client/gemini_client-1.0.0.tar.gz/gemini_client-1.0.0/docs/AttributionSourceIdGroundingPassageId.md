# AttributionSourceIdGroundingPassageId

Identifier for a part within a `GroundingPassage`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**passage_id** | **str** | Output only. ID of the passage matching the &#x60;GenerateAnswerRequest&#x60;&#39;s  &#x60;GroundingPassage.id&#x60;. | [optional] [readonly] 
**part_index** | **int** | Output only. Index of the part within the &#x60;GenerateAnswerRequest&#x60;&#39;s  &#x60;GroundingPassage.content&#x60;. | [optional] [readonly] 

## Example

```python
from openapi_client.models.attribution_source_id_grounding_passage_id import AttributionSourceIdGroundingPassageId

# TODO update the JSON string below
json = "{}"
# create an instance of AttributionSourceIdGroundingPassageId from a JSON string
attribution_source_id_grounding_passage_id_instance = AttributionSourceIdGroundingPassageId.from_json(json)
# print the JSON string representation of the object
print(AttributionSourceIdGroundingPassageId.to_json())

# convert the object into a dict
attribution_source_id_grounding_passage_id_dict = attribution_source_id_grounding_passage_id_instance.to_dict()
# create an instance of AttributionSourceIdGroundingPassageId from a dict
attribution_source_id_grounding_passage_id_from_dict = AttributionSourceIdGroundingPassageId.from_dict(attribution_source_id_grounding_passage_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


