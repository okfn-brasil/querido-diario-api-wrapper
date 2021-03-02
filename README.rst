==========================
Querido Diário API Wrapper
==========================

*******
Install
*******

.. code-block:: shell

   pip install querido-diario-api-wrapper

*****
Usage
*****

.. code-block:: python

   import querido_diario

   # Returns all gazettes between 01/01/2020 and 31/01/2021 that contains the words
   # 'covid' and 'cloroquina' from territory '2408102' (Natal-RN)
   gazettes = querido_diario.gazettes(
      since="2020-01-01",
      until="2021-01-31",
      keywords=["covid", "cloroquina],
      territory_id="1302603",
      offset=0,
      size=10
   )

   # Returns list of all territories available in the API
   querido_diario.TERRITORIES

Response
========

.. code-block:: json

  {
    "total_gazettes": 1,
    "gazettes": [
      {
        "territory_id": "2408102",
        "date": "2020-07-31",
        "url": "https://querido-diario.nyc3.cdn.digitaloceanspaces.com/2408102/2020-07-31/64e13a14bfe1f03b39cfe9d4a194070539fd6fe3.pdf",
        "territory_name": "Natal",
        "state_code": "RN",
        "is_extra_edition": false
      }
    ]
  }