from django.contrib import admin
from .models import data
from .models import user
from .models import detail

# Register your models here.

admin.site.register(data)
admin.site.register(user)
admin.site.register(detail)


