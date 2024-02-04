# ThemedExcerptItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**territory_id** | **str** |  | 
**var_date** | **date** |  | 
**scraped_at** | **datetime** |  | 
**url** | **str** |  | 
**territory_name** | **str** |  | 
**state_code** | **str** |  | 
**excerpt** | **str** |  | 
**subthemes** | **List[str]** |  | 
**entities** | **List[str]** |  | [optional] 
**edition** | **str** |  | [optional] 
**is_extra_edition** | **bool** |  | [optional] 
**txt_url** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.themed_excerpt_item import ThemedExcerptItem

# TODO update the JSON string below
json = "{}"
# create an instance of ThemedExcerptItem from a JSON string
themed_excerpt_item_instance = ThemedExcerptItem.from_json(json)
# print the JSON string representation of the object
print ThemedExcerptItem.to_json()

# convert the object into a dict
themed_excerpt_item_dict = themed_excerpt_item_instance.to_dict()
# create an instance of ThemedExcerptItem from a dict
themed_excerpt_item_form_dict = themed_excerpt_item.from_dict(themed_excerpt_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


