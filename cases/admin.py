from django.contrib import admin
from cases.models import *
# Register your models here.

admin.site.register(Case)
admin.site.register(Lawyer)
admin.site.register(Client)

# change in the dashboard
