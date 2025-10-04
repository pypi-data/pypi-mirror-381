# GenerateContentResponsePromptFeedback

A set of the feedback metadata the prompt specified in  `GenerateContentRequest.content`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block_reason** | **int** | Optional. If set, the prompt was blocked and no candidates are returned.  Rephrase the prompt. | [optional] 
**safety_ratings** | [**List[SafetyRating]**](SafetyRating.md) | Ratings for safety of the prompt.  There is at most one rating per category. | [optional] 

## Example

```python
from openapi_client.models.generate_content_response_prompt_feedback import GenerateContentResponsePromptFeedback

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateContentResponsePromptFeedback from a JSON string
generate_content_response_prompt_feedback_instance = GenerateContentResponsePromptFeedback.from_json(json)
# print the JSON string representation of the object
print(GenerateContentResponsePromptFeedback.to_json())

# convert the object into a dict
generate_content_response_prompt_feedback_dict = generate_content_response_prompt_feedback_instance.to_dict()
# create an instance of GenerateContentResponsePromptFeedback from a dict
generate_content_response_prompt_feedback_from_dict = GenerateContentResponsePromptFeedback.from_dict(generate_content_response_prompt_feedback_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


