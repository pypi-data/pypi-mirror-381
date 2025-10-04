# LogprobsResultTopCandidates

Candidates with top log probabilities at each decoding step.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**candidates** | [**List[LogprobsResultCandidate]**](LogprobsResultCandidate.md) | Sorted by log probability in descending order. | [optional] 

## Example

```python
from openapi_client.models.logprobs_result_top_candidates import LogprobsResultTopCandidates

# TODO update the JSON string below
json = "{}"
# create an instance of LogprobsResultTopCandidates from a JSON string
logprobs_result_top_candidates_instance = LogprobsResultTopCandidates.from_json(json)
# print the JSON string representation of the object
print(LogprobsResultTopCandidates.to_json())

# convert the object into a dict
logprobs_result_top_candidates_dict = logprobs_result_top_candidates_instance.to_dict()
# create an instance of LogprobsResultTopCandidates from a dict
logprobs_result_top_candidates_from_dict = LogprobsResultTopCandidates.from_dict(logprobs_result_top_candidates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


