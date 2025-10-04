# Blob

Raw media bytes.   Text should not be sent as raw bytes, use the 'text' field.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mime_type** | **str** | The IANA standard MIME type of the source data.  Examples:    - image/png    - image/jpeg  If an unsupported MIME type is provided, an error will be returned. For a  complete list of supported types, see [Supported file  formats](https://ai.google.dev/gemini-api/docs/prompting_with_media#supported_file_formats). | [optional] 
**data** | **str** | Raw bytes for media formats. | [optional] 

## Example

```python
from openapi_client.models.blob import Blob

# TODO update the JSON string below
json = "{}"
# create an instance of Blob from a JSON string
blob_instance = Blob.from_json(json)
# print the JSON string representation of the object
print(Blob.to_json())

# convert the object into a dict
blob_dict = blob_instance.to_dict()
# create an instance of Blob from a dict
blob_from_dict = Blob.from_dict(blob_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


