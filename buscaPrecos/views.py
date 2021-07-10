from django.shortcuts import render
import urllib.request
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

from selenium import webdriver
import time
import pandas as pd

# Create your views here.
from .models import Produto

def index(request):
    search = ''
    # create empty array to store data
    data = []
    try:
        search = request.GET['s']
    except:
        #do varios nada
        print('não há consulta')
    if(search != ''):
        driver = webdriver.Chrome()
        search = request.GET['s']
        print(f"https://www.casasbahia.com.br/{search}/b")
        driver.get(f"https://www.casasbahia.com.br/{search}/b")

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        time.sleep(5)  
        results = driver.find_elements_by_xpath("//*[@id='__next']/div[2]/div/div/div[4]/div[2]/div/article/ul")
        # loop over results
        for result in results:
            products = result.find_elements_by_tag_name("a")
            for product in products:
                try:
                    productInfo = {
                        'link': product.get_attribute('href'),
                        'imagem': product.find_element_by_tag_name('img').get_attribute('src'),
                        'nome': product.find_element_by_tag_name('p').text,
                        'preco': product.find_element_by_css_selector("div[class^='ProductPrice']").text
                    }
                except:
                    print('não foi possível adicionar o produto na lista')

                data.append(productInfo)
        
        driver.quit()

    context = {
        'products': data
    }
    
    return render(request, 'precos\index.html', context=context)