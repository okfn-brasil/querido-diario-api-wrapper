# CompanySearchResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cnpj_info** | [**Company**](Company.md) |  | 

## Example

```python
from openapi_client.models.company_search_response import CompanySearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CompanySearchResponse from a JSON string
company_search_response_instance = CompanySearchResponse.from_json(json)
# print the JSON string representation of the object
print CompanySearchResponse.to_json()

# convert the object into a dict
company_search_response_dict = company_search_response_instance.to_dict()
# create an instance of CompanySearchResponse from a dict
company_search_response_form_dict = company_search_response.from_dict(company_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


