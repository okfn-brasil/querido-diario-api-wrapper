[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/querido-diario-api-wrapper)](https://pypi.org/project/querido-diario-api-wrapper/)
[![PyPI](https://img.shields.io/pypi/v/querido-diario-api-wrapper)](https://pypi.org/project/querido-diario-api-wrapper/)

**Português (BR)** | [English (US)](https://github.com/okfn-brasil/querido-diario-api-wrapper/blob/main/docs/README-en-US.md) 

<p align="center">
  <a href="https://queridodiario.ok.org.br/sobre" target="_blank"> <img alt="Querido Diário" src="https://raw.githubusercontent.com/okfn-brasil/querido-diario-api-wrapper/main/docs/images/querido-diario-logo.png" width="200">
  </a>
</p>

# API wrapper
Dentro do [ecossistema do Querido Diário](https://docs.queridodiario.ok.org.br/pt-br/latest/contribuindo/guia-de-contribuicao.html#ecossistema-do-querido-diario), este repositório fornece uma **biblioteca simples para acessar e consultar a [API](https://queridodiario.ok.org.br/api/docs) do projeto**.

Conheça mais sobre as [tecnologias](https://queridodiario.ok.org.br/tecnologia) e a [história](https://queridodiario.ok.org.br/sobre) do projeto no [site do Querido Diário](https://queridodiario.ok.org.br)

# Sumário
- [Como contribuir](https://github.com/okfn-brasil/querido-diario-api-wrapper/blob/main/README.md#como-contribuir)
- [Como executar](https://github.com/okfn-brasil/querido-diario-api-wrapper/blob/main/README.md#como-executar)
  - [Exemplos de uso](https://github.com/okfn-brasil/querido-diario-api-wrapper/blob/main/README.md#exemplos-de-uso)
- [Suporte](https://github.com/okfn-brasil/querido-diario-api-wrapper/blob/main/README.md#suporte)
- [Agradecimentos](https://github.com/okfn-brasil/querido-diario-api-wrapper/blob/main/README.md#agradecimentos)
- [Open Knowledge Brasil](https://github.com/okfn-brasil/querido-diario-api-wrapper/blob/main/README.md#open-knowledge-brasil)
- [Licença](https://github.com/okfn-brasil/querido-diario-api-wrapper/blob/main/README.md#licença)

# Como contribuir
<p>  
  <a href="https://www.catarse.me/queridodiario-okbr" target="_blank"> 
    <img alt="catarse" src="https://img.shields.io/badge/Catarse-Apoie%20o%20projeto-orange?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB2ZXJzaW9uPSIxLjIiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgdmlld0JveD0iMCAwIDMyNSA0NTUiIHdpZHRoPSIzMjUiIGhlaWdodD0iNDU1Ij4KCTx0aXRsZT5sb2dvLXYtY29yLXBvc2l0aXZvLWFpPC90aXRsZT4KCTxzdHlsZT4KCQkuczAgeyBmaWxsOiAjMTdhMzM4IH0gCgkJLnMxIHsgZmlsbDogIzdkYjkzZCB9IAoJCS5zMiB7IGZpbGw6ICNmMmJmMDAgfSAKCQkuczMgeyBmaWxsOiAjZjE5MTA2IH0gCgkJLnM0IHsgZmlsbDogI2VhNjYwYiB9IAoJCS5zNSB7IGZpbGw6ICNkZTMyODEgfSAKCTwvc3R5bGU+Cgk8ZyBpZD0iTGF5ZXIgMSI+CgkJPGcgaWQ9IiZsdDtHcm91cCZndDsiPgoJCQk8cGF0aCBpZD0iJmx0O1BhdGgmZ3Q7IiBjbGFzcz0iczAiIGQ9Im01Ni40IDI1Ni40cS0xLjggMy4xLTMuNCA2LjRjLTE1LjQgMzMuMS00LjcgNjMuMSAxNC44IDkyLjQgMTEuNiAxNy40IDguNiAzNi40LTEuOSA0Ny4zLTYgNi4zLTE0LjUgOS44LTIzLjIgOS43LTQuNSAwLTkuMS0wLjktMTMuNS0zLTYuMy0yLjktMTUuMS05LjEtMjIuMi0yOC43LTguOS0yNC4yLTkuMS01MS42IDIuNi03Ni44IDEwLjEtMjEuNiAyNi45LTM3LjggNDYuOC00Ny4zeiIvPgoJCQk8cGF0aCBpZD0iJmx0O1BhdGgmZ3Q7IiBjbGFzcz0iczEiIGQ9Im00Ni41IDMwNS44YzAuNSAyLjYgMSA1LjIgMS43IDcuOCAxMC41IDM4LjcgNDAuNyA1Ni41IDc3LjggNjcuNCAyMi4xIDYuNSAzMyAyNC43IDMxLjkgNDEuMi0wLjcgOS42LTUuMyAxOC41LTEyLjcgMjQuNi0zLjggMy4yLTguNCA1LjctMTMuNSA3LTcuNCAyLTE5LjIgMy0zOS4xLTguNC0yNC41LTE0LjItNDQuMS0zNy4yLTUyLTY2LjctNi44LTI1LjItNC4xLTUwLjggNS45LTcyLjl6Ii8+CgkJCTxwYXRoIGlkPSImbHQ7UGF0aCZndDsiIGNsYXNzPSJzMiIgZD0ibTczLjIgMzU0LjVjMi4yIDEuOCA0LjUgMy42IDYuOSA1LjMgMzYuMiAyNS4zIDc0LjMgMTguOSAxMTMuMiAxLjggMjMuMi0xMC4xIDQ1LjMtMi41IDU2IDEyLjIgNi4zIDguNiA4LjYgMTkuNCA2LjggMjkuNy0xIDUuNC0zLjEgMTAuNy02LjUgMTUuNS00LjggNi45LTE0IDE2LjEtMzguOSAyMC41LTMwLjcgNS40LTYzLjQtMC4xLTkwLjktMTkuNC0yMy42LTE2LjUtMzkuNC0zOS45LTQ2LjYtNjUuNnoiLz4KCQkJPHBhdGggaWQ9IiZsdDtQYXRoJmd0OyIgY2xhc3M9InMzIiBkPSJtMTMwLjEgMzc2LjZxNC43IDAuMSA5LjUtMC40YzQ4LjQtNC4zIDc2LTM2LjUgOTYuNy03OC41IDEyLjQtMjUgMzYuNC0zNC4xIDU1LjgtMjkuMyAxMS40IDIuOCAyMSAxMC4yIDI2LjcgMjAuMyAzIDUuMiA1IDExLjEgNS41IDE3LjYgMC45IDkuMi0wLjQgMjMuNC0xOC4zIDQ0LjctMjIgMjYuMy01My41IDQ0LjgtOTAuMyA0OC0zMS41IDIuOC02MS40LTUuOC04NS42LTIyLjR6Ii8+CgkJCTxwYXRoIGlkPSImbHQ7UGF0aCZndDsiIGNsYXNzPSJzNCIgZD0ibTE5My42IDM1NS4xYzIuNy0yLjIgNS4zLTQuNiA3LjgtNy4xIDM3LjctMzcuOCAzOC4xLTg0LjUgMjUuOS0xMzQuNS03LjItMjkuOCA2LjUtNTQuNSAyNi4zLTY0LjIgMTEuNS01LjYgMjQuOS02LjEgMzYuOC0xLjggNi4zIDIuMyAxMi4xIDUuOSAxNy4xIDExIDcuMiA3LjEgMTYuMiAyMC4xIDE2LjMgNTAuNiAwIDM3LjctMTMuNSA3NS42LTQyLjIgMTA0LjMtMjQuNiAyNC43LTU1LjkgMzguNi04OCA0MS43eiIvPgoJCQk8cGF0aCBpZD0iJmx0O1BhdGgmZ3Q7IiBjbGFzcz0iczUiIGQ9Im0yMzEuOSAyOTJjMC44LTQuNCAxLjQtOC45IDEuOC0xMy41IDYtNjkuMi0zMi42LTExNi04Ni41LTE1NS43LTMyLjItMjMuNi0zOS4xLTU5LjYtMjcuNS04NS44IDYuNy0xNS4zIDE5LjctMjcgMzUuMi0zMi42IDguMS0yLjkgMTctNC4yIDI2LjEtMy40IDEzLjIgMS4xIDMzIDYuNSA1OC42IDM2LjkgMzEuNSAzNy41IDQ5LjcgODYuNSA0NS4xIDEzOS4xLTMuOSA0NS4xLTIzLjQgODUuMS01Mi44IDExNXoiLz4KCQk8L2c+Cgk8L2c+Cjwvc3ZnPg==">
  </a>
</p> 

Agradecemos por considerar contribuir com o Querido Diário! :tada:

Você encontra como fazê-lo no [CONTRIBUTING.md](https://github.com/okfn-brasil/querido-diario-api-wrapper/blob/main/docs/CONTRIBUTING.md)!

Além disso, consulte a [documentação do Querido Diário](https://docs.queridodiario.ok.org.br/pt-br/latest/) para te ajudar. 

# Como executar
Para utilizar a biblioteca `querido_diario` é necessário ter [Python](https://docs.python.org/3.8/) (3.8+) instalado.
1. Em um terminal aberto, obtenha a biblioteca:
```
pip install querido-diario-api-wrapper
```

2. Para usar, importe a biblioteca em seu código em Python.
```
import querido_diario
```

## Exemplos de uso

A busca por palavra-chave é limitada e ainda não conseguimos isolar as partes dos Diários. Por isso, buscar por palavras muito genéricas pode retornar uma quantidade de resultados muito grande e possivelmente pouco interessantes. Por exemplo, se procurarmos por "prefeito", é bem provável que todos os Diários contenham essa palavra.

Este projeto fornece uma maneira mais simples de se acessar essa API e fazer consultas a ela. Conforme
a API evoluir, esse projeto também será atualizado. Para sugestões de melhorias, erros, tipos de consultas que seriam interessantes de se adicionar, abra uma Issue para que possa ser avaliado.


### Consulta lista de municípios disponíveis
```
In [1]: import querido_diario

In [2]: querido_diario.TERRITORIES
```

### Consulta de palavras-chave em dado período por cidade
Armazena em `gazettes` todos os diários entre 01/01/2020 e 31/01/2021 que contêm as palavras "covid" e "cloroquina" do município de código (IBGE) `2408102` (Natal-RN)

```
In [1]: import querido_diario

In [2]: gazettes = querido_diario.gazettes(
      since="2020-01-01",
      until="2021-01-31",
      keywords=["covid", "cloroquina"],
      territory_id="1302603",
      offset=0,
      size=10
      )

In [3]: gazettes

Out[3]: 
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
```


# Suporte 
<p>  
  <a href="https://go.ok.org.br/discord" target="_blank">
    <img alt="Discord Invite" src="https://img.shields.io/badge/Discord-Entre%20no%20servidor-blue?style=for-the-badge&logo=discord" >
  </a>
</p>

Ingresse em nosso [canal de comunidade](https://go.ok.org.br/discord) para trocas sobre os projetos, dúvidas, pedidos de ajuda com contribuição e conversar sobre inovação cívica em geral.

# Agradecimentos
Este projeto é mantido pela Open Knowledge Brasil e possível graças às comunidades técnicas, às [Embaixadoras de Inovação Cívica](https://embaixadoras.ok.org.br/), às pessoas voluntárias e doadoras financeiras, além de universidades parceiras, empresas apoiadoras e financiadoras.

Conheça [quem apoia o Querido Diário](https://queridodiario.ok.org.br/apoie#quem-apoia).

# Open Knowledge Brasil
<p>
  <a href="https://bsky.app/profile/ok.org.br" target="_blank">
    <img alt="Bluesky Follow" src="https://img.shields.io/badge/Bluesky-_-0285FF?style=for-the-badge&logo=bluesky">
  </a>
  <a href="https://www.instagram.com/openknowledgebrasil/" target="_blank">
    <img alt="Instagram Follow" src="https://img.shields.io/badge/Instagram-_-red?style=for-the-badge&logo=instagram">
  </a>
  <a href="https://www.linkedin.com/company/open-knowledge-brasil" target="_blank">
    <img alt="LinkedIn Follow" src="https://img.shields.io/badge/LinkedIn-_-9cf?style=for-the-badge&logo=linkedin">
  </a> 
  <a href="https://mastodon.social/@okbr" target="_blank">
    <img alt="Mastodon Follow" src="https://img.shields.io/badge/mastodon-_-6364FF?style=for-the-badge&logo=mastodon">
  </a>
</p>

A [Open Knowledge Brasil](https://ok.org.br/) é uma organização da sociedade civil sem fins lucrativos, cuja missão é utilizar e desenvolver ferramentas cívicas, projetos, análises de políticas públicas, jornalismo de dados para promover o conhecimento livre nos diversos campos da sociedade. 

Todo o trabalho produzido pela OKBR está disponível livremente.

# Licença

Código licenciado sob a [Licença MIT](https://github.com/okfn-brasil/querido-diario-api-wrapper/blob/main/LICENSE.md).
