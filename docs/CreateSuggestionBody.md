# CreateSuggestionBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email_address** | **str** | Email address who is sending email | 
**name** | **str** | Name who is sending email | 
**content** | **str** | Email content with suggestion | 

## Example

```python
from openapi_client.models.create_suggestion_body import CreateSuggestionBody

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSuggestionBody from a JSON string
create_suggestion_body_instance = CreateSuggestionBody.from_json(json)
# print the JSON string representation of the object
print CreateSuggestionBody.to_json()

# convert the object into a dict
create_suggestion_body_dict = create_suggestion_body_instance.to_dict()
# create an instance of CreateSuggestionBody from a dict
create_suggestion_body_form_dict = create_suggestion_body.from_dict(create_suggestion_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


