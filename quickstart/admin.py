from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Manufacturer)
admin.site.register(Shoe)
admin.site.register(ShoeType)
admin.site.register(ShoeColor)

