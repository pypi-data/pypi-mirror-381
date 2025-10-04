# LogprobsResultCandidate

Candidate for the logprobs token and score.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | The candidate’s token string value. | [optional] 
**token_id** | **int** | The candidate’s token id value. | [optional] 
**log_probability** | **float** | The candidate&#39;s log probability. | [optional] 

## Example

```python
from openapi_client.models.logprobs_result_candidate import LogprobsResultCandidate

# TODO update the JSON string below
json = "{}"
# create an instance of LogprobsResultCandidate from a JSON string
logprobs_result_candidate_instance = LogprobsResultCandidate.from_json(json)
# print the JSON string representation of the object
print(LogprobsResultCandidate.to_json())

# convert the object into a dict
logprobs_result_candidate_dict = logprobs_result_candidate_instance.to_dict()
# create an instance of LogprobsResultCandidate from a dict
logprobs_result_candidate_from_dict = LogprobsResultCandidate.from_dict(logprobs_result_candidate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


