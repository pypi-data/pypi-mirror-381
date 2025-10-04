# ModelSchema

The `Schema` object allows the definition of input and output data types.  These types can be objects, but also primitives and arrays.  Represents a select subset of an [OpenAPI 3.0 schema  object](https://spec.openapis.org/oas/v3.0.3#schema).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** | Required. Data type. | 
**format** | **str** | Optional. The format of the data. This is used only for primitive  datatypes. Supported formats:   for NUMBER type: float, double   for INTEGER type: int32, int64   for STRING type: enum, date-time | [optional] 
**title** | **str** | Optional. The title of the schema. | [optional] 
**description** | **str** | Optional. A brief description of the parameter. This could contain examples  of use. Parameter description may be formatted as Markdown. | [optional] 
**nullable** | **bool** | Optional. Indicates if the value may be null. | [optional] 
**enum** | **List[str]** | Optional. Possible values of the element of Type.STRING with enum format.  For example we can define an Enum Direction as :  {type:STRING, format:enum, enum:[\&quot;EAST\&quot;, NORTH\&quot;, \&quot;SOUTH\&quot;, \&quot;WEST\&quot;]} | [optional] 
**items** | [**ModelSchema**](ModelSchema.md) | Optional. Schema of the elements of Type.ARRAY. | [optional] 
**max_items** | **str** | Optional. Maximum number of the elements for Type.ARRAY. | [optional] 
**min_items** | **str** | Optional. Minimum number of the elements for Type.ARRAY. | [optional] 
**properties** | [**Dict[str, ModelSchema]**](ModelSchema.md) | Optional. Properties of Type.OBJECT. | [optional] 
**required** | **List[str]** | Optional. Required properties of Type.OBJECT. | [optional] 
**min_properties** | **str** | Optional. Minimum number of the properties for Type.OBJECT. | [optional] 
**max_properties** | **str** | Optional. Maximum number of the properties for Type.OBJECT. | [optional] 
**minimum** | **float** | Optional. SCHEMA FIELDS FOR TYPE INTEGER and NUMBER  Minimum value of the Type.INTEGER and Type.NUMBER | [optional] 
**maximum** | **float** | Optional. Maximum value of the Type.INTEGER and Type.NUMBER | [optional] 
**min_length** | **str** | Optional. SCHEMA FIELDS FOR TYPE STRING  Minimum length of the Type.STRING | [optional] 
**max_length** | **str** | Optional. Maximum length of the Type.STRING | [optional] 
**pattern** | **str** | Optional. Pattern of the Type.STRING to restrict a string to a regular  expression. | [optional] 
**example** | **object** | Optional. Example of the object. Will only populated when the object is the  root. | [optional] 
**any_of** | [**List[ModelSchema]**](ModelSchema.md) | Optional. The value should be validated against any (one or more) of the  subschemas in the list. | [optional] 
**property_ordering** | **List[str]** | Optional. The order of the properties.  Not a standard field in open api spec. Used to determine the order of the  properties in the response. | [optional] 
**default** | **object** | Optional. Default value of the field. Per JSON Schema, this field is  intended for documentation generators and doesn&#39;t affect validation. Thus  it&#39;s included here and ignored so that developers who send schemas with a  &#x60;default&#x60; field don&#39;t get unknown-field errors. | [optional] 

## Example

```python
from openapi_client.models.model_schema import ModelSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ModelSchema from a JSON string
model_schema_instance = ModelSchema.from_json(json)
# print the JSON string representation of the object
print(ModelSchema.to_json())

# convert the object into a dict
model_schema_dict = model_schema_instance.to_dict()
# create an instance of ModelSchema from a dict
model_schema_from_dict = ModelSchema.from_dict(model_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


