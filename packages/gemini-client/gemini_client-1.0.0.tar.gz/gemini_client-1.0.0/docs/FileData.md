# FileData

URI based data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mime_type** | **str** | Optional. The IANA standard MIME type of the source data. | [optional] 
**file_uri** | **str** | Required. URI. | 

## Example

```python
from openapi_client.models.file_data import FileData

# TODO update the JSON string below
json = "{}"
# create an instance of FileData from a JSON string
file_data_instance = FileData.from_json(json)
# print the JSON string representation of the object
print(FileData.to_json())

# convert the object into a dict
file_data_dict = file_data_instance.to_dict()
# create an instance of FileData from a dict
file_data_from_dict = FileData.from_dict(file_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


