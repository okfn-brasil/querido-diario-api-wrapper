# Partner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cnpj_basico** | **str** |  | 
**cnpj_ordem** | **str** |  | 
**cnpj_dv** | **str** |  | 
**cnpj_completo** | **str** |  | 
**cnpj_completo_apenas_numeros** | **str** |  | 
**identificador_socio** | **str** |  | [optional] 
**razao_social** | **str** |  | [optional] 
**cnpj_cpf_socio** | **str** |  | [optional] 
**qualificacao_socio** | **str** |  | [optional] 
**data_entrada_sociedade** | **str** |  | [optional] 
**pais_socio_estrangeiro** | **str** |  | [optional] 
**numero_cpf_representante_legal** | **str** |  | [optional] 
**nome_representante_legal** | **str** |  | [optional] 
**qualificacao_representante_legal** | **str** |  | [optional] 
**faixa_etaria** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.partner import Partner

# TODO update the JSON string below
json = "{}"
# create an instance of Partner from a JSON string
partner_instance = Partner.from_json(json)
# print the JSON string representation of the object
print Partner.to_json()

# convert the object into a dict
partner_dict = partner_instance.to_dict()
# create an instance of Partner from a dict
partner_form_dict = partner.from_dict(partner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


