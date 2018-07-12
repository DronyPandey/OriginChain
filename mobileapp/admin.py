from django.contrib import admin

# Register your models here.
from .models import MaterialTransaction, Material

admin.site.register(MaterialTransaction)
admin.site.register(Material)