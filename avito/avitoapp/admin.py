from avitoapp.models import AdImage
from avitoapp.models import Ad

from django.contrib import admin



class AdInline(admin.StackedInline):
    model = AdImage



@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    inlines = [
        AdInline,
    ]
    list_display = 'name', 'description', 'price', 'address', 'user', 'created_at'
    fieldsets = [
        ('Images', {
            'fields': ('preview',),
        }
         )
    ]