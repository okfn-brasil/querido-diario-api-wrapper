# HTTPExceptionMessage


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail** | **str** |  | 

## Example

```python
from openapi_client.models.http_exception_message import HTTPExceptionMessage

# TODO update the JSON string below
json = "{}"
# create an instance of HTTPExceptionMessage from a JSON string
http_exception_message_instance = HTTPExceptionMessage.from_json(json)
# print the JSON string representation of the object
print HTTPExceptionMessage.to_json()

# convert the object into a dict
http_exception_message_dict = http_exception_message_instance.to_dict()
# create an instance of HTTPExceptionMessage from a dict
http_exception_message_form_dict = http_exception_message.from_dict(http_exception_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


