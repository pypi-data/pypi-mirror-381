# GroundingChunkWeb

Chunk from the web.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uri** | **str** | URI reference of the chunk. | [optional] 
**title** | **str** | Title of the chunk. | [optional] 

## Example

```python
from openapi_client.models.grounding_chunk_web import GroundingChunkWeb

# TODO update the JSON string below
json = "{}"
# create an instance of GroundingChunkWeb from a JSON string
grounding_chunk_web_instance = GroundingChunkWeb.from_json(json)
# print the JSON string representation of the object
print(GroundingChunkWeb.to_json())

# convert the object into a dict
grounding_chunk_web_dict = grounding_chunk_web_instance.to_dict()
# create an instance of GroundingChunkWeb from a dict
grounding_chunk_web_from_dict = GroundingChunkWeb.from_dict(grounding_chunk_web_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


