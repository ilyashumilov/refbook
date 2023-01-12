from django.contrib import admin
from .models import Refbook, RefbookVersion, RefbookElement
# Register your models here.

admin.site.register(Refbook)
admin.site.register(RefbookVersion)
admin.site.register(RefbookElement)