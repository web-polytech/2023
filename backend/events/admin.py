from django.contrib import admin
from events.models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
  list_display = ['title','tagline']
  list_filter = ['tagline']
  fieldsets = [
        (
            "Обычные поля",
            {
                "fields": ["title", "tagline"],
            },
        ),
        (
            "Поля с файлом",
            {
                "fields": ["cover"],
            },
        ),
    ]
