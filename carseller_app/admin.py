from django.contrib import admin
from .models import Sellrequest,Carmodel,Carvender,User
# Register your models here.
admin.site.register(Sellrequest)

admin.site.register(Carvender)
admin.site.register(Carmodel)
admin.site.register(User)