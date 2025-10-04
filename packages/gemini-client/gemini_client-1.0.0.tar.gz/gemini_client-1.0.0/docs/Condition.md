# Condition

Filter condition applicable to a single key.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**string_value** | **str** | The string value to filter the metadata on. | [optional] 
**numeric_value** | **float** | The numeric value to filter the metadata on. | [optional] 
**operation** | **int** | Required. Operator applied to the given key-value pair to trigger the  condition. | 

## Example

```python
from openapi_client.models.condition import Condition

# TODO update the JSON string below
json = "{}"
# create an instance of Condition from a JSON string
condition_instance = Condition.from_json(json)
# print the JSON string representation of the object
print(Condition.to_json())

# convert the object into a dict
condition_dict = condition_instance.to_dict()
# create an instance of Condition from a dict
condition_from_dict = Condition.from_dict(condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


