# BatchEmbedContentsResponse

The response to a `BatchEmbedContentsRequest`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embeddings** | [**List[ContentEmbedding]**](ContentEmbedding.md) | Output only. The embeddings for each request, in the same order as provided  in the batch request. | [optional] [readonly] 

## Example

```python
from openapi_client.models.batch_embed_contents_response import BatchEmbedContentsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BatchEmbedContentsResponse from a JSON string
batch_embed_contents_response_instance = BatchEmbedContentsResponse.from_json(json)
# print the JSON string representation of the object
print(BatchEmbedContentsResponse.to_json())

# convert the object into a dict
batch_embed_contents_response_dict = batch_embed_contents_response_instance.to_dict()
# create an instance of BatchEmbedContentsResponse from a dict
batch_embed_contents_response_from_dict = BatchEmbedContentsResponse.from_dict(batch_embed_contents_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


