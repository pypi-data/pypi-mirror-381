# FunctionDeclaration

Structured representation of a function declaration as defined by the  [OpenAPI 3.03 specification](https://spec.openapis.org/oas/v3.0.3). Included  in this declaration are the function name and parameters. This  FunctionDeclaration is a representation of a block of code that can be used  as a `Tool` by the model and executed by the client.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Required. The name of the function.  Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum  length of 63. | 
**description** | **str** | Required. A brief description of the function. | 
**parameters** | [**ModelSchema**](ModelSchema.md) | Optional. Describes the parameters to this function. Reflects the Open  API 3.03 Parameter Object string Key: the name of the parameter. Parameter  names are case sensitive. Schema Value: the Schema defining the type used  for the parameter. | [optional] 
**parameters_json_schema** | **object** | Optional. Describes the parameters to the function in JSON Schema format.  The schema must describe an object where the properties are the parameters  to the function. For example:   &#x60;&#x60;&#x60;  {    \&quot;type\&quot;: \&quot;object\&quot;,    \&quot;properties\&quot;: {      \&quot;name\&quot;: { \&quot;type\&quot;: \&quot;string\&quot; },      \&quot;age\&quot;: { \&quot;type\&quot;: \&quot;integer\&quot; }    },    \&quot;additionalProperties\&quot;: false,    \&quot;required\&quot;: [\&quot;name\&quot;, \&quot;age\&quot;],    \&quot;propertyOrdering\&quot;: [\&quot;name\&quot;, \&quot;age\&quot;]  }  &#x60;&#x60;&#x60;   This field is mutually exclusive with &#x60;parameters&#x60;. | [optional] 
**response** | [**ModelSchema**](ModelSchema.md) | Optional. Describes the output from this function in JSON Schema format.  Reflects the Open API 3.03 Response Object. The Schema defines the type  used for the response value of the function. | [optional] 
**response_json_schema** | **object** | Optional. Describes the output from this function in JSON Schema format.  The value specified by the schema is the response value of the function.   This field is mutually exclusive with &#x60;response&#x60;. | [optional] 
**behavior** | **int** | Optional. Specifies the function Behavior.  Currently only supported by the BidiGenerateContent method. | [optional] 

## Example

```python
from openapi_client.models.function_declaration import FunctionDeclaration

# TODO update the JSON string below
json = "{}"
# create an instance of FunctionDeclaration from a JSON string
function_declaration_instance = FunctionDeclaration.from_json(json)
# print the JSON string representation of the object
print(FunctionDeclaration.to_json())

# convert the object into a dict
function_declaration_dict = function_declaration_instance.to_dict()
# create an instance of FunctionDeclaration from a dict
function_declaration_from_dict = FunctionDeclaration.from_dict(function_declaration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


