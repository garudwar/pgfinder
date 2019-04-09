from django.contrib import admin
from  .models  import ItemModel,RegisterModel
# Register your models here.

admin.site.register(ItemModel)
admin.site.register(RegisterModel)