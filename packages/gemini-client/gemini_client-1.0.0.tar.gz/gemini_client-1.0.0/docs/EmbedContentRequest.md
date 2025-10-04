# EmbedContentRequest

Request containing the `Content` for the model to embed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | **str** | Required. The model&#39;s resource name. This serves as an ID for the Model to  use.   This name should match a model name returned by the &#x60;ListModels&#x60; method.   Format: &#x60;models/{model}&#x60; | 
**content** | [**Content**](Content.md) | Required. The content to embed. Only the &#x60;parts.text&#x60; fields will be  counted. | 
**task_type** | **int** | Optional. Optional task type for which the embeddings will be used. Not  supported on earlier models (&#x60;models/embedding-001&#x60;). | [optional] 
**title** | **str** | Optional. An optional title for the text. Only applicable when TaskType is  &#x60;RETRIEVAL_DOCUMENT&#x60;.   Note: Specifying a &#x60;title&#x60; for &#x60;RETRIEVAL_DOCUMENT&#x60; provides better quality  embeddings for retrieval. | [optional] 
**output_dimensionality** | **int** | Optional. Optional reduced dimension for the output embedding. If set,  excessive values in the output embedding are truncated from the end.  Supported by newer models since 2024 only. You cannot set this value if  using the earlier model (&#x60;models/embedding-001&#x60;). | [optional] 

## Example

```python
from openapi_client.models.embed_content_request import EmbedContentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EmbedContentRequest from a JSON string
embed_content_request_instance = EmbedContentRequest.from_json(json)
# print the JSON string representation of the object
print(EmbedContentRequest.to_json())

# convert the object into a dict
embed_content_request_dict = embed_content_request_instance.to_dict()
# create an instance of EmbedContentRequest from a dict
embed_content_request_from_dict = EmbedContentRequest.from_dict(embed_content_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


