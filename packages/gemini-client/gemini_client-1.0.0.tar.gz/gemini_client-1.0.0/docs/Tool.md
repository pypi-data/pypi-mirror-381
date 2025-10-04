# Tool

Tool details that the model may use to generate response.   A `Tool` is a piece of code that enables the system to interact with  external systems to perform an action, or set of actions, outside of  knowledge and scope of the model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**function_declarations** | [**List[FunctionDeclaration]**](FunctionDeclaration.md) | Optional. A list of &#x60;FunctionDeclarations&#x60; available to the model that can  be used for function calling.   The model or system does not execute the function. Instead the defined  function may be returned as a  [FunctionCall][google.ai.generativelanguage.v1beta.Part.function_call] with  arguments to the client side for execution. The model may decide to call a  subset of these functions by populating  [FunctionCall][google.ai.generativelanguage.v1beta.Part.function_call] in  the response. The next conversation turn may contain a  [FunctionResponse][google.ai.generativelanguage.v1beta.Part.function_response]  with the [Content.role][google.ai.generativelanguage.v1beta.Content.role]  \&quot;function\&quot; generation context for the next model turn. | [optional] 
**google_search_retrieval** | [**GoogleSearchRetrieval**](GoogleSearchRetrieval.md) | Optional. Retrieval tool that is powered by Google search. | [optional] 
**code_execution** | **object** | Optional. Enables the model to execute code as part of generation. | [optional] 
**google_search** | [**ToolGoogleSearch**](ToolGoogleSearch.md) | Optional. GoogleSearch tool type.  Tool to support Google Search in Model. Powered by Google. | [optional] 
**url_context** | **object** | Optional. Tool to support URL context retrieval. | [optional] 

## Example

```python
from openapi_client.models.tool import Tool

# TODO update the JSON string below
json = "{}"
# create an instance of Tool from a JSON string
tool_instance = Tool.from_json(json)
# print the JSON string representation of the object
print(Tool.to_json())

# convert the object into a dict
tool_dict = tool_instance.to_dict()
# create an instance of Tool from a dict
tool_from_dict = Tool.from_dict(tool_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


