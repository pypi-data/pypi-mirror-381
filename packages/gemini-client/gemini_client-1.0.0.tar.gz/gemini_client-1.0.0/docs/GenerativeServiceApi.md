# openapi_client.GenerativeServiceApi

All URIs are relative to *https://generativelanguage.googleapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generative_service_batch_embed_contents**](GenerativeServiceApi.md#generative_service_batch_embed_contents) | **POST** /v1beta/models/{model}:batchEmbedContents | 
[**generative_service_count_tokens**](GenerativeServiceApi.md#generative_service_count_tokens) | **POST** /v1beta/models/{model}:countTokens | 
[**generative_service_embed_content**](GenerativeServiceApi.md#generative_service_embed_content) | **POST** /v1beta/models/{model}:embedContent | 
[**generative_service_generate_answer**](GenerativeServiceApi.md#generative_service_generate_answer) | **POST** /v1beta/models/{model}:generateAnswer | 
[**generative_service_generate_dynamic_content**](GenerativeServiceApi.md#generative_service_generate_dynamic_content) | **POST** /v1beta/dynamic/{dynamic}:generateContent | 
[**generative_service_generate_model_content**](GenerativeServiceApi.md#generative_service_generate_model_content) | **POST** /v1beta/models/{model}:generateContent | 
[**generative_service_generate_tuned_model_content**](GenerativeServiceApi.md#generative_service_generate_tuned_model_content) | **POST** /v1beta/tunedModels/{tunedModel}:generateContent | 
[**generative_service_stream_generate_dynamic_content**](GenerativeServiceApi.md#generative_service_stream_generate_dynamic_content) | **POST** /v1beta/dynamic/{dynamic}:streamGenerateContent | 
[**generative_service_stream_generate_model_content**](GenerativeServiceApi.md#generative_service_stream_generate_model_content) | **POST** /v1beta/models/{model}:streamGenerateContent | 
[**generative_service_stream_generate_tuned_model_content**](GenerativeServiceApi.md#generative_service_stream_generate_tuned_model_content) | **POST** /v1beta/tunedModels/{tunedModel}:streamGenerateContent | 


# **generative_service_batch_embed_contents**
> BatchEmbedContentsResponse generative_service_batch_embed_contents(model, batch_embed_contents_request)

Generates multiple embedding vectors from the input `Content` which
 consists of a batch of strings represented as `EmbedContentRequest`
 objects.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.batch_embed_contents_request import BatchEmbedContentsRequest
from openapi_client.models.batch_embed_contents_response import BatchEmbedContentsResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://generativelanguage.googleapis.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://generativelanguage.googleapis.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.GenerativeServiceApi(api_client)
    model = 'model_example' # str | The model id.
    batch_embed_contents_request = openapi_client.BatchEmbedContentsRequest() # BatchEmbedContentsRequest | 

    try:
        api_response = api_instance.generative_service_batch_embed_contents(model, batch_embed_contents_request)
        print("The response of GenerativeServiceApi->generative_service_batch_embed_contents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenerativeServiceApi->generative_service_batch_embed_contents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | **str**| The model id. | 
 **batch_embed_contents_request** | [**BatchEmbedContentsRequest**](BatchEmbedContentsRequest.md)|  | 

### Return type

[**BatchEmbedContentsResponse**](BatchEmbedContentsResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generative_service_count_tokens**
> CountTokensResponse generative_service_count_tokens(model, count_tokens_request)

Runs a model's tokenizer on input `Content` and returns the token count.
 Refer to the [tokens guide](https://ai.google.dev/gemini-api/docs/tokens)
 to learn more about tokens.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.count_tokens_request import CountTokensRequest
from openapi_client.models.count_tokens_response import CountTokensResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://generativelanguage.googleapis.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://generativelanguage.googleapis.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.GenerativeServiceApi(api_client)
    model = 'model_example' # str | The model id.
    count_tokens_request = openapi_client.CountTokensRequest() # CountTokensRequest | 

    try:
        api_response = api_instance.generative_service_count_tokens(model, count_tokens_request)
        print("The response of GenerativeServiceApi->generative_service_count_tokens:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenerativeServiceApi->generative_service_count_tokens: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | **str**| The model id. | 
 **count_tokens_request** | [**CountTokensRequest**](CountTokensRequest.md)|  | 

### Return type

[**CountTokensResponse**](CountTokensResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generative_service_embed_content**
> EmbedContentResponse generative_service_embed_content(model, embed_content_request)

Generates a text embedding vector from the input `Content` using the
 specified [Gemini Embedding
 model](https://ai.google.dev/gemini-api/docs/models/gemini#text-embedding).

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.embed_content_request import EmbedContentRequest
from openapi_client.models.embed_content_response import EmbedContentResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://generativelanguage.googleapis.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://generativelanguage.googleapis.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.GenerativeServiceApi(api_client)
    model = 'model_example' # str | The model id.
    embed_content_request = openapi_client.EmbedContentRequest() # EmbedContentRequest | 

    try:
        api_response = api_instance.generative_service_embed_content(model, embed_content_request)
        print("The response of GenerativeServiceApi->generative_service_embed_content:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenerativeServiceApi->generative_service_embed_content: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | **str**| The model id. | 
 **embed_content_request** | [**EmbedContentRequest**](EmbedContentRequest.md)|  | 

### Return type

[**EmbedContentResponse**](EmbedContentResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generative_service_generate_answer**
> GenerateAnswerResponse generative_service_generate_answer(model, generate_answer_request)

Generates a grounded answer from the model given an input
 `GenerateAnswerRequest`.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.generate_answer_request import GenerateAnswerRequest
from openapi_client.models.generate_answer_response import GenerateAnswerResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://generativelanguage.googleapis.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://generativelanguage.googleapis.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.GenerativeServiceApi(api_client)
    model = 'model_example' # str | The model id.
    generate_answer_request = openapi_client.GenerateAnswerRequest() # GenerateAnswerRequest | 

    try:
        api_response = api_instance.generative_service_generate_answer(model, generate_answer_request)
        print("The response of GenerativeServiceApi->generative_service_generate_answer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenerativeServiceApi->generative_service_generate_answer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | **str**| The model id. | 
 **generate_answer_request** | [**GenerateAnswerRequest**](GenerateAnswerRequest.md)|  | 

### Return type

[**GenerateAnswerResponse**](GenerateAnswerResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generative_service_generate_dynamic_content**
> GenerateContentResponse generative_service_generate_dynamic_content(dynamic, generate_content_request)

Generates a model response for a dynamic model.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.generate_content_request import GenerateContentRequest
from openapi_client.models.generate_content_response import GenerateContentResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://generativelanguage.googleapis.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://generativelanguage.googleapis.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.GenerativeServiceApi(api_client)
    dynamic = 'dynamic_example' # str | The dynamic id.
    generate_content_request = openapi_client.GenerateContentRequest() # GenerateContentRequest | 

    try:
        api_response = api_instance.generative_service_generate_dynamic_content(dynamic, generate_content_request)
        print("The response of GenerativeServiceApi->generative_service_generate_dynamic_content:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenerativeServiceApi->generative_service_generate_dynamic_content: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dynamic** | **str**| The dynamic id. | 
 **generate_content_request** | [**GenerateContentRequest**](GenerateContentRequest.md)|  | 

### Return type

[**GenerateContentResponse**](GenerateContentResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generative_service_generate_model_content**
> GenerateContentResponse generative_service_generate_model_content(model, generate_content_request)

Generates a model response for a standard model.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.generate_content_request import GenerateContentRequest
from openapi_client.models.generate_content_response import GenerateContentResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://generativelanguage.googleapis.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://generativelanguage.googleapis.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.GenerativeServiceApi(api_client)
    model = 'model_example' # str | The model id.
    generate_content_request = openapi_client.GenerateContentRequest() # GenerateContentRequest | 

    try:
        api_response = api_instance.generative_service_generate_model_content(model, generate_content_request)
        print("The response of GenerativeServiceApi->generative_service_generate_model_content:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenerativeServiceApi->generative_service_generate_model_content: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | **str**| The model id. | 
 **generate_content_request** | [**GenerateContentRequest**](GenerateContentRequest.md)|  | 

### Return type

[**GenerateContentResponse**](GenerateContentResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generative_service_generate_tuned_model_content**
> GenerateContentResponse generative_service_generate_tuned_model_content(tuned_model, generate_content_request)

Generates a model response for a tuned model.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.generate_content_request import GenerateContentRequest
from openapi_client.models.generate_content_response import GenerateContentResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://generativelanguage.googleapis.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://generativelanguage.googleapis.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.GenerativeServiceApi(api_client)
    tuned_model = 'tuned_model_example' # str | The tunedModel id.
    generate_content_request = openapi_client.GenerateContentRequest() # GenerateContentRequest | 

    try:
        api_response = api_instance.generative_service_generate_tuned_model_content(tuned_model, generate_content_request)
        print("The response of GenerativeServiceApi->generative_service_generate_tuned_model_content:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenerativeServiceApi->generative_service_generate_tuned_model_content: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tuned_model** | **str**| The tunedModel id. | 
 **generate_content_request** | [**GenerateContentRequest**](GenerateContentRequest.md)|  | 

### Return type

[**GenerateContentResponse**](GenerateContentResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generative_service_stream_generate_dynamic_content**
> GenerateContentResponse generative_service_stream_generate_dynamic_content(dynamic, generate_content_request)

Generates a streamed response from a dynamic model.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.generate_content_request import GenerateContentRequest
from openapi_client.models.generate_content_response import GenerateContentResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://generativelanguage.googleapis.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://generativelanguage.googleapis.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.GenerativeServiceApi(api_client)
    dynamic = 'dynamic_example' # str | The dynamic id.
    generate_content_request = openapi_client.GenerateContentRequest() # GenerateContentRequest | 

    try:
        api_response = api_instance.generative_service_stream_generate_dynamic_content(dynamic, generate_content_request)
        print("The response of GenerativeServiceApi->generative_service_stream_generate_dynamic_content:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenerativeServiceApi->generative_service_stream_generate_dynamic_content: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dynamic** | **str**| The dynamic id. | 
 **generate_content_request** | [**GenerateContentRequest**](GenerateContentRequest.md)|  | 

### Return type

[**GenerateContentResponse**](GenerateContentResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generative_service_stream_generate_model_content**
> GenerateContentResponse generative_service_stream_generate_model_content(model, generate_content_request)

Generates a streamed response from a standard model.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.generate_content_request import GenerateContentRequest
from openapi_client.models.generate_content_response import GenerateContentResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://generativelanguage.googleapis.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://generativelanguage.googleapis.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.GenerativeServiceApi(api_client)
    model = 'model_example' # str | The model id.
    generate_content_request = openapi_client.GenerateContentRequest() # GenerateContentRequest | 

    try:
        api_response = api_instance.generative_service_stream_generate_model_content(model, generate_content_request)
        print("The response of GenerativeServiceApi->generative_service_stream_generate_model_content:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenerativeServiceApi->generative_service_stream_generate_model_content: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | **str**| The model id. | 
 **generate_content_request** | [**GenerateContentRequest**](GenerateContentRequest.md)|  | 

### Return type

[**GenerateContentResponse**](GenerateContentResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generative_service_stream_generate_tuned_model_content**
> GenerateContentResponse generative_service_stream_generate_tuned_model_content(tuned_model, generate_content_request)

Generates a streamed response from a tuned model.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.generate_content_request import GenerateContentRequest
from openapi_client.models.generate_content_response import GenerateContentResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://generativelanguage.googleapis.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://generativelanguage.googleapis.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.GenerativeServiceApi(api_client)
    tuned_model = 'tuned_model_example' # str | The tunedModel id.
    generate_content_request = openapi_client.GenerateContentRequest() # GenerateContentRequest | 

    try:
        api_response = api_instance.generative_service_stream_generate_tuned_model_content(tuned_model, generate_content_request)
        print("The response of GenerativeServiceApi->generative_service_stream_generate_tuned_model_content:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenerativeServiceApi->generative_service_stream_generate_tuned_model_content: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tuned_model** | **str**| The tunedModel id. | 
 **generate_content_request** | [**GenerateContentRequest**](GenerateContentRequest.md)|  | 

### Return type

[**GenerateContentResponse**](GenerateContentResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

