# CitySearchResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**city** | [**City**](City.md) |  | 

## Example

```python
from openapi_client.models.city_search_response import CitySearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CitySearchResponse from a JSON string
city_search_response_instance = CitySearchResponse.from_json(json)
# print the JSON string representation of the object
print CitySearchResponse.to_json()

# convert the object into a dict
city_search_response_dict = city_search_response_instance.to_dict()
# create an instance of CitySearchResponse from a dict
city_search_response_form_dict = city_search_response.from_dict(city_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


