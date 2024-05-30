from django.contrib import admin
from .models import ArchiveCategory, PhysicalDocument, Archive



admin.site.register(ArchiveCategory)
admin.site.register(PhysicalDocument)
admin.site.register(Archive)
