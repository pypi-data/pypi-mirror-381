# AttributionSourceId

Identifier for the source contributing to this attribution.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grounding_passage** | [**AttributionSourceIdGroundingPassageId**](AttributionSourceIdGroundingPassageId.md) | Identifier for an inline passage. | [optional] 
**semantic_retriever_chunk** | [**AttributionSourceIdSemanticRetrieverChunk**](AttributionSourceIdSemanticRetrieverChunk.md) | Identifier for a &#x60;Chunk&#x60; fetched via Semantic Retriever. | [optional] 

## Example

```python
from openapi_client.models.attribution_source_id import AttributionSourceId

# TODO update the JSON string below
json = "{}"
# create an instance of AttributionSourceId from a JSON string
attribution_source_id_instance = AttributionSourceId.from_json(json)
# print the JSON string representation of the object
print(AttributionSourceId.to_json())

# convert the object into a dict
attribution_source_id_dict = attribution_source_id_instance.to_dict()
# create an instance of AttributionSourceId from a dict
attribution_source_id_from_dict = AttributionSourceId.from_dict(attribution_source_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


