# GroundingSupport

Grounding support.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**segment** | [**Segment**](Segment.md) | Segment of the content this support belongs to. | [optional] 
**grounding_chunk_indices** | **List[int]** | A list of indices (into &#39;grounding_chunk&#39;) specifying the  citations associated with the claim. For instance [1,3,4] means  that grounding_chunk[1], grounding_chunk[3],  grounding_chunk[4] are the retrieved content attributed to the claim. | [optional] 
**confidence_scores** | **List[float]** | Confidence score of the support references. Ranges from 0 to 1. 1 is the  most confident. This list must have the same size as the  grounding_chunk_indices. | [optional] 

## Example

```python
from openapi_client.models.grounding_support import GroundingSupport

# TODO update the JSON string below
json = "{}"
# create an instance of GroundingSupport from a JSON string
grounding_support_instance = GroundingSupport.from_json(json)
# print the JSON string representation of the object
print(GroundingSupport.to_json())

# convert the object into a dict
grounding_support_dict = grounding_support_instance.to_dict()
# create an instance of GroundingSupport from a dict
grounding_support_from_dict = GroundingSupport.from_dict(grounding_support_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


