from django.urls import path
from . import views
app_name = 'buscarPrecos'

urlpatterns = [
    path('', views.index, name="precos.index")
]