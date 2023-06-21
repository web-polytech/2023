from django.contrib import admin

from logvisit.models import LogVisit

@admin.register(LogVisit)
class LogVisitAdmin(admin.ModelAdmin):
    list_display = ('user', 'url', 'browser')
