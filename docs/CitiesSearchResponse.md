# CitiesSearchResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cities** | [**List[City]**](City.md) |  | 

## Example

```python
from openapi_client.models.cities_search_response import CitiesSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CitiesSearchResponse from a JSON string
cities_search_response_instance = CitiesSearchResponse.from_json(json)
# print the JSON string representation of the object
print CitiesSearchResponse.to_json()

# convert the object into a dict
cities_search_response_dict = cities_search_response_instance.to_dict()
# create an instance of CitiesSearchResponse from a dict
cities_search_response_form_dict = cities_search_response.from_dict(cities_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


