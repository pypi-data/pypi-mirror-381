# GenerateContentResponseUsageMetadata

Metadata on the generation request's token usage.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prompt_token_count** | **int** | Number of tokens in the prompt. When &#x60;cached_content&#x60; is set, this is  still the total effective prompt size meaning this includes the number of  tokens in the cached content. | [optional] 
**cached_content_token_count** | **int** | Number of tokens in the cached part of the prompt (the cached content) | [optional] 
**candidates_token_count** | **int** | Total number of tokens across all the generated response candidates. | [optional] 
**tool_use_prompt_token_count** | **int** | Output only. Number of tokens present in tool-use prompt(s). | [optional] [readonly] 
**thoughts_token_count** | **int** | Output only. Number of tokens of thoughts for thinking models. | [optional] [readonly] 
**total_token_count** | **int** | Total token count for the generation request (prompt + response  candidates). | [optional] 
**prompt_tokens_details** | [**List[ModalityTokenCount]**](ModalityTokenCount.md) | Output only. List of modalities that were processed in the request input. | [optional] [readonly] 
**cache_tokens_details** | [**List[ModalityTokenCount]**](ModalityTokenCount.md) | Output only. List of modalities of the cached content in the request  input. | [optional] [readonly] 
**candidates_tokens_details** | [**List[ModalityTokenCount]**](ModalityTokenCount.md) | Output only. List of modalities that were returned in the response. | [optional] [readonly] 
**tool_use_prompt_tokens_details** | [**List[ModalityTokenCount]**](ModalityTokenCount.md) | Output only. List of modalities that were processed for tool-use request  inputs. | [optional] [readonly] 

## Example

```python
from openapi_client.models.generate_content_response_usage_metadata import GenerateContentResponseUsageMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateContentResponseUsageMetadata from a JSON string
generate_content_response_usage_metadata_instance = GenerateContentResponseUsageMetadata.from_json(json)
# print the JSON string representation of the object
print(GenerateContentResponseUsageMetadata.to_json())

# convert the object into a dict
generate_content_response_usage_metadata_dict = generate_content_response_usage_metadata_instance.to_dict()
# create an instance of GenerateContentResponseUsageMetadata from a dict
generate_content_response_usage_metadata_from_dict = GenerateContentResponseUsageMetadata.from_dict(generate_content_response_usage_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


