# CodeExecutionResult

Result of executing the `ExecutableCode`.   Only generated when using the `CodeExecution`, and always follows a `part`  containing the `ExecutableCode`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**outcome** | **int** | Required. Outcome of the code execution. | 
**output** | **str** | Optional. Contains stdout when code execution is successful, stderr or  other description otherwise. | [optional] 

## Example

```python
from openapi_client.models.code_execution_result import CodeExecutionResult

# TODO update the JSON string below
json = "{}"
# create an instance of CodeExecutionResult from a JSON string
code_execution_result_instance = CodeExecutionResult.from_json(json)
# print the JSON string representation of the object
print(CodeExecutionResult.to_json())

# convert the object into a dict
code_execution_result_dict = code_execution_result_instance.to_dict()
# create an instance of CodeExecutionResult from a dict
code_execution_result_from_dict = CodeExecutionResult.from_dict(code_execution_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


