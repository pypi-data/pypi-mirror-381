# GenerationConfig

Configuration options for model generation and outputs. Not all parameters  are configurable for every model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**candidate_count** | **int** | Optional. Number of generated responses to return. If unset, this will  default to 1. Please note that this doesn&#39;t work for previous generation  models (Gemini 1.0 family) | [optional] 
**stop_sequences** | **List[str]** | Optional. The set of character sequences (up to 5) that will stop output  generation. If specified, the API will stop at the first appearance of a  &#x60;stop_sequence&#x60;. The stop sequence will not be included as part of the  response. | [optional] 
**max_output_tokens** | **int** | Optional. The maximum number of tokens to include in a response candidate.   Note: The default value varies by model, see the &#x60;Model.output_token_limit&#x60;  attribute of the &#x60;Model&#x60; returned from the &#x60;getModel&#x60; function. | [optional] 
**temperature** | **float** | Optional. Controls the randomness of the output.   Note: The default value varies by model, see the &#x60;Model.temperature&#x60;  attribute of the &#x60;Model&#x60; returned from the &#x60;getModel&#x60; function.   Values can range from [0.0, 2.0]. | [optional] 
**top_p** | **float** | Optional. The maximum cumulative probability of tokens to consider when  sampling.   The model uses combined Top-k and Top-p (nucleus) sampling.   Tokens are sorted based on their assigned probabilities so that only the  most likely tokens are considered. Top-k sampling directly limits the  maximum number of tokens to consider, while Nucleus sampling limits the  number of tokens based on the cumulative probability.   Note: The default value varies by &#x60;Model&#x60; and is specified by  the&#x60;Model.top_p&#x60; attribute returned from the &#x60;getModel&#x60; function. An empty  &#x60;top_k&#x60; attribute indicates that the model doesn&#39;t apply top-k sampling  and doesn&#39;t allow setting &#x60;top_k&#x60; on requests. | [optional] 
**top_k** | **int** | Optional. The maximum number of tokens to consider when sampling.   Gemini models use Top-p (nucleus) sampling or a combination of Top-k and  nucleus sampling. Top-k sampling considers the set of &#x60;top_k&#x60; most probable  tokens. Models running with nucleus sampling don&#39;t allow top_k setting.   Note: The default value varies by &#x60;Model&#x60; and is specified by  the&#x60;Model.top_p&#x60; attribute returned from the &#x60;getModel&#x60; function. An empty  &#x60;top_k&#x60; attribute indicates that the model doesn&#39;t apply top-k sampling  and doesn&#39;t allow setting &#x60;top_k&#x60; on requests. | [optional] 
**seed** | **int** | Optional. Seed used in decoding. If not set, the request uses a randomly  generated seed. | [optional] 
**response_mime_type** | **str** | Optional. MIME type of the generated candidate text.  Supported MIME types are:  &#x60;text/plain&#x60;: (default) Text output.  &#x60;application/json&#x60;: JSON response in the response candidates.  &#x60;text/x.enum&#x60;: ENUM as a string response in the response candidates.  Refer to the  [docs](https://ai.google.dev/gemini-api/docs/prompting_with_media#plain_text_formats)  for a list of all supported text MIME types. | [optional] 
**response_schema** | [**ModelSchema**](ModelSchema.md) | Optional. Output schema of the generated candidate text. Schemas must be a  subset of the [OpenAPI schema](https://spec.openapis.org/oas/v3.0.3#schema)  and can be objects, primitives or arrays.   If set, a compatible &#x60;response_mime_type&#x60; must also be set.  Compatible MIME types:  &#x60;application/json&#x60;: Schema for JSON response.  Refer to the [JSON text generation  guide](https://ai.google.dev/gemini-api/docs/json-mode) for more details. | [optional] 
**response_json_schema** | **object** | Optional. Output schema of the generated response. This is an alternative  to &#x60;response_schema&#x60; that accepts [JSON Schema](https://json-schema.org/).   If set, &#x60;response_schema&#x60; must be omitted, but &#x60;response_mime_type&#x60; is  required.   While the full JSON Schema may be sent, not all features are supported.  Specifically, only the following properties are supported:   - &#x60;$id&#x60;  - &#x60;$defs&#x60;  - &#x60;$ref&#x60;  - &#x60;$anchor&#x60;  - &#x60;type&#x60;  - &#x60;format&#x60;  - &#x60;title&#x60;  - &#x60;description&#x60;  - &#x60;enum&#x60; (for strings and numbers)  - &#x60;items&#x60;  - &#x60;prefixItems&#x60;  - &#x60;minItems&#x60;  - &#x60;maxItems&#x60;  - &#x60;minimum&#x60;  - &#x60;maximum&#x60;  - &#x60;anyOf&#x60;  - &#x60;oneOf&#x60; (interpreted the same as &#x60;anyOf&#x60;)  - &#x60;properties&#x60;  - &#x60;additionalProperties&#x60;  - &#x60;required&#x60;   The non-standard &#x60;propertyOrdering&#x60; property may also be set.   Cyclic references are unrolled to a limited degree and, as such, may only  be used within non-required properties. (Nullable properties are not  sufficient.) If &#x60;$ref&#x60; is set on a sub-schema, no other properties, except  for than those starting as a &#x60;$&#x60;, may be set. | [optional] 
**presence_penalty** | **float** | Optional. Presence penalty applied to the next token&#39;s logprobs if the  token has already been seen in the response.   This penalty is binary on/off and not dependant on the number of times the  token is used (after the first). Use  [frequency_penalty][google.ai.generativelanguage.v1beta.GenerationConfig.frequency_penalty]  for a penalty that increases with each use.   A positive penalty will discourage the use of tokens that have already  been used in the response, increasing the vocabulary.   A negative penalty will encourage the use of tokens that have already been  used in the response, decreasing the vocabulary. | [optional] 
**frequency_penalty** | **float** | Optional. Frequency penalty applied to the next token&#39;s logprobs,  multiplied by the number of times each token has been seen in the respponse  so far.   A positive penalty will discourage the use of tokens that have already  been used, proportional to the number of times the token has been used:  The more a token is used, the more difficult it is for the model to use  that token again increasing the vocabulary of responses.   Caution: A _negative_ penalty will encourage the model to reuse tokens  proportional to the number of times the token has been used. Small  negative values will reduce the vocabulary of a response. Larger negative  values will cause the model to start repeating a common token  until it  hits the  [max_output_tokens][google.ai.generativelanguage.v1beta.GenerationConfig.max_output_tokens]  limit. | [optional] 
**response_logprobs** | **bool** | Optional. If true, export the logprobs results in response. | [optional] 
**logprobs** | **int** | Optional. Only valid if  [response_logprobs&#x3D;True][google.ai.generativelanguage.v1beta.GenerationConfig.response_logprobs].  This sets the number of top logprobs to return at each decoding step in the  [Candidate.logprobs_result][google.ai.generativelanguage.v1beta.Candidate.logprobs_result]. | [optional] 
**enable_enhanced_civic_answers** | **bool** | Optional. Enables enhanced civic answers. It may not be available for all  models. | [optional] 
**response_modalities** | **List[int]** | Optional. The requested modalities of the response. Represents the set of  modalities that the model can return, and should be expected in the  response. This is an exact match to the modalities of the response.   A model may have multiple combinations of supported modalities. If the  requested modalities do not match any of the supported combinations, an  error will be returned.   An empty list is equivalent to requesting only text. | [optional] 
**speech_config** | [**SpeechConfig**](SpeechConfig.md) | Optional. The speech generation config. | [optional] 
**thinking_config** | [**ThinkingConfig**](ThinkingConfig.md) | Optional. Config for thinking features.  An error will be returned if this field is set for models that don&#39;t  support thinking. | [optional] 
**media_resolution** | **int** | Optional. If specified, the media resolution specified will be used. | [optional] 

## Example

```python
from openapi_client.models.generation_config import GenerationConfig

# TODO update the JSON string below
json = "{}"
# create an instance of GenerationConfig from a JSON string
generation_config_instance = GenerationConfig.from_json(json)
# print the JSON string representation of the object
print(GenerationConfig.to_json())

# convert the object into a dict
generation_config_dict = generation_config_instance.to_dict()
# create an instance of GenerationConfig from a dict
generation_config_from_dict = GenerationConfig.from_dict(generation_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


