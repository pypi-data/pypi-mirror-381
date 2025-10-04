# MetadataFilter

User provided filter to limit retrieval based on `Chunk` or `Document` level  metadata values.  Example (genre = drama OR genre = action):    key = \"document.custom_metadata.genre\"    conditions = [{string_value = \"drama\", operation = EQUAL},                  {string_value = \"action\", operation = EQUAL}]

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Required. The key of the metadata to filter on. | 
**conditions** | [**List[Condition]**](Condition.md) | Required. The &#x60;Condition&#x60;s for the given key that will trigger this filter.  Multiple &#x60;Condition&#x60;s are joined by logical ORs. | 

## Example

```python
from openapi_client.models.metadata_filter import MetadataFilter

# TODO update the JSON string below
json = "{}"
# create an instance of MetadataFilter from a JSON string
metadata_filter_instance = MetadataFilter.from_json(json)
# print the JSON string representation of the object
print(MetadataFilter.to_json())

# convert the object into a dict
metadata_filter_dict = metadata_filter_instance.to_dict()
# create an instance of MetadataFilter from a dict
metadata_filter_from_dict = MetadataFilter.from_dict(metadata_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


