# RetrievalMetadata

Metadata related to retrieval in the grounding flow.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**google_search_dynamic_retrieval_score** | **float** | Optional. Score indicating how likely information from google search could  help answer the prompt. The score is in the range [0, 1], where 0 is the  least likely and 1 is the most likely. This score is only populated when  google search grounding and dynamic retrieval is enabled. It will be  compared to the threshold to determine whether to trigger google search. | [optional] 

## Example

```python
from openapi_client.models.retrieval_metadata import RetrievalMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of RetrievalMetadata from a JSON string
retrieval_metadata_instance = RetrievalMetadata.from_json(json)
# print the JSON string representation of the object
print(RetrievalMetadata.to_json())

# convert the object into a dict
retrieval_metadata_dict = retrieval_metadata_instance.to_dict()
# create an instance of RetrievalMetadata from a dict
retrieval_metadata_from_dict = RetrievalMetadata.from_dict(retrieval_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


