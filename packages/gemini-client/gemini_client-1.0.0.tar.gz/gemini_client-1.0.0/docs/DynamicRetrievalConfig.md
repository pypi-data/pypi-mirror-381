# DynamicRetrievalConfig

Describes the options to customize dynamic retrieval.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **int** | The mode of the predictor to be used in dynamic retrieval. | [optional] 
**dynamic_threshold** | **float** | The threshold to be used in dynamic retrieval.  If not set, a system default value is used. | [optional] 

## Example

```python
from openapi_client.models.dynamic_retrieval_config import DynamicRetrievalConfig

# TODO update the JSON string below
json = "{}"
# create an instance of DynamicRetrievalConfig from a JSON string
dynamic_retrieval_config_instance = DynamicRetrievalConfig.from_json(json)
# print the JSON string representation of the object
print(DynamicRetrievalConfig.to_json())

# convert the object into a dict
dynamic_retrieval_config_dict = dynamic_retrieval_config_instance.to_dict()
# create an instance of DynamicRetrievalConfig from a dict
dynamic_retrieval_config_from_dict = DynamicRetrievalConfig.from_dict(dynamic_retrieval_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


