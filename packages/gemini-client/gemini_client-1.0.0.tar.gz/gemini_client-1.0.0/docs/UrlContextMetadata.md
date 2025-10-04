# UrlContextMetadata

Metadata related to url context retrieval tool.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url_metadata** | [**List[UrlMetadata]**](UrlMetadata.md) | List of url context. | [optional] 

## Example

```python
from openapi_client.models.url_context_metadata import UrlContextMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of UrlContextMetadata from a JSON string
url_context_metadata_instance = UrlContextMetadata.from_json(json)
# print the JSON string representation of the object
print(UrlContextMetadata.to_json())

# convert the object into a dict
url_context_metadata_dict = url_context_metadata_instance.to_dict()
# create an instance of UrlContextMetadata from a dict
url_context_metadata_from_dict = UrlContextMetadata.from_dict(url_context_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


