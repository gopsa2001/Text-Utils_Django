from django.urls import path,include
from textu import views

urlpatterns = [
    path ("",views.index,name='index'),
    path("analyze",views.analyze,name='analyze')

]