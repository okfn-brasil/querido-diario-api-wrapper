# GazetteItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**territory_id** | **str** |  | 
**var_date** | **date** |  | 
**scraped_at** | **datetime** |  | 
**url** | **str** |  | 
**territory_name** | **str** |  | 
**state_code** | **str** |  | 
**excerpts** | **List[str]** |  | 
**edition** | **str** |  | [optional] 
**is_extra_edition** | **bool** |  | [optional] 
**txt_url** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.gazette_item import GazetteItem

# TODO update the JSON string below
json = "{}"
# create an instance of GazetteItem from a JSON string
gazette_item_instance = GazetteItem.from_json(json)
# print the JSON string representation of the object
print GazetteItem.to_json()

# convert the object into a dict
gazette_item_dict = gazette_item_instance.to_dict()
# create an instance of GazetteItem from a dict
gazette_item_form_dict = gazette_item.from_dict(gazette_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


