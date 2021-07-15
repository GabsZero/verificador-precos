import urllib.request
import json
import time
from bs4 import BeautifulSoup as bs
import re


class CrawlerService:
    # this will hold information found in pages
    products = []

    def clearResults(self):
        self.products.clear()

    def getResults(self):
        return self.products

    def casasBahiaRequest(self, search):
        urlRequest = f"https://prd-api-partner.viavarejo.com.br/api/search?resultsPerPage=20&terms={search}&salesChannel=desktop&apiKey=casasbahia"
        request = urllib.request.Request(urlRequest)
        request.add_header('authority', 'prd-api-partner.viavarejo.com.br')
        request.add_header('method', 'GET')
        request.add_header('path', '/api/search?resultsPerPage=20&terms=geladeira&salesChannel=desktop&apiKey=casasbahia')
        request.add_header('scheme', 'https')
        request.add_header('accept', 'application/json, text/plain, */*')
        request.add_header('accept-language', 'en-US,en;q=0.9,pt-BR;q=0.8,pt;q=0.7')
        request.add_header('origin', 'https://www.casasbahia.com.br')
        request.add_header('sec-ch-ua', '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"')
        request.add_header('sec-ch-ua-mobile', '?0')
        request.add_header('sec-fetch-dest', 'empty')
        request.add_header('sec-fetch-mode', 'cors')
        request.add_header('sec-fetch-site', 'cross-site')
        request.add_header('user-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')

        response = urllib.request.urlopen(request)

        response = response.read()

        return json.loads(response)

    def getProductsFromAmericanas(self, search):
        urlRequest = f"https://www.americanas.com.br/busca/geladeira"
        request = urllib.request.Request(urlRequest)
        request.add_header('authority', 'prd-api-partner.viavarejo.com.br')
        request.add_header('method', 'GET')
        request.add_header('path', '/api/search?resultsPerPage=20&terms=geladeira&salesChannel=desktop&apiKey=casasbahia')
        request.add_header('scheme', 'https')
        request.add_header('accept', 'application/json, text/plain, */*')
        request.add_header('accept-language', 'en-US,en;q=0.9,pt-BR;q=0.8,pt;q=0.7')
        request.add_header('origin', 'https://www.casasbahia.com.br')
        request.add_header('sec-ch-ua', '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"')
        request.add_header('sec-ch-ua-mobile', '?0')
        request.add_header('sec-fetch-dest', 'empty')
        request.add_header('sec-fetch-mode', 'cors')
        request.add_header('sec-fetch-site', 'cross-site')
        request.add_header('user-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')
        response = urllib.request.urlopen(request)

        response = response.read()
        soup = bs(response, 'html.parser')

        for div in soup.find_all(class_=re.compile("src__ColGridItem")):
            productInfo = {'empresa': 'Americanas'}
            for span in div.find('span', class_=re.compile("src__Name")):
                productInfo['nome'] = span
            for price in div.find('span', class_=re.compile("src__PromotionalPrice")):
                productInfo['preco'] = price.replace('R$', '').rstrip()
            
            url = f"https://www.americanas.com.br{div.find('a')['href']}"
            productInfo['link'] = url
            self.products.append(productInfo)


    def getProductsFromCasasBahia(self, search):
        response = self.casasBahiaRequest(search)

        try:
            products = response['products']
            for product in products:
                productInfo = {
                        'link': product['url'],
                        'imagem': product['images']['default'],
                        'nome': product['name'],
                        'preco': product['price'],
                        'empresa': 'Casas Bahia'
                    }
                self.products.append(productInfo)

        except Exception as inst:
            print(inst)
        