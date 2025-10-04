# GenerateAnswerRequest

Request to generate a grounded answer from the `Model`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inline_passages** | [**GroundingPassages**](GroundingPassages.md) | Passages provided inline with the request. | [optional] 
**semantic_retriever** | [**SemanticRetrieverConfig**](SemanticRetrieverConfig.md) | Content retrieved from resources created via the Semantic Retriever  API. | [optional] 
**model** | **str** | Required. The name of the &#x60;Model&#x60; to use for generating the grounded  response.   Format: &#x60;model&#x3D;models/{model}&#x60;. | 
**contents** | [**List[Content]**](Content.md) | Required. The content of the current conversation with the &#x60;Model&#x60;. For  single-turn queries, this is a single question to answer. For multi-turn  queries, this is a repeated field that contains conversation history and  the last &#x60;Content&#x60; in the list containing the question.   Note: &#x60;GenerateAnswer&#x60; only supports queries in English. | 
**answer_style** | **int** | Required. Style in which answers should be returned. | 
**safety_settings** | [**List[SafetySetting]**](SafetySetting.md) | Optional. A list of unique &#x60;SafetySetting&#x60; instances for blocking unsafe  content.   This will be enforced on the &#x60;GenerateAnswerRequest.contents&#x60; and  &#x60;GenerateAnswerResponse.candidate&#x60;. There should not be more than one  setting for each &#x60;SafetyCategory&#x60; type. The API will block any contents and  responses that fail to meet the thresholds set by these settings. This list  overrides the default settings for each &#x60;SafetyCategory&#x60; specified in the  safety_settings. If there is no &#x60;SafetySetting&#x60; for a given  &#x60;SafetyCategory&#x60; provided in the list, the API will use the default safety  setting for that category. Harm categories HARM_CATEGORY_HATE_SPEECH,  HARM_CATEGORY_SEXUALLY_EXPLICIT, HARM_CATEGORY_DANGEROUS_CONTENT,  HARM_CATEGORY_HARASSMENT are supported.  Refer to the  [guide](https://ai.google.dev/gemini-api/docs/safety-settings)  for detailed information on available safety settings. Also refer to the  [Safety guidance](https://ai.google.dev/gemini-api/docs/safety-guidance) to  learn how to incorporate safety considerations in your AI applications. | [optional] 
**temperature** | **float** | Optional. Controls the randomness of the output.   Values can range from [0.0,1.0], inclusive. A value closer to 1.0 will  produce responses that are more varied and creative, while a value closer  to 0.0 will typically result in more straightforward responses from the  model. A low temperature (~0.2) is usually recommended for  Attributed-Question-Answering use cases. | [optional] 

## Example

```python
from openapi_client.models.generate_answer_request import GenerateAnswerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateAnswerRequest from a JSON string
generate_answer_request_instance = GenerateAnswerRequest.from_json(json)
# print the JSON string representation of the object
print(GenerateAnswerRequest.to_json())

# convert the object into a dict
generate_answer_request_dict = generate_answer_request_instance.to_dict()
# create an instance of GenerateAnswerRequest from a dict
generate_answer_request_from_dict = GenerateAnswerRequest.from_dict(generate_answer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


