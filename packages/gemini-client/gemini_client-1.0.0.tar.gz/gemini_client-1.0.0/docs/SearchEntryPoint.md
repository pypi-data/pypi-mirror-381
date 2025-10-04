# SearchEntryPoint

Google search entry point.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rendered_content** | **str** | Optional. Web content snippet that can be embedded in a web page or an app  webview. | [optional] 
**sdk_blob** | **str** | Optional. Base64 encoded JSON representing array of &lt;search term, search  url&gt; tuple. | [optional] 

## Example

```python
from openapi_client.models.search_entry_point import SearchEntryPoint

# TODO update the JSON string below
json = "{}"
# create an instance of SearchEntryPoint from a JSON string
search_entry_point_instance = SearchEntryPoint.from_json(json)
# print the JSON string representation of the object
print(SearchEntryPoint.to_json())

# convert the object into a dict
search_entry_point_dict = search_entry_point_instance.to_dict()
# create an instance of SearchEntryPoint from a dict
search_entry_point_from_dict = SearchEntryPoint.from_dict(search_entry_point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


