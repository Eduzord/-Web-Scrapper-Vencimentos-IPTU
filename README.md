

# 📆 Web Scrapper Vencimentos de IPTU 📆
### _Uma automação para agilizar a consulta de vencimentos_


![python version](https://img.shields.io/badge/python%20ver-3.10-brightgreen)

Este script foi desenvolvido para auxiliar na operação de pessoas jurídicas ou físicas que tenham a necessidade de montar um calendário de vencimentos de IPTU de municípios diversos pelo Brasil, realizando consultas no google  e exibindo os resultados mais relevantes.

A ideia surgiu por meio da necessidade que eu tinha enquanto assistente admnistrativo numa empresa de grande porte nacional que possuia diversos imóveis locados pelo Brasil inteiro e precisava levantar os vencimentos do Imposto Predial e Territorial Urbano dos municípios onde a Cia. possui unidades para que pudesse realizar um orçamento para solicitar o valor a ser liberado pela tesouraria para o pagamento do tributo.


## Funcionalidades

- Consulta automaticamente diversos municípios disponibilizados em uma **lista.**
- Filtra resultados que não contenham o nome do município pesquisado no **título do link**.
- Filtra resultados de páginas "clickbait" que não trazem informações relevantes, como  o "https;//2viaiptu,com"

O projeto atualmente apenas imprime os resulados no console , pois foi escrito primeiramente no Google Colab e desta forma já me antendia muito bem, não havia necessidade de guardar em um arquivo externo.

## 🤖Utilizando o script

Simplesmente abra-o em qualquer interpretador de python, altere a lista de municipios a ser consultado na linha **_77_** e de especificar o exercício de consulta na variável _pesquisa_ na linha **171**.

Lembre-se de verificar a compatibilidade da versão do python instalada e de certificar-se de que os módulos [Requests](https://pypi.org/project/requests/) e [Requests-HTML](https://requests.readthedocs.io/projects/requests-html/en/latest/) estão instalados

## Tecnologias utilizadas

- ``Python 3.10``
- Módulo [Requests](https://pypi.org/project/requests/) 
- Módulo  [Requests-HTML](https://requests.readthedocs.io/projects/requests-html/en/latest/) 
- [Google Colab](https://colab.research.google.com/)


## 👨‍💻Desenvolvimento, Créditos, Agradecimentos

Desenvolvido [mim mesmo](https://github.com/Eduzord) utilizando como base o código no [artigo](https://practicaldatascience.co.uk/data-science/how-to-scrape-google-search-results-using-python) do [Matt Clarcke](https://www.linkedin.com/in/mattclarke/).

Não posso deixar de agradecer também diversos membros da comunidade do [Stack Overflow](https://stackoverflow.com) pelo inestimável auxílio involuntário que me prestaram ao contribuir nos fóruns.
