# SafetyRating

Safety rating for a piece of content.   The safety rating contains the category of harm and the  harm probability level in that category for a piece of content.  Content is classified for safety across a number of  harm categories and the probability of the harm classification is included  here.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **int** | Required. The category for this rating. | 
**probability** | **int** | Required. The probability of harm for this content. | 
**blocked** | **bool** | Was this content blocked because of this rating? | [optional] 

## Example

```python
from openapi_client.models.safety_rating import SafetyRating

# TODO update the JSON string below
json = "{}"
# create an instance of SafetyRating from a JSON string
safety_rating_instance = SafetyRating.from_json(json)
# print the JSON string representation of the object
print(SafetyRating.to_json())

# convert the object into a dict
safety_rating_dict = safety_rating_instance.to_dict()
# create an instance of SafetyRating from a dict
safety_rating_from_dict = SafetyRating.from_dict(safety_rating_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


