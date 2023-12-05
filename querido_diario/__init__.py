import requests
# import json

BASE_API_URL = "https://queridodiario.ok.org.br/api/"

# endpoints (EPs)
EP_GAZETTES = "gazettes"

RESPONSE_GAZETTE_KEY = "gazettes"
RESPONSE_TOTAL_GAZETTES_KEY = "total_gazettes"


# TODO: verificar se segue funcionando gazettes()
# TODO: criar testes unitários

def gazettes(
    since=None, until=None, keywords=None, territory_ids=None, offset=0, size=10
):
    endpoint = "gazettes"
    if territory_id is not None:
        endpoint = f"gazettes/{territory_id}"

    payload = [
        f"offset={offset}",
        f"size={size}",
    ]
    if since is not None:
        payload.append(f"since={since}")
    if until is not None:
        payload.append(f"until={until}")
    if keywords is not None:
        for keyword in keywords:
            payload.append(f"keywords={keyword}")
    url_params = "&".join(payload)
    response = requests.get(f"{BASE_API_URL}{endpoint}?{url_params}")
    response.raise_for_status()

    return response.json()


def available_cities():
    ''' (None) -> list
    '''
    endpoint = "cities"
    url_params = "levels=3"
    response = requests.get(f"{BASE_API_URL}{endpoint}?{url_params}")
    response.raise_for_status()

    return response.json()['cities']


def available_cities_codes():
    ''' (None) -> list
    '''
    cities_list = available_cities()
    ibge_codes = []

    for i in range(len(cities_list)):
        ibge_codes.append(cities_list[i]['territory_id'])

    return ibge_codes


def _limit_edition(territory_id, sort_by, size):
    ''' str, str -> dict
    '''
    endpoint = "gazettes"

    payload = [
        f"territory_ids={territory_id}",
        "number_of_excerpts=1",
        f"size={size}",
        f"sort_by={sort_by}"
    ]
    url_params = "&".join(payload)
    response = requests.get(f"{BASE_API_URL}{endpoint}?{url_params}")
    response.raise_for_status()

    return response.json()['gazettes'][0]


def newest_edition(territory_id):
    ''' str -> dict
    '''
    return _limit_edition(territory_id, "descending_date", 1)


def oldest_edition(territory_id):
    ''' str -> dict
    '''
    return _limit_edition(territory_id, "ascending_date", 1)


def publication_frequency(territory_id):
    recent_editions = _limit_edition(territory_id, "descending_date", 10)
    # calcula o delta de cada intervalo dessas 10 edições
    # calcula média
    pass

def gazette_date_validation(territory_id, published_date):
    '''
    '''
    payload = [
        f"territory_ids={territory_id}",
        f"published_since={published_date}",
        f"published_until={published_date}",
        "number_of_excerpts=1"
    ]
    url_params = "&".join(payload)
    response = requests.get(f"{BASE_API_URL}{EP_GAZETTES}?{url_params}")
    response.raise_for_status()

    if response.json()[RESPONSE_TOTAL_GAZETTES_KEY] > 0:
        return True #, response.json()[RESPONSE_GAZETTE_KEY]
    return False #, response.json()[RESPONSE_GAZETTE_KEY]
    
def _get_from_item():
    pass

def get_edition_number(itens):
    ''' (list) -> list
    '''
    return [item["edition"] for item in itens]

    