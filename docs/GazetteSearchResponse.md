# GazetteSearchResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_gazettes** | **int** |  | 
**gazettes** | [**List[GazetteItem]**](GazetteItem.md) |  | 

## Example

```python
from openapi_client.models.gazette_search_response import GazetteSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GazetteSearchResponse from a JSON string
gazette_search_response_instance = GazetteSearchResponse.from_json(json)
# print the JSON string representation of the object
print GazetteSearchResponse.to_json()

# convert the object into a dict
gazette_search_response_dict = gazette_search_response_instance.to_dict()
# create an instance of GazetteSearchResponse from a dict
gazette_search_response_form_dict = gazette_search_response.from_dict(gazette_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


