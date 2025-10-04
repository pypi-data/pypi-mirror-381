# CitationSource

A citation to a source for a portion of a specific response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_index** | **int** | Optional. Start of segment of the response that is attributed to this  source.   Index indicates the start of the segment, measured in bytes. | [optional] 
**end_index** | **int** | Optional. End of the attributed segment, exclusive. | [optional] 
**uri** | **str** | Optional. URI that is attributed as a source for a portion of the text. | [optional] 
**license** | **str** | Optional. License for the GitHub project that is attributed as a source for  segment.   License info is required for code citations. | [optional] 

## Example

```python
from openapi_client.models.citation_source import CitationSource

# TODO update the JSON string below
json = "{}"
# create an instance of CitationSource from a JSON string
citation_source_instance = CitationSource.from_json(json)
# print the JSON string representation of the object
print(CitationSource.to_json())

# convert the object into a dict
citation_source_dict = citation_source_instance.to_dict()
# create an instance of CitationSource from a dict
citation_source_from_dict = CitationSource.from_dict(citation_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


