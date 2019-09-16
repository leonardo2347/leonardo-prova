from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('produto/', views.produto_list),
    path('produto/<int:produto_id>/', views.produto_show),
    path('produto/create/', views.produto_form),
    path('produto/<int:produto_id>/editar/' ,views.produto_editar),
    path('produto/<int:produto_id>/delete/' ,views.produto_delete)
    
]