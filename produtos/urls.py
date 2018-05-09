from django.urls import path
from .views import lista_produtos, new_produto, update_produto, delete_produto

urlpatterns = [
    path('lista/', lista_produtos, name="lista_produtos"),
    path('new/', new_produto, name="new_produto"),
    path('update/<int:id>', update_produto, name="update_produto"),
    path('delete/<int:id>', delete_produto, name="delete_produto"),

]