# GoogleSearchRetrieval

Tool to retrieve public web data for grounding, powered by Google.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dynamic_retrieval_config** | [**DynamicRetrievalConfig**](DynamicRetrievalConfig.md) | Specifies the dynamic retrieval configuration for the given source. | [optional] 

## Example

```python
from openapi_client.models.google_search_retrieval import GoogleSearchRetrieval

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleSearchRetrieval from a JSON string
google_search_retrieval_instance = GoogleSearchRetrieval.from_json(json)
# print the JSON string representation of the object
print(GoogleSearchRetrieval.to_json())

# convert the object into a dict
google_search_retrieval_dict = google_search_retrieval_instance.to_dict()
# create an instance of GoogleSearchRetrieval from a dict
google_search_retrieval_from_dict = GoogleSearchRetrieval.from_dict(google_search_retrieval_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


