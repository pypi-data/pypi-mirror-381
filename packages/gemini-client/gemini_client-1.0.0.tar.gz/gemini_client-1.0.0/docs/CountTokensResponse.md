# CountTokensResponse

A response from `CountTokens`.   It returns the model's `token_count` for the `prompt`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_tokens** | **int** | The number of tokens that the &#x60;Model&#x60; tokenizes the &#x60;prompt&#x60; into. Always  non-negative. | [optional] 
**cached_content_token_count** | **int** | Number of tokens in the cached part of the prompt (the cached content). | [optional] 
**prompt_tokens_details** | [**List[ModalityTokenCount]**](ModalityTokenCount.md) | Output only. List of modalities that were processed in the request input. | [optional] [readonly] 
**cache_tokens_details** | [**List[ModalityTokenCount]**](ModalityTokenCount.md) | Output only. List of modalities that were processed in the cached content. | [optional] [readonly] 

## Example

```python
from openapi_client.models.count_tokens_response import CountTokensResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CountTokensResponse from a JSON string
count_tokens_response_instance = CountTokensResponse.from_json(json)
# print the JSON string representation of the object
print(CountTokensResponse.to_json())

# convert the object into a dict
count_tokens_response_dict = count_tokens_response_instance.to_dict()
# create an instance of CountTokensResponse from a dict
count_tokens_response_from_dict = CountTokensResponse.from_dict(count_tokens_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


