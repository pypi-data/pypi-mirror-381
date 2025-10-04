# CitationMetadata

A collection of source attributions for a piece of content.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**citation_sources** | [**List[CitationSource]**](CitationSource.md) | Citations to sources for a specific response. | [optional] 

## Example

```python
from openapi_client.models.citation_metadata import CitationMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of CitationMetadata from a JSON string
citation_metadata_instance = CitationMetadata.from_json(json)
# print the JSON string representation of the object
print(CitationMetadata.to_json())

# convert the object into a dict
citation_metadata_dict = citation_metadata_instance.to_dict()
# create an instance of CitationMetadata from a dict
citation_metadata_from_dict = CitationMetadata.from_dict(citation_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


