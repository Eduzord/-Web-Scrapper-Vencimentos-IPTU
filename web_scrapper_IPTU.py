

import requests
import urllib
from requests_html import HTMLSession
import pprint




def get_source(url):
    """Retorna o código fonte da URL fornecida. 

    Argumentos: 
        url (string): URL da página a ser scrapada.

    Returna:
        response (object): HTTP resposta do objeto requests_html. 
    """

    try:
        session = HTMLSession()
        response = session.get(url)
        return response

    except requests.exceptions.RequestException as e:
        print(e)

def get_results(query):
    
    query = urllib.parse.quote_plus(str(query))
    response = get_source("https://www.google.com.br/search?q=" + query)
    
    return response

def get_text(css_identifier, result, valor_default =''):
    #valida a existencia do identificador css
    identificador = result.find(css_identifier, first=True)
    if identificador is None: #se o identificador não existir, retornar o valor default
        return valor_default
    return identificador.text

def parse_results(response, cidade):
    
    css_identifier_result = ".tF2Cxc"
    css_identifier_title = "h3"
    css_identifier_link = ".yuRUbf a"
    css_identifier_text = ".VwiC3b"
    
    results = response.html.find(css_identifier_result)
    
    output = []

    for result in results:
      #Filtro para evitar domínios clickbait
      if result.find(css_identifier_link, first=True).attrs['href'].startswith('https://iptu') or result.find(css_identifier_link, first=True).attrs['href'].startswith('https://2viaiptu'):
        continue
      
      

      else:  
        #Filtro pra remover do resultado os sites que não contenham o nome do município pesquisado
        if cidade.lower() in result.find(css_identifier_title, first=True).text.lower():  
          item = {
              'title': get_text(css_identifier_title,result),
              #'title': result.find(css_identifier_title, first=True).text,
              'link': result.find(css_identifier_link, first=True).attrs['href'],
              'text': get_text(css_identifier_text,result)
              #'text': result.find(css_identifier_text, first=True).text
          }
          #mantive a versão anterior sem a utilização da função get_text pois as vezes funciona sem ela(?)
          output.append(item)
    if not output:
      output.append('Não há resultados relevantes para {}'.format(cidade))
     
    return output

def google_search(query,cidade):
    response = get_results(query)
    return parse_results(response, cidade)

municipio = ['Alegrete',
'Angra dos Reis',
'Aracaju',
'Araçatuba',
'Araguaína',
'Arapongas',
'Araraquara',
'Arraial do Cabo',
'Bagé',
'Balneário Camboriú',
'Barretos',
'Belém',
'Bertioga',
'Betim',
'Birigüi',
'Blumenau',
'Boituva',
'Caicó',
'Campinas',
'Campo Bom',
'Campo Largo',
'Campos do Jordão',
'Campos dos Goytacazes',
'Canguaretama',
'Capão da Canoa',
'Caraguatatuba',
'Carapicuíba',
'Casimiro de Abreu',
'Catanduva',
'Caxias',
'Chapecó',
'Cianorte',
'Criciúma',
'Cruz Alta',
'Curitiba',
'Divinópolis',
'Dourados',
'Duque de Caxias',
'Fortaleza',
'Goiânia',
'Gramado',
'Guararapes',
'Guaratinguetá',
'Itaboraí',
'Itajaí',
'Itaquaquecetuba',
'Itatiba',
'Ituverava',
'Jaboatão dos Guararapes',
'Jales',
'João Pessoa',
'Jundiaí',
'Londrina',
'Maricá',
'Marília',
'Mococa',
'Mossoró',
'Natal',
'Navegantes',
'Niterói',
'Nova Iguaçu',
'Olinda',
'Pedreira',
'Petrópolis',
'Porto Alegre',
'Porto Ferreira',
'Presidente Dutra',
'Presidente Prudente',
'Recife',
'Resende',
'Ribeira do Pombal',
'Rio Claro',
'Rio de Janeiro',
'Salvador',
'Santa Maria',
'Santos',
'São Carlos',
'São Gabriel',
'São José dos Campos',
'São Paulo',
'São Pedro',
'Sumaré',
'Tabatinga',
'Taquara',
'Tubarão',
'Ubatuba',
'Uberlândia',
'Uruguaiana',
'Várzea Grande',
'Vera Cruz',
'Votuporanga'
]
for cidade in municipio:

  pesquisa = "IPTU {} 2023 Cota Única".format(cidade)
  results = google_search(pesquisa, cidade)

  pprint.pp(results)

#results



