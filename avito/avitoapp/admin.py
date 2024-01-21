from django.contrib import admin

from avitoapp.models import Ad
from avitoapp.models import AdImage



class AdInline(admin.StackedInline):
    model = AdImage


# Register your models here.
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