==========================
Querido Diário API Wrapper
==========================

*****
Sobre
*****

O `Querido Diário <https://queridodiario.ok.org.br/>`_ é um projeto de código aberto
da `Open Knowledge Brasil <https://www.ok.org.br/>`_ que tem como objetivo libertar e 
centralizar as informações publicadas nos diários oficiais dos municípios, hoje presas 
em PDFs obscuros de acesso complicado.

Diariamente estamos `coletando os diários <https://github.com/okfn-brasil/querido-diario>`_ 
e `processando seu conteúdo <https://github.com/okfn-brasil/querido-diario-toolbox>`_ para
obter o conteúdo de texto desses diários. O resultado desse processamento está disponível em
uma `API <https://github.com/okfn-brasil/querido-diario-api>`_.

Algumas buscas que são possíveis de se fazer nesse momento:

- Obter os Diários Oficiais de um município dentro de um período determinado de tempo e retornar o link para seus arquivos PDFs. Por exemplo, podemos buscar todos os Diários Oficiais de Natal-RN no período de 01/01/2012 até 31/01/2021;

- Obter todos os Diários Oficiais que contenham determinadas palavras-chave. Por exemplo podemos buscar todos os Diários Oficiais de Natal-RN que contenham as palavras "COVID" e "hidroxicloroquina" em toda história ou em determinado período de tempo.

A busca por palavra-chave ainda é limitada e ainda não conseguimos isolar partes dos Diários. 
Então a busca por palavras muito genéricas pode retornar uma quantidade de resultados muito grande.
Por exemplo, se procurarmos por "prefeito", é bem provável que todos os Diários contenham essa
palavra.

Este projeto fornece uma maneira mais simples de se acessar essa API e fazer consultas a ela. Conforme
a API evoluir, esse projeto também será atualizado. Para sugestões de melhorias, erros, tipos de consultas que seriam interessantes de se adicionar, abra uma Issue para que possa ser avaliado.

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
      keywords=["covid", "cloroquina"],
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
