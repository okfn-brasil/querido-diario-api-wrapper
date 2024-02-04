# openapi_client.DefaultApi

All URIs are relative to *https://queridodiario.ok.org.br/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_available_entities_of_a_theme_gazettes_by_theme_entities_theme_get**](DefaultApi.md#get_all_available_entities_of_a_theme_gazettes_by_theme_entities_theme_get) | **GET** /gazettes/by_theme/entities/{theme} | Get All Available Entities Of A Theme
[**get_all_available_subthemes_of_a_theme_gazettes_by_theme_subthemes_theme_get**](DefaultApi.md#get_all_available_subthemes_of_a_theme_gazettes_by_theme_subthemes_theme_get) | **GET** /gazettes/by_theme/subthemes/{theme} | Get All Available Subthemes Of A Theme
[**get_all_available_themes_gazettes_by_theme_themes_get**](DefaultApi.md#get_all_available_themes_gazettes_by_theme_themes_get) | **GET** /gazettes/by_theme/themes/ | Get All Available Themes
[**get_city_by_ibgeid_cities_territory_id_get**](DefaultApi.md#get_city_by_ibgeid_cities_territory_id_get) | **GET** /cities/{territory_id} | Get City By Ibge Id
[**get_company_info_by_cnpj_number_company_info_cnpj_get**](DefaultApi.md#get_company_info_by_cnpj_number_company_info_cnpj_get) | **GET** /company/info/{cnpj} | Get Company Info By Cnpj Number
[**get_company_partners_infos_by_cnpj_number_company_partners_cnpj_get**](DefaultApi.md#get_company_partners_infos_by_cnpj_number_company_partners_cnpj_get) | **GET** /company/partners/{cnpj} | Get Company Partners Infos By Cnpj Number
[**search_for_cities_by_name_cities_get**](DefaultApi.md#search_for_cities_by_name_cities_get) | **GET** /cities | Search For Cities By Name.
[**search_for_content_in_gazette_excerpts_associated_with_a_theme_gazettes_by_theme_theme_get**](DefaultApi.md#search_for_content_in_gazette_excerpts_associated_with_a_theme_gazettes_by_theme_theme_get) | **GET** /gazettes/by_theme/{theme} | Search For Content In Gazette Excerpts Associated With A Theme
[**search_for_content_in_gazettes_gazettes_get**](DefaultApi.md#search_for_content_in_gazettes_gazettes_get) | **GET** /gazettes | Search For Content In Gazettes
[**send_a_suggestion_suggestions_post**](DefaultApi.md#send_a_suggestion_suggestions_post) | **POST** /suggestions | Send A Suggestion


# **get_all_available_entities_of_a_theme_gazettes_by_theme_entities_theme_get**
> EntitiesSearchResponse get_all_available_entities_of_a_theme_gazettes_by_theme_entities_theme_get(theme)

Get All Available Entities Of A Theme

Get all available entities of a theme that can be used to search in gazettes by theme and further filtering by entities.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.entities_search_response import EntitiesSearchResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://queridodiario.ok.org.br/api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://queridodiario.ok.org.br/api"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    theme = 'theme_example' # str | Theme that can be used to search in gazettes by theme.

    try:
        # Get All Available Entities Of A Theme
        api_response = api_instance.get_all_available_entities_of_a_theme_gazettes_by_theme_entities_theme_get(theme)
        print("The response of DefaultApi->get_all_available_entities_of_a_theme_gazettes_by_theme_entities_theme_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_all_available_entities_of_a_theme_gazettes_by_theme_entities_theme_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **theme** | **str**| Theme that can be used to search in gazettes by theme. | 

### Return type

[**EntitiesSearchResponse**](EntitiesSearchResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Theme not found. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_available_subthemes_of_a_theme_gazettes_by_theme_subthemes_theme_get**
> SubthemesSearchResponse get_all_available_subthemes_of_a_theme_gazettes_by_theme_subthemes_theme_get(theme)

Get All Available Subthemes Of A Theme

Get all available subthemes of a theme that can be used to search in gazettes by theme and further filtering by subthemes.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.subthemes_search_response import SubthemesSearchResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://queridodiario.ok.org.br/api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://queridodiario.ok.org.br/api"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    theme = 'theme_example' # str | Theme that can be used to search in gazettes by theme.

    try:
        # Get All Available Subthemes Of A Theme
        api_response = api_instance.get_all_available_subthemes_of_a_theme_gazettes_by_theme_subthemes_theme_get(theme)
        print("The response of DefaultApi->get_all_available_subthemes_of_a_theme_gazettes_by_theme_subthemes_theme_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_all_available_subthemes_of_a_theme_gazettes_by_theme_subthemes_theme_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **theme** | **str**| Theme that can be used to search in gazettes by theme. | 

### Return type

[**SubthemesSearchResponse**](SubthemesSearchResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Theme not found. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_available_themes_gazettes_by_theme_themes_get**
> ThemesSearchResponse get_all_available_themes_gazettes_by_theme_themes_get()

Get All Available Themes

Get all available themes that can be used to search in gazettes by theme.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.themes_search_response import ThemesSearchResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://queridodiario.ok.org.br/api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://queridodiario.ok.org.br/api"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        # Get All Available Themes
        api_response = api_instance.get_all_available_themes_gazettes_by_theme_themes_get()
        print("The response of DefaultApi->get_all_available_themes_gazettes_by_theme_themes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_all_available_themes_gazettes_by_theme_themes_get: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**ThemesSearchResponse**](ThemesSearchResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_city_by_ibgeid_cities_territory_id_get**
> CitySearchResponse get_city_by_ibgeid_cities_territory_id_get(territory_id)

Get City By Ibge Id

Get general info from specific city with 7-digit IBGE ID.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.city_search_response import CitySearchResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://queridodiario.ok.org.br/api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://queridodiario.ok.org.br/api"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    territory_id = 'territory_id_example' # str | City's 7-digit IBGE ID.

    try:
        # Get City By Ibge Id
        api_response = api_instance.get_city_by_ibgeid_cities_territory_id_get(territory_id)
        print("The response of DefaultApi->get_city_by_ibgeid_cities_territory_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_city_by_ibgeid_cities_territory_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **territory_id** | **str**| City&#39;s 7-digit IBGE ID. | 

### Return type

[**CitySearchResponse**](CitySearchResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | City not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_info_by_cnpj_number_company_info_cnpj_get**
> CompanySearchResponse get_company_info_by_cnpj_number_company_info_cnpj_get(cnpj)

Get Company Info By Cnpj Number

Get info from specific company by its CNPJ number.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.company_search_response import CompanySearchResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://queridodiario.ok.org.br/api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://queridodiario.ok.org.br/api"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    cnpj = 'cnpj_example' # str | Company's CNPJ number (may include non-digit characters).

    try:
        # Get Company Info By Cnpj Number
        api_response = api_instance.get_company_info_by_cnpj_number_company_info_cnpj_get(cnpj)
        print("The response of DefaultApi->get_company_info_by_cnpj_number_company_info_cnpj_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_company_info_by_cnpj_number_company_info_cnpj_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cnpj** | **str**| Company&#39;s CNPJ number (may include non-digit characters). | 

### Return type

[**CompanySearchResponse**](CompanySearchResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Company not found. |  -  |
**400** | CNPJ is not valid. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_partners_infos_by_cnpj_number_company_partners_cnpj_get**
> PartnersSearchResponse get_company_partners_infos_by_cnpj_number_company_partners_cnpj_get(cnpj)

Get Company Partners Infos By Cnpj Number

Get info of partners of a company by its CNPJ number.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.partners_search_response import PartnersSearchResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://queridodiario.ok.org.br/api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://queridodiario.ok.org.br/api"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    cnpj = 'cnpj_example' # str | Company's CNPJ number (may include non-digit characters).

    try:
        # Get Company Partners Infos By Cnpj Number
        api_response = api_instance.get_company_partners_infos_by_cnpj_number_company_partners_cnpj_get(cnpj)
        print("The response of DefaultApi->get_company_partners_infos_by_cnpj_number_company_partners_cnpj_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_company_partners_infos_by_cnpj_number_company_partners_cnpj_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cnpj** | **str**| Company&#39;s CNPJ number (may include non-digit characters). | 

### Return type

[**PartnersSearchResponse**](PartnersSearchResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | CNPJ is not valid. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_for_cities_by_name_cities_get**
> CitiesSearchResponse search_for_cities_by_name_cities_get(city_name=city_name, levels=levels)

Search For Cities By Name.

Search for cities with a name similar to the city_name query.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.cities_search_response import CitiesSearchResponse
from openapi_client.models.city_level import CityLevel
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://queridodiario.ok.org.br/api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://queridodiario.ok.org.br/api"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    city_name = '' # str | Search for cities with a similar name (empty field returns all cities). (optional) (default to '')
    levels = [""] # List[CityLevel] | Search for cities within the same openness level (empty field returns from all levels) (optional) (default to [""])

    try:
        # Search For Cities By Name.
        api_response = api_instance.search_for_cities_by_name_cities_get(city_name=city_name, levels=levels)
        print("The response of DefaultApi->search_for_cities_by_name_cities_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->search_for_cities_by_name_cities_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **city_name** | **str**| Search for cities with a similar name (empty field returns all cities). | [optional] [default to &#39;&#39;]
 **levels** | [**List[CityLevel]**](CityLevel.md)| Search for cities within the same openness level (empty field returns from all levels) | [optional] [default to [&quot;&quot;]]

### Return type

[**CitiesSearchResponse**](CitiesSearchResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_for_content_in_gazette_excerpts_associated_with_a_theme_gazettes_by_theme_theme_get**
> ThemedExcerptSearchResponse search_for_content_in_gazette_excerpts_associated_with_a_theme_gazettes_by_theme_theme_get(theme, entities=entities, subthemes=subthemes, territory_ids=territory_ids, published_since=published_since, published_until=published_until, scraped_since=scraped_since, scraped_until=scraped_until, querystring=querystring, pre_tags=pre_tags, post_tags=post_tags, size=size, offset=offset, sort_by=sort_by)

Search For Content In Gazette Excerpts Associated With A Theme

Search for content in excerpts from available cities that are related to an available theme. Each search result is an excerpt from a gazette.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.themed_excerpt_search_response import ThemedExcerptSearchResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://queridodiario.ok.org.br/api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://queridodiario.ok.org.br/api"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    theme = 'theme_example' # str | Search in excerpts from gazettes that are associated to the given theme.
    entities = [] # List[str] | Search in excerpts which contains any of the given entities (entities are theme-specific). (optional) (default to [])
    subthemes = [] # List[str] | Search in excerpts which contains any of the given subthemes (subthemes are theme-specific). (optional) (default to [])
    territory_ids = [] # List[str] | Search in excerpts from gazettes published by cities with the given 7-digit IBGE IDs (an empty field searches in all available cities). (optional) (default to [])
    published_since = '2013-10-20' # date | Search in excerpts from gazettes published on given date or after (format: YYYY-MM-DD). (optional)
    published_until = '2013-10-20' # date | Search in excerpts from gazettes published on given date or before (format: YYYY-MM-DD). (optional)
    scraped_since = '2013-10-20T19:20:30+01:00' # datetime | Search in excerpts from gazettes scraped on given datetime or after (format: YYYY-MM-DDTHH:MM:SS). (optional)
    scraped_until = '2013-10-20T19:20:30+01:00' # datetime | Search in excerpts from gazettes scraped on given datetime or before (format: YYYY-MM-DDTHH:MM:SS). (optional)
    querystring = '' # str | Search in excerpts using OpenSearch's \"simple query string syntax\". (optional) (default to '')
    pre_tags = [""] # List[str] | List of strings (usually HTML tags) to be inserted before the text which matches the query in the excerpts. (optional) (default to [""])
    post_tags = [""] # List[str] | List of strings (usually HTML tags) to be inserted after the text which matches the query in the excerpts. (optional) (default to [""])
    size = 10 # int | Maximum number of results to be returned in the response (use with caution). (optional) (default to 10)
    offset = 0 # int | Number of search results to be skipped in the response. (optional) (default to 0)
    sort_by = openapi_client.SortBy() # SortBy | How to sort the search results. (optional)

    try:
        # Search For Content In Gazette Excerpts Associated With A Theme
        api_response = api_instance.search_for_content_in_gazette_excerpts_associated_with_a_theme_gazettes_by_theme_theme_get(theme, entities=entities, subthemes=subthemes, territory_ids=territory_ids, published_since=published_since, published_until=published_until, scraped_since=scraped_since, scraped_until=scraped_until, querystring=querystring, pre_tags=pre_tags, post_tags=post_tags, size=size, offset=offset, sort_by=sort_by)
        print("The response of DefaultApi->search_for_content_in_gazette_excerpts_associated_with_a_theme_gazettes_by_theme_theme_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->search_for_content_in_gazette_excerpts_associated_with_a_theme_gazettes_by_theme_theme_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **theme** | **str**| Search in excerpts from gazettes that are associated to the given theme. | 
 **entities** | [**List[str]**](str.md)| Search in excerpts which contains any of the given entities (entities are theme-specific). | [optional] [default to []]
 **subthemes** | [**List[str]**](str.md)| Search in excerpts which contains any of the given subthemes (subthemes are theme-specific). | [optional] [default to []]
 **territory_ids** | [**List[str]**](str.md)| Search in excerpts from gazettes published by cities with the given 7-digit IBGE IDs (an empty field searches in all available cities). | [optional] [default to []]
 **published_since** | **date**| Search in excerpts from gazettes published on given date or after (format: YYYY-MM-DD). | [optional] 
 **published_until** | **date**| Search in excerpts from gazettes published on given date or before (format: YYYY-MM-DD). | [optional] 
 **scraped_since** | **datetime**| Search in excerpts from gazettes scraped on given datetime or after (format: YYYY-MM-DDTHH:MM:SS). | [optional] 
 **scraped_until** | **datetime**| Search in excerpts from gazettes scraped on given datetime or before (format: YYYY-MM-DDTHH:MM:SS). | [optional] 
 **querystring** | **str**| Search in excerpts using OpenSearch&#39;s \&quot;simple query string syntax\&quot;. | [optional] [default to &#39;&#39;]
 **pre_tags** | [**List[str]**](str.md)| List of strings (usually HTML tags) to be inserted before the text which matches the query in the excerpts. | [optional] [default to [&quot;&quot;]]
 **post_tags** | [**List[str]**](str.md)| List of strings (usually HTML tags) to be inserted after the text which matches the query in the excerpts. | [optional] [default to [&quot;&quot;]]
 **size** | **int**| Maximum number of results to be returned in the response (use with caution). | [optional] [default to 10]
 **offset** | **int**| Number of search results to be skipped in the response. | [optional] [default to 0]
 **sort_by** | [**SortBy**](.md)| How to sort the search results. | [optional] 

### Return type

[**ThemedExcerptSearchResponse**](ThemedExcerptSearchResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Theme not found. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_for_content_in_gazettes_gazettes_get**
> GazetteSearchResponse search_for_content_in_gazettes_gazettes_get(territory_ids=territory_ids, published_since=published_since, published_until=published_until, scraped_since=scraped_since, scraped_until=scraped_until, querystring=querystring, excerpt_size=excerpt_size, number_of_excerpts=number_of_excerpts, pre_tags=pre_tags, post_tags=post_tags, size=size, offset=offset, sort_by=sort_by)

Search For Content In Gazettes

Search for content in published gazettes from available cities. Each search result is an individual gazette.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.gazette_search_response import GazetteSearchResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://queridodiario.ok.org.br/api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://queridodiario.ok.org.br/api"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    territory_ids = [] # List[str] | Search in gazettes published by cities with the given 7-digit IBGE IDs (an empty field searches in all available cities). (optional) (default to [])
    published_since = '2013-10-20' # date | Search in gazettes published on given date or after (format: YYYY-MM-DD). (optional)
    published_until = '2013-10-20' # date | Search in gazettes published on given date or before (format: YYYY-MM-DD). (optional)
    scraped_since = '2013-10-20T19:20:30+01:00' # datetime | Search in gazettes scraped on given datetime or after (format: YYYY-MM-DDTHH:MM:SS). (optional)
    scraped_until = '2013-10-20T19:20:30+01:00' # datetime | Search in gazettes scraped on given datetime or before (format: YYYY-MM-DDTHH:MM:SS). (optional)
    querystring = '' # str | Search in gazettes using OpenSearch's \"simple query string syntax\" (an empty field returns no excerpts, only the results metadata). (optional) (default to '')
    excerpt_size = 500 # int | Maximum number of characters that an excerpt should display (use with caution). (optional) (default to 500)
    number_of_excerpts = 1 # int | Maximum number of excerpts of a gazette to be returned (use with caution). (optional) (default to 1)
    pre_tags = [""] # List[str] | List of strings (usually HTML tags) to be inserted before the text which matches the query in the excerpts. (optional) (default to [""])
    post_tags = [""] # List[str] | List of strings (usually HTML tags) to be inserted after the text which matches the query in the excerpts. (optional) (default to [""])
    size = 10 # int | Maximum number of results to be returned in the response (use with caution). (optional) (default to 10)
    offset = 0 # int | Number of search results to be skipped in the response. (optional) (default to 0)
    sort_by = openapi_client.SortBy() # SortBy | How to sort the search results. (optional)

    try:
        # Search For Content In Gazettes
        api_response = api_instance.search_for_content_in_gazettes_gazettes_get(territory_ids=territory_ids, published_since=published_since, published_until=published_until, scraped_since=scraped_since, scraped_until=scraped_until, querystring=querystring, excerpt_size=excerpt_size, number_of_excerpts=number_of_excerpts, pre_tags=pre_tags, post_tags=post_tags, size=size, offset=offset, sort_by=sort_by)
        print("The response of DefaultApi->search_for_content_in_gazettes_gazettes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->search_for_content_in_gazettes_gazettes_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **territory_ids** | [**List[str]**](str.md)| Search in gazettes published by cities with the given 7-digit IBGE IDs (an empty field searches in all available cities). | [optional] [default to []]
 **published_since** | **date**| Search in gazettes published on given date or after (format: YYYY-MM-DD). | [optional] 
 **published_until** | **date**| Search in gazettes published on given date or before (format: YYYY-MM-DD). | [optional] 
 **scraped_since** | **datetime**| Search in gazettes scraped on given datetime or after (format: YYYY-MM-DDTHH:MM:SS). | [optional] 
 **scraped_until** | **datetime**| Search in gazettes scraped on given datetime or before (format: YYYY-MM-DDTHH:MM:SS). | [optional] 
 **querystring** | **str**| Search in gazettes using OpenSearch&#39;s \&quot;simple query string syntax\&quot; (an empty field returns no excerpts, only the results metadata). | [optional] [default to &#39;&#39;]
 **excerpt_size** | **int**| Maximum number of characters that an excerpt should display (use with caution). | [optional] [default to 500]
 **number_of_excerpts** | **int**| Maximum number of excerpts of a gazette to be returned (use with caution). | [optional] [default to 1]
 **pre_tags** | [**List[str]**](str.md)| List of strings (usually HTML tags) to be inserted before the text which matches the query in the excerpts. | [optional] [default to [&quot;&quot;]]
 **post_tags** | [**List[str]**](str.md)| List of strings (usually HTML tags) to be inserted after the text which matches the query in the excerpts. | [optional] [default to [&quot;&quot;]]
 **size** | **int**| Maximum number of results to be returned in the response (use with caution). | [optional] [default to 10]
 **offset** | **int**| Number of search results to be skipped in the response. | [optional] [default to 0]
 **sort_by** | [**SortBy**](.md)| How to sort the search results. | [optional] 

### Return type

[**GazetteSearchResponse**](GazetteSearchResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_a_suggestion_suggestions_post**
> CreatedSuggestionResponse send_a_suggestion_suggestions_post(create_suggestion_body)

Send A Suggestion

Send a suggestion to the project

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.create_suggestion_body import CreateSuggestionBody
from openapi_client.models.created_suggestion_response import CreatedSuggestionResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://queridodiario.ok.org.br/api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://queridodiario.ok.org.br/api"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    create_suggestion_body = openapi_client.CreateSuggestionBody() # CreateSuggestionBody | 

    try:
        # Send A Suggestion
        api_response = api_instance.send_a_suggestion_suggestions_post(create_suggestion_body)
        print("The response of DefaultApi->send_a_suggestion_suggestions_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->send_a_suggestion_suggestions_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_suggestion_body** | [**CreateSuggestionBody**](CreateSuggestionBody.md)|  | 

### Return type

[**CreatedSuggestionResponse**](CreatedSuggestionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

