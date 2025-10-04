# Content

The base structured datatype containing multi-part content of a message.   A `Content` includes a `role` field designating the producer of the `Content`  and a `parts` field containing multi-part data that contains the content of  the message turn.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parts** | [**List[Part]**](Part.md) | Ordered &#x60;Parts&#x60; that constitute a single message. Parts may have different  MIME types. | [optional] 
**role** | **str** | Optional. The producer of the content. Must be either &#39;user&#39; or &#39;model&#39;.   Useful to set for multi-turn conversations, otherwise can be left blank  or unset. | [optional] 

## Example

```python
from openapi_client.models.content import Content

# TODO update the JSON string below
json = "{}"
# create an instance of Content from a JSON string
content_instance = Content.from_json(json)
# print the JSON string representation of the object
print(Content.to_json())

# convert the object into a dict
content_dict = content_instance.to_dict()
# create an instance of Content from a dict
content_from_dict = Content.from_dict(content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


