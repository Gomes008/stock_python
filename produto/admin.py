from django.contrib import admin

# Register your models here.
from produto.models import Produto


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'quantidade', 'valor', 'responsavel')

admin.site.register(Produto, ProdutoAdmin)
