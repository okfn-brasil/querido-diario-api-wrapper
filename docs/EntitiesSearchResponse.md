# EntitiesSearchResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entities** | [**List[Entity]**](Entity.md) |  | 

## Example

```python
from openapi_client.models.entities_search_response import EntitiesSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EntitiesSearchResponse from a JSON string
entities_search_response_instance = EntitiesSearchResponse.from_json(json)
# print the JSON string representation of the object
print EntitiesSearchResponse.to_json()

# convert the object into a dict
entities_search_response_dict = entities_search_response_instance.to_dict()
# create an instance of EntitiesSearchResponse from a dict
entities_search_response_form_dict = entities_search_response.from_dict(entities_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


