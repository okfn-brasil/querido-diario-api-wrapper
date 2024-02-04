# ThemedExcerptSearchResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_excerpts** | **int** |  | 
**excerpts** | [**List[ThemedExcerptItem]**](ThemedExcerptItem.md) |  | 

## Example

```python
from openapi_client.models.themed_excerpt_search_response import ThemedExcerptSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ThemedExcerptSearchResponse from a JSON string
themed_excerpt_search_response_instance = ThemedExcerptSearchResponse.from_json(json)
# print the JSON string representation of the object
print ThemedExcerptSearchResponse.to_json()

# convert the object into a dict
themed_excerpt_search_response_dict = themed_excerpt_search_response_instance.to_dict()
# create an instance of ThemedExcerptSearchResponse from a dict
themed_excerpt_search_response_form_dict = themed_excerpt_search_response.from_dict(themed_excerpt_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


