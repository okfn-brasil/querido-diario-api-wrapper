# City


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**territory_id** | **str** |  | 
**territory_name** | **str** |  | 
**state_code** | **str** |  | 
**publication_urls** | **List[str]** |  | [optional] 
**level** | [**CityLevel**](CityLevel.md) |  | 

## Example

```python
from openapi_client.models.city import City

# TODO update the JSON string below
json = "{}"
# create an instance of City from a JSON string
city_instance = City.from_json(json)
# print the JSON string representation of the object
print City.to_json()

# convert the object into a dict
city_dict = city_instance.to_dict()
# create an instance of City from a dict
city_form_dict = city.from_dict(city_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


