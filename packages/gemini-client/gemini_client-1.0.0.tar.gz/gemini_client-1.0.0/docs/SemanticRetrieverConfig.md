# SemanticRetrieverConfig

Configuration for retrieving grounding content from a `Corpus` or  `Document` created using the Semantic Retriever API.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** | Required. Name of the resource for retrieval. Example: &#x60;corpora/123&#x60; or  &#x60;corpora/123/documents/abc&#x60;. | 
**query** | [**Content**](Content.md) | Required. Query to use for matching &#x60;Chunk&#x60;s in the given resource by  similarity. | 
**metadata_filters** | [**List[MetadataFilter]**](MetadataFilter.md) | Optional. Filters for selecting &#x60;Document&#x60;s and/or &#x60;Chunk&#x60;s from the  resource. | [optional] 
**max_chunks_count** | **int** | Optional. Maximum number of relevant &#x60;Chunk&#x60;s to retrieve. | [optional] 
**minimum_relevance_score** | **float** | Optional. Minimum relevance score for retrieved relevant &#x60;Chunk&#x60;s. | [optional] 

## Example

```python
from openapi_client.models.semantic_retriever_config import SemanticRetrieverConfig

# TODO update the JSON string below
json = "{}"
# create an instance of SemanticRetrieverConfig from a JSON string
semantic_retriever_config_instance = SemanticRetrieverConfig.from_json(json)
# print the JSON string representation of the object
print(SemanticRetrieverConfig.to_json())

# convert the object into a dict
semantic_retriever_config_dict = semantic_retriever_config_instance.to_dict()
# create an instance of SemanticRetrieverConfig from a dict
semantic_retriever_config_from_dict = SemanticRetrieverConfig.from_dict(semantic_retriever_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


