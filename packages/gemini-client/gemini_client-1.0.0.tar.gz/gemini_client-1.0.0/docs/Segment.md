# Segment

Segment of the content.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**part_index** | **int** | Output only. The index of a Part object within its parent Content object. | [optional] [readonly] 
**start_index** | **int** | Output only. Start index in the given Part, measured in bytes. Offset from  the start of the Part, inclusive, starting at zero. | [optional] [readonly] 
**end_index** | **int** | Output only. End index in the given Part, measured in bytes. Offset from  the start of the Part, exclusive, starting at zero. | [optional] [readonly] 
**text** | **str** | Output only. The text corresponding to the segment from the response. | [optional] [readonly] 

## Example

```python
from openapi_client.models.segment import Segment

# TODO update the JSON string below
json = "{}"
# create an instance of Segment from a JSON string
segment_instance = Segment.from_json(json)
# print the JSON string representation of the object
print(Segment.to_json())

# convert the object into a dict
segment_dict = segment_instance.to_dict()
# create an instance of Segment from a dict
segment_from_dict = Segment.from_dict(segment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


