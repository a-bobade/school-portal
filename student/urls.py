from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('records', views.record, name='records'),
    path('create', views.create, name='create'),
    path('store', views.store, name='store'),
    path('view/<matric>', views.view, name='view'),
    path('delete/<matric>', views.delete, name='delete'),
    path('update/<matric>', views.updateStudent, name='update'),
    path('edit/<matric>', views.update, name='edit'),
    path('search', views.search, name='search')
]
