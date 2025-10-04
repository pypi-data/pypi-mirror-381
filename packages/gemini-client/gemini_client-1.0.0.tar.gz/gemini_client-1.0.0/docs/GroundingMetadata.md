# GroundingMetadata

Metadata returned to client when grounding is enabled.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search_entry_point** | [**SearchEntryPoint**](SearchEntryPoint.md) | Optional. Google search entry for the following-up web searches. | [optional] 
**grounding_chunks** | [**List[GroundingChunk]**](GroundingChunk.md) | List of supporting references retrieved from specified grounding source. | [optional] 
**grounding_supports** | [**List[GroundingSupport]**](GroundingSupport.md) | List of grounding support. | [optional] 
**retrieval_metadata** | [**RetrievalMetadata**](RetrievalMetadata.md) | Metadata related to retrieval in the grounding flow. | [optional] 
**web_search_queries** | **List[str]** | Web search queries for the following-up web search. | [optional] 

## Example

```python
from openapi_client.models.grounding_metadata import GroundingMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of GroundingMetadata from a JSON string
grounding_metadata_instance = GroundingMetadata.from_json(json)
# print the JSON string representation of the object
print(GroundingMetadata.to_json())

# convert the object into a dict
grounding_metadata_dict = grounding_metadata_instance.to_dict()
# create an instance of GroundingMetadata from a dict
grounding_metadata_from_dict = GroundingMetadata.from_dict(grounding_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


