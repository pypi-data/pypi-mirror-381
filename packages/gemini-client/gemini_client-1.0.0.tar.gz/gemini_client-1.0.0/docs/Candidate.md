# Candidate

A response candidate generated from the model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** | Output only. Index of the candidate in the list of response candidates. | [optional] [readonly] 
**content** | [**Content**](Content.md) | Output only. Generated content returned from the model. | [optional] [readonly] 
**finish_reason** | **int** | Optional. Output only. The reason why the model stopped generating tokens.   If empty, the model has not stopped generating tokens. | [optional] [readonly] 
**safety_ratings** | [**List[SafetyRating]**](SafetyRating.md) | List of ratings for the safety of a response candidate.   There is at most one rating per category. | [optional] 
**citation_metadata** | [**CitationMetadata**](CitationMetadata.md) | Output only. Citation information for model-generated candidate.   This field may be populated with recitation information for any text  included in the &#x60;content&#x60;. These are passages that are \&quot;recited\&quot; from  copyrighted material in the foundational LLM&#39;s training data. | [optional] [readonly] 
**token_count** | **int** | Output only. Token count for this candidate. | [optional] [readonly] 
**grounding_attributions** | [**List[GroundingAttribution]**](GroundingAttribution.md) | Output only. Attribution information for sources that contributed to a  grounded answer.   This field is populated for &#x60;GenerateAnswer&#x60; calls. | [optional] [readonly] 
**grounding_metadata** | [**GroundingMetadata**](GroundingMetadata.md) | Output only. Grounding metadata for the candidate.   This field is populated for &#x60;GenerateContent&#x60; calls. | [optional] [readonly] 
**avg_logprobs** | **float** | Output only. Average log probability score of the candidate. | [optional] [readonly] 
**logprobs_result** | [**LogprobsResult**](LogprobsResult.md) | Output only. Log-likelihood scores for the response tokens and top tokens | [optional] [readonly] 
**url_context_metadata** | [**UrlContextMetadata**](UrlContextMetadata.md) | Output only. Metadata related to url context retrieval tool. | [optional] [readonly] 

## Example

```python
from openapi_client.models.candidate import Candidate

# TODO update the JSON string below
json = "{}"
# create an instance of Candidate from a JSON string
candidate_instance = Candidate.from_json(json)
# print the JSON string representation of the object
print(Candidate.to_json())

# convert the object into a dict
candidate_dict = candidate_instance.to_dict()
# create an instance of Candidate from a dict
candidate_from_dict = Candidate.from_dict(candidate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


