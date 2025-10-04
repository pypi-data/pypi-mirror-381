# GenerateAnswerResponse

Response from the model for a grounded answer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**answer** | [**Candidate**](Candidate.md) | Candidate answer from the model.   Note: The model *always* attempts to provide a grounded answer, even when  the answer is unlikely to be answerable from the given passages.  In that case, a low-quality or ungrounded answer may be provided, along  with a low &#x60;answerable_probability&#x60;. | [optional] 
**answerable_probability** | **float** | Output only. The model&#39;s estimate of the probability that its answer is  correct and grounded in the input passages.   A low &#x60;answerable_probability&#x60; indicates that the answer might not be  grounded in the sources.   When &#x60;answerable_probability&#x60; is low, you may want to:   * Display a message to the effect of \&quot;We couldn’t answer that question\&quot; to  the user.  * Fall back to a general-purpose LLM that answers the question from world  knowledge. The threshold and nature of such fallbacks will depend on  individual use cases. &#x60;0.5&#x60; is a good starting threshold. | [optional] [readonly] 
**input_feedback** | [**GenerateAnswerResponseInputFeedback**](GenerateAnswerResponseInputFeedback.md) | Output only. Feedback related to the input data used to answer the  question, as opposed to the model-generated response to the question.   The input data can be one or more of the following:   - Question specified by the last entry in &#x60;GenerateAnswerRequest.content&#x60;  - Conversation history specified by the other entries in  &#x60;GenerateAnswerRequest.content&#x60;  - Grounding sources (&#x60;GenerateAnswerRequest.semantic_retriever&#x60; or  &#x60;GenerateAnswerRequest.inline_passages&#x60;) | [optional] [readonly] 

## Example

```python
from openapi_client.models.generate_answer_response import GenerateAnswerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateAnswerResponse from a JSON string
generate_answer_response_instance = GenerateAnswerResponse.from_json(json)
# print the JSON string representation of the object
print(GenerateAnswerResponse.to_json())

# convert the object into a dict
generate_answer_response_dict = generate_answer_response_instance.to_dict()
# create an instance of GenerateAnswerResponse from a dict
generate_answer_response_from_dict = GenerateAnswerResponse.from_dict(generate_answer_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


