from django.urls import path
from . import views

urlpatterns = [
    path('result-form', views.resultForm, name='result_form'),
    path('save', views.save, name='save'),
    path('check-result', views.viewResult, name='check_result'),
    path('result-view', views.searchResult, name='result_view')
]
