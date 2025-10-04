# VideoMetadata

Metadata describes the input video content.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_offset** | **str** | Optional. The start offset of the video. | [optional] 
**end_offset** | **str** | Optional. The end offset of the video. | [optional] 
**fps** | **float** | Optional. The frame rate of the video sent to the model. If not specified,  the default value will be 1.0. The fps range is (0.0, 24.0]. | [optional] 

## Example

```python
from openapi_client.models.video_metadata import VideoMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of VideoMetadata from a JSON string
video_metadata_instance = VideoMetadata.from_json(json)
# print the JSON string representation of the object
print(VideoMetadata.to_json())

# convert the object into a dict
video_metadata_dict = video_metadata_instance.to_dict()
# create an instance of VideoMetadata from a dict
video_metadata_from_dict = VideoMetadata.from_dict(video_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


