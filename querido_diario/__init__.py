import requests

__version__ = "0.0.1"


BASE_API_URL = "https://queridodiario.ok.org.br/api/"


TERRITORIES = [
    {"territory_id": "2408102", "territory_name": "Natal", "territory_state": "RN"},
    {"territory_id": "5208707", "territory_name": "Goiânia", "territory_state": "GO"},
    {"territory_id": "2927408", "territory_name": "Salvador", "territory_state": "BA"},
    {
        "territory_id": "5002704",
        "territory_name": "Campo Grande",
        "territory_state": "MS",
    },
    {
        "territory_id": "4205407",
        "territory_name": "Florianópolis",
        "territory_state": "SC",
    },
    {"territory_id": "1721000", "territory_name": "Palmas", "territory_state": "TO"},
    {
        "territory_id": "3304557",
        "territory_name": "Rio de Janeiro",
        "territory_state": "RJ",
    },
    {
        "territory_id": "2507507",
        "territory_name": "João Pessoa",
        "territory_state": "PB",
    },
    {"territory_id": "2211001", "territory_name": "Teresina", "territory_state": "PI"},
    {"territory_id": "1400100", "territory_name": "Boa Vista", "territory_state": "RR"},
    {"territory_id": "2704302", "territory_name": "Maceió", "territory_state": "AL"},
    {"territory_id": "1302603", "territory_name": "Manaus", "territory_state": "AM"},
]


def gazettes(
    since=None, until=None, keywords=None, territory_id=None, offset=0, size=10
):
    endpoint = "gazettes/"
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
