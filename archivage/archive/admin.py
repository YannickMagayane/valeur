from django.contrib import admin
from .models import ArchiveCategory, PhysicalDocument, Archive,RepportInformation



admin.site.register(ArchiveCategory)
admin.site.register(PhysicalDocument)
admin.site.register(Archive)
admin.site.register(RepportInformation)