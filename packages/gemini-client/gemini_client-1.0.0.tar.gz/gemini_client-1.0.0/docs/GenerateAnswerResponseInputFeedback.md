# GenerateAnswerResponseInputFeedback

Feedback related to the input data used to answer the question, as opposed  to the model-generated response to the question.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block_reason** | **int** | Optional. If set, the input was blocked and no candidates are returned.  Rephrase the input. | [optional] 
**safety_ratings** | [**List[SafetyRating]**](SafetyRating.md) | Ratings for safety of the input.  There is at most one rating per category. | [optional] 

## Example

```python
from openapi_client.models.generate_answer_response_input_feedback import GenerateAnswerResponseInputFeedback

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateAnswerResponseInputFeedback from a JSON string
generate_answer_response_input_feedback_instance = GenerateAnswerResponseInputFeedback.from_json(json)
# print the JSON string representation of the object
print(GenerateAnswerResponseInputFeedback.to_json())

# convert the object into a dict
generate_answer_response_input_feedback_dict = generate_answer_response_input_feedback_instance.to_dict()
# create an instance of GenerateAnswerResponseInputFeedback from a dict
generate_answer_response_input_feedback_from_dict = GenerateAnswerResponseInputFeedback.from_dict(generate_answer_response_input_feedback_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


