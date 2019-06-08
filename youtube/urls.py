from django.urls import path
from django.conf.urls import url
from . import views
from . import example
from . import example2
urlpatterns = [
    #path('', views.index2),
    path('', views.main ,name = 'youtube'),

    #path('', example2.main),

    #path('example', example.main),

]
