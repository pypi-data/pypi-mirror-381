# GenerateContentRequest

Request to generate a completion from the model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | **str** | Required. The name of the &#x60;Model&#x60; to use for generating the completion.   Format: &#x60;models/{model}&#x60;. | 
**system_instruction** | [**Content**](Content.md) | Optional. Developer set [system  instruction(s)](https://ai.google.dev/gemini-api/docs/system-instructions).  Currently, text only. | [optional] 
**contents** | [**List[Content]**](Content.md) | Required. The content of the current conversation with the model.   For single-turn queries, this is a single instance. For multi-turn queries  like [chat](https://ai.google.dev/gemini-api/docs/text-generation#chat),  this is a repeated field that contains the conversation history and the  latest request. | 
**tools** | [**List[Tool]**](Tool.md) | Optional. A list of &#x60;Tools&#x60; the &#x60;Model&#x60; may use to generate the next  response.   A &#x60;Tool&#x60; is a piece of code that enables the system to interact with  external systems to perform an action, or set of actions, outside of  knowledge and scope of the &#x60;Model&#x60;. Supported &#x60;Tool&#x60;s are &#x60;Function&#x60; and  &#x60;code_execution&#x60;. Refer to the [Function  calling](https://ai.google.dev/gemini-api/docs/function-calling) and the  [Code execution](https://ai.google.dev/gemini-api/docs/code-execution)  guides to learn more. | [optional] 
**tool_config** | [**ToolConfig**](ToolConfig.md) | Optional. Tool configuration for any &#x60;Tool&#x60; specified in the request. Refer  to the [Function calling  guide](https://ai.google.dev/gemini-api/docs/function-calling#function_calling_mode)  for a usage example. | [optional] 
**safety_settings** | [**List[SafetySetting]**](SafetySetting.md) | Optional. A list of unique &#x60;SafetySetting&#x60; instances for blocking unsafe  content.   This will be enforced on the &#x60;GenerateContentRequest.contents&#x60; and  &#x60;GenerateContentResponse.candidates&#x60;. There should not be more than one  setting for each &#x60;SafetyCategory&#x60; type. The API will block any contents and  responses that fail to meet the thresholds set by these settings. This list  overrides the default settings for each &#x60;SafetyCategory&#x60; specified in the  safety_settings. If there is no &#x60;SafetySetting&#x60; for a given  &#x60;SafetyCategory&#x60; provided in the list, the API will use the default safety  setting for that category. Harm categories HARM_CATEGORY_HATE_SPEECH,  HARM_CATEGORY_SEXUALLY_EXPLICIT, HARM_CATEGORY_DANGEROUS_CONTENT,  HARM_CATEGORY_HARASSMENT, HARM_CATEGORY_CIVIC_INTEGRITY are supported.  Refer to the [guide](https://ai.google.dev/gemini-api/docs/safety-settings)  for detailed information on available safety settings. Also refer to the  [Safety guidance](https://ai.google.dev/gemini-api/docs/safety-guidance) to  learn how to incorporate safety considerations in your AI applications. | [optional] 
**generation_config** | [**GenerationConfig**](GenerationConfig.md) | Optional. Configuration options for model generation and outputs. | [optional] 
**cached_content** | **str** | Optional. The name of the content  [cached](https://ai.google.dev/gemini-api/docs/caching) to use as context  to serve the prediction. Format: &#x60;cachedContents/{cachedContent}&#x60; | [optional] 

## Example

```python
from openapi_client.models.generate_content_request import GenerateContentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateContentRequest from a JSON string
generate_content_request_instance = GenerateContentRequest.from_json(json)
# print the JSON string representation of the object
print(GenerateContentRequest.to_json())

# convert the object into a dict
generate_content_request_dict = generate_content_request_instance.to_dict()
# create an instance of GenerateContentRequest from a dict
generate_content_request_from_dict = GenerateContentRequest.from_dict(generate_content_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


