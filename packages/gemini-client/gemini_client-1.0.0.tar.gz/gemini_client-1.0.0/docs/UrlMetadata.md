# UrlMetadata

Context of the a single url retrieval.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**retrieved_url** | **str** | Retrieved url by the tool. | [optional] 
**url_retrieval_status** | **int** | Status of the url retrieval. | [optional] 

## Example

```python
from openapi_client.models.url_metadata import UrlMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of UrlMetadata from a JSON string
url_metadata_instance = UrlMetadata.from_json(json)
# print the JSON string representation of the object
print(UrlMetadata.to_json())

# convert the object into a dict
url_metadata_dict = url_metadata_instance.to_dict()
# create an instance of UrlMetadata from a dict
url_metadata_from_dict = UrlMetadata.from_dict(url_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


