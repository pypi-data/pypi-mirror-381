# GroundingChunk

Grounding chunk.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**web** | [**GroundingChunkWeb**](GroundingChunkWeb.md) | Grounding chunk from the web. | [optional] 

## Example

```python
from openapi_client.models.grounding_chunk import GroundingChunk

# TODO update the JSON string below
json = "{}"
# create an instance of GroundingChunk from a JSON string
grounding_chunk_instance = GroundingChunk.from_json(json)
# print the JSON string representation of the object
print(GroundingChunk.to_json())

# convert the object into a dict
grounding_chunk_dict = grounding_chunk_instance.to_dict()
# create an instance of GroundingChunk from a dict
grounding_chunk_from_dict = GroundingChunk.from_dict(grounding_chunk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


