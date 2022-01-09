from django.contrib import admin

# Register your models here.
from login_app.models import Test, Hey

admin.site.register(Test)
admin.site.register(Hey)