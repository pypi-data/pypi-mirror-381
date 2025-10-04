# LogprobsResult

Logprobs Result

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**top_candidates** | [**List[LogprobsResultTopCandidates]**](LogprobsResultTopCandidates.md) | Length &#x3D; total number of decoding steps. | [optional] 
**chosen_candidates** | [**List[LogprobsResultCandidate]**](LogprobsResultCandidate.md) | Length &#x3D; total number of decoding steps.  The chosen candidates may or may not be in top_candidates. | [optional] 

## Example

```python
from openapi_client.models.logprobs_result import LogprobsResult

# TODO update the JSON string below
json = "{}"
# create an instance of LogprobsResult from a JSON string
logprobs_result_instance = LogprobsResult.from_json(json)
# print the JSON string representation of the object
print(LogprobsResult.to_json())

# convert the object into a dict
logprobs_result_dict = logprobs_result_instance.to_dict()
# create an instance of LogprobsResult from a dict
logprobs_result_from_dict = LogprobsResult.from_dict(logprobs_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


