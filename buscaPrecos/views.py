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
    driver = webdriver.Chrome()  # Optional argument, if not specified will search path.

    driver.get('https://www.casasbahia.com.br/geladeira/b')

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    time.sleep(5)  
    results = driver.find_elements_by_xpath("//*[@id='__next']/div[2]/div/div/div[4]/div[2]/div/article/ul")
    # create empty array to store data
    data = []
    # loop over results
    for result in results:
        products = result.find_elements_by_tag_name("a")
        for product in products:
            print(product.find_element_by_css_selector("div[class^='ProductPrice']").text)
            productInfo = {
                'link': product.get_attribute('href'),
                'imagem': product.find_element_by_tag_name('img').get_attribute('src'),
                'nome': product.find_element_by_tag_name('p').text,
                'preco': product.find_element_by_css_selector("div[class^='ProductPrice']").text
            }

            data.append(productInfo)

    context = {
        'products': data
    }

    driver.quit()
    
    return render(request, 'precos\index.html', context=context)