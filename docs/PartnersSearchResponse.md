# PartnersSearchResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_partners** | **int** |  | 
**partners** | [**List[Partner]**](Partner.md) |  | 

## Example

```python
from openapi_client.models.partners_search_response import PartnersSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PartnersSearchResponse from a JSON string
partners_search_response_instance = PartnersSearchResponse.from_json(json)
# print the JSON string representation of the object
print PartnersSearchResponse.to_json()

# convert the object into a dict
partners_search_response_dict = partners_search_response_instance.to_dict()
# create an instance of PartnersSearchResponse from a dict
partners_search_response_form_dict = partners_search_response.from_dict(partners_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


