# ToolGoogleSearch

GoogleSearch tool type.  Tool to support Google Search in Model. Powered by Google.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_range_filter** | [**Interval**](Interval.md) | Optional. Filter search results to a specific time range.  If customers set a start time, they must set an end time (and vice  versa). | [optional] 

## Example

```python
from openapi_client.models.tool_google_search import ToolGoogleSearch

# TODO update the JSON string below
json = "{}"
# create an instance of ToolGoogleSearch from a JSON string
tool_google_search_instance = ToolGoogleSearch.from_json(json)
# print the JSON string representation of the object
print(ToolGoogleSearch.to_json())

# convert the object into a dict
tool_google_search_dict = tool_google_search_instance.to_dict()
# create an instance of ToolGoogleSearch from a dict
tool_google_search_from_dict = ToolGoogleSearch.from_dict(tool_google_search_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


