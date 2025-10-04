# BatchEmbedContentsRequest

Batch request to get embeddings from the model for a list of prompts.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | **str** | Required. The model&#39;s resource name. This serves as an ID for the Model to  use.   This name should match a model name returned by the &#x60;ListModels&#x60; method.   Format: &#x60;models/{model}&#x60; | 
**requests** | [**List[EmbedContentRequest]**](EmbedContentRequest.md) | Required. Embed requests for the batch. The model in each of these requests  must match the model specified &#x60;BatchEmbedContentsRequest.model&#x60;. | 

## Example

```python
from openapi_client.models.batch_embed_contents_request import BatchEmbedContentsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BatchEmbedContentsRequest from a JSON string
batch_embed_contents_request_instance = BatchEmbedContentsRequest.from_json(json)
# print the JSON string representation of the object
print(BatchEmbedContentsRequest.to_json())

# convert the object into a dict
batch_embed_contents_request_dict = batch_embed_contents_request_instance.to_dict()
# create an instance of BatchEmbedContentsRequest from a dict
batch_embed_contents_request_from_dict = BatchEmbedContentsRequest.from_dict(batch_embed_contents_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


