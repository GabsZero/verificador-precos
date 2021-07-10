from buscaPrecos.services.product import CrawlerService
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
        crawler.searchInCasasBahia(search)
        data = crawler.getResult()
    except:
        #do varios nada
        print('não há consulta')

    context = {
        'products': data
    }
    
    return render(request, 'precos\index.html', context=context)