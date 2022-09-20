from django.urls import path

from apps.core.views import index, index_yandex


app_name = 'core'

urlpatterns = [
    path('', index, name='index'),
    path('ya/', index_yandex, name='index_yandex'),
]
