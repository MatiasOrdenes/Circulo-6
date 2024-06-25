from django.contrib import admin
from .models import Expense, Category
# Register your models here.


class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('amount', 'description', 'owner', 'category', 'date', 'ncompra', 'dfactura', 'ddespacho', 'contacto',)
    search_fields = ('description', 'category', 'date', 'ncompra')

    list_per_page = 5


admin.site.register(Expense, ExpenseAdmin)
admin.site.register(Category)
