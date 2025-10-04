# GroundingAttribution

Attribution for a source that contributed to an answer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_id** | [**AttributionSourceId**](AttributionSourceId.md) | Output only. Identifier for the source contributing to this attribution. | [optional] [readonly] 
**content** | [**Content**](Content.md) | Grounding source content that makes up this attribution. | [optional] 

## Example

```python
from openapi_client.models.grounding_attribution import GroundingAttribution

# TODO update the JSON string below
json = "{}"
# create an instance of GroundingAttribution from a JSON string
grounding_attribution_instance = GroundingAttribution.from_json(json)
# print the JSON string representation of the object
print(GroundingAttribution.to_json())

# convert the object into a dict
grounding_attribution_dict = grounding_attribution_instance.to_dict()
# create an instance of GroundingAttribution from a dict
grounding_attribution_from_dict = GroundingAttribution.from_dict(grounding_attribution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


