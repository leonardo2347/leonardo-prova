from django.contrib import admin

from . models import *

admin.site.register(Produto)
admin.site.register(Cliente)
admin.site.register(Carrinho_De_Compras)