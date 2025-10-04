# GenerateContentResponse

Response from the model supporting multiple candidate responses.   Safety ratings and content filtering are reported for both  prompt in `GenerateContentResponse.prompt_feedback` and for each candidate  in `finish_reason` and in `safety_ratings`. The API:   - Returns either all requested candidates or none of them   - Returns no candidates at all only if there was something wrong with the     prompt (check `prompt_feedback`)   - Reports feedback on each candidate in `finish_reason` and     `safety_ratings`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**candidates** | [**List[Candidate]**](Candidate.md) | Candidate responses from the model. | [optional] 
**prompt_feedback** | [**GenerateContentResponsePromptFeedback**](GenerateContentResponsePromptFeedback.md) | Returns the prompt&#39;s feedback related to the content filters. | [optional] 
**usage_metadata** | [**GenerateContentResponseUsageMetadata**](GenerateContentResponseUsageMetadata.md) | Output only. Metadata on the generation requests&#39; token usage. | [optional] [readonly] 
**model_version** | **str** | Output only. The model version used to generate the response. | [optional] [readonly] 
**response_id** | **str** | Output only. response_id is used to identify each response. | [optional] [readonly] 

## Example

```python
from openapi_client.models.generate_content_response import GenerateContentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateContentResponse from a JSON string
generate_content_response_instance = GenerateContentResponse.from_json(json)
# print the JSON string representation of the object
print(GenerateContentResponse.to_json())

# convert the object into a dict
generate_content_response_dict = generate_content_response_instance.to_dict()
# create an instance of GenerateContentResponse from a dict
generate_content_response_from_dict = GenerateContentResponse.from_dict(generate_content_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


