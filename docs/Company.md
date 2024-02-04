# Company


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cnpj_basico** | **str** |  | 
**cnpj_ordem** | **str** |  | 
**cnpj_dv** | **str** |  | 
**cnpj_completo** | **str** |  | 
**cnpj_completo_apenas_numeros** | **str** |  | 
**identificador_matriz_filial** | **str** |  | [optional] 
**nome_fantasia** | **str** |  | [optional] 
**situacao_cadastral** | **str** |  | [optional] 
**data_situacao_cadastral** | **str** |  | [optional] 
**motivo_situacao_cadastral** | **str** |  | [optional] 
**nome_cidade_exterior** | **str** |  | [optional] 
**data_inicio_atividade** | **str** |  | [optional] 
**cnae_fiscal_secundario** | **str** |  | [optional] 
**tipo_logradouro** | **str** |  | [optional] 
**logradouro** | **str** |  | [optional] 
**numero** | **str** |  | [optional] 
**complemento** | **str** |  | [optional] 
**bairro** | **str** |  | [optional] 
**cep** | **str** |  | [optional] 
**uf** | **str** |  | [optional] 
**ddd_telefone_1** | **str** |  | [optional] 
**ddd_telefone_2** | **str** |  | [optional] 
**ddd_telefone_fax** | **str** |  | [optional] 
**correio_eletronico** | **str** |  | [optional] 
**situacao_especial** | **str** |  | [optional] 
**data_situacao_especial** | **str** |  | [optional] 
**pais** | **str** |  | [optional] 
**municipio** | **str** |  | [optional] 
**razao_social** | **str** |  | [optional] 
**natureza_juridica** | **str** |  | [optional] 
**qualificacao_do_responsavel** | **str** |  | [optional] 
**capital_social** | **str** |  | [optional] 
**porte** | **str** |  | [optional] 
**ente_federativo_responsavel** | **str** |  | [optional] 
**opcao_pelo_simples** | **str** |  | [optional] 
**data_opcao_pelo_simples** | **str** |  | [optional] 
**data_exclusao_pelo_simples** | **str** |  | [optional] 
**opcao_pelo_mei** | **str** |  | [optional] 
**data_opcao_pelo_mei** | **str** |  | [optional] 
**data_exclusao_pelo_mei** | **str** |  | [optional] 
**cnae** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.company import Company

# TODO update the JSON string below
json = "{}"
# create an instance of Company from a JSON string
company_instance = Company.from_json(json)
# print the JSON string representation of the object
print Company.to_json()

# convert the object into a dict
company_dict = company_instance.to_dict()
# create an instance of Company from a dict
company_form_dict = company.from_dict(company_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


