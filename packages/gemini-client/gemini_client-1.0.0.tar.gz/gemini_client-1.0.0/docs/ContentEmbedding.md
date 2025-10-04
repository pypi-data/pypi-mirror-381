# ContentEmbedding

A list of floats representing an embedding.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | **List[float]** | The embedding values. | [optional] 

## Example

```python
from openapi_client.models.content_embedding import ContentEmbedding

# TODO update the JSON string below
json = "{}"
# create an instance of ContentEmbedding from a JSON string
content_embedding_instance = ContentEmbedding.from_json(json)
# print the JSON string representation of the object
print(ContentEmbedding.to_json())

# convert the object into a dict
content_embedding_dict = content_embedding_instance.to_dict()
# create an instance of ContentEmbedding from a dict
content_embedding_from_dict = ContentEmbedding.from_dict(content_embedding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


