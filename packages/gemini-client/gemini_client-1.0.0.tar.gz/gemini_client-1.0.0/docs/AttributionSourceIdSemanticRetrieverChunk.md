# AttributionSourceIdSemanticRetrieverChunk

Identifier for a `Chunk` retrieved via Semantic Retriever specified in the  `GenerateAnswerRequest` using `SemanticRetrieverConfig`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** | Output only. Name of the source matching the request&#39;s  &#x60;SemanticRetrieverConfig.source&#x60;. Example: &#x60;corpora/123&#x60; or  &#x60;corpora/123/documents/abc&#x60; | [optional] [readonly] 
**chunk** | **str** | Output only. Name of the &#x60;Chunk&#x60; containing the attributed text.  Example: &#x60;corpora/123/documents/abc/chunks/xyz&#x60; | [optional] [readonly] 

## Example

```python
from openapi_client.models.attribution_source_id_semantic_retriever_chunk import AttributionSourceIdSemanticRetrieverChunk

# TODO update the JSON string below
json = "{}"
# create an instance of AttributionSourceIdSemanticRetrieverChunk from a JSON string
attribution_source_id_semantic_retriever_chunk_instance = AttributionSourceIdSemanticRetrieverChunk.from_json(json)
# print the JSON string representation of the object
print(AttributionSourceIdSemanticRetrieverChunk.to_json())

# convert the object into a dict
attribution_source_id_semantic_retriever_chunk_dict = attribution_source_id_semantic_retriever_chunk_instance.to_dict()
# create an instance of AttributionSourceIdSemanticRetrieverChunk from a dict
attribution_source_id_semantic_retriever_chunk_from_dict = AttributionSourceIdSemanticRetrieverChunk.from_dict(attribution_source_id_semantic_retriever_chunk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


