from buscaPrecos.services.crawler import CrawlerService
from django.shortcuts import render


# Create your views here.
from .models import Produto

def index(request):
    search = ''
    # create empty array to store data
    data = []
    try:
        # trying to get the parameter first
        #if it fail, nothing will happen
        search = request.GET['s']

        crawler = CrawlerService()
        crawler.getProductsFromCasasBahia(search)
        data = crawler.getResults()
    except Exception as inst:
        #do varios nada
        print(inst)

    context = {
        'products': data
    }
    
    return render(request, 'precos\index.html', context=context)