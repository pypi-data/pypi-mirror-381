# CountTokensRequest

Counts the number of tokens in the `prompt` sent to a model.   Models may tokenize text differently, so each model may return a different  `token_count`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | **str** | Required. The model&#39;s resource name. This serves as an ID for the Model to  use.   This name should match a model name returned by the &#x60;ListModels&#x60; method.   Format: &#x60;models/{model}&#x60; | 
**contents** | [**List[Content]**](Content.md) | Optional. The input given to the model as a prompt. This field is ignored  when &#x60;generate_content_request&#x60; is set. | [optional] 
**generate_content_request** | [**GenerateContentRequest**](GenerateContentRequest.md) | Optional. The overall input given to the &#x60;Model&#x60;. This includes the prompt  as well as other model steering information like [system  instructions](https://ai.google.dev/gemini-api/docs/system-instructions),  and/or function declarations for [function  calling](https://ai.google.dev/gemini-api/docs/function-calling).  &#x60;Model&#x60;s/&#x60;Content&#x60;s and &#x60;generate_content_request&#x60;s are mutually  exclusive. You can either send &#x60;Model&#x60; + &#x60;Content&#x60;s or a  &#x60;generate_content_request&#x60;, but never both. | [optional] 

## Example

```python
from openapi_client.models.count_tokens_request import CountTokensRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CountTokensRequest from a JSON string
count_tokens_request_instance = CountTokensRequest.from_json(json)
# print the JSON string representation of the object
print(CountTokensRequest.to_json())

# convert the object into a dict
count_tokens_request_dict = count_tokens_request_instance.to_dict()
# create an instance of CountTokensRequest from a dict
count_tokens_request_from_dict = CountTokensRequest.from_dict(count_tokens_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


