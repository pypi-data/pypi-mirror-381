# EmbedContentResponse

The response to an `EmbedContentRequest`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embedding** | [**ContentEmbedding**](ContentEmbedding.md) | Output only. The embedding generated from the input content. | [optional] [readonly] 

## Example

```python
from openapi_client.models.embed_content_response import EmbedContentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EmbedContentResponse from a JSON string
embed_content_response_instance = EmbedContentResponse.from_json(json)
# print the JSON string representation of the object
print(EmbedContentResponse.to_json())

# convert the object into a dict
embed_content_response_dict = embed_content_response_instance.to_dict()
# create an instance of EmbedContentResponse from a dict
embed_content_response_from_dict = EmbedContentResponse.from_dict(embed_content_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


