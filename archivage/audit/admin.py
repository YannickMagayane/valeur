from django.contrib import admin
from .models import LogEntry

class LogEntryAdmin(admin.ModelAdmin):
    list_display = ('action_time', 'object_repr', 'action_flag', 'change_message')
    search_fields = ('object_repr', 'action_flag')
    list_filter = ('action_flag', 'action_time')

    # Rendre tous les champs en lecture seule
    readonly_fields = ('action_time', 'object_repr', 'action_flag', 'change_message')

    # Désactiver l'ajout et la suppression
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    # Désactiver l'édition
    def has_change_permission(self, request, obj=None):
        return False

admin.site.register(LogEntry, LogEntryAdmin)
