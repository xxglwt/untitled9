from django.contrib import admin
from TestModel.models import *
# Register your models here.
admin.site.register([Test,Tag])

class TagInline(admin.TabularInline):
    model = Tag

class ContactAdmin(admin.ModelAdmin):
    # fields = ('name','email')
    list_display = ('name','age','email')
    search_fields = ('name',)
    inlines = [TagInline]
    fieldsets = (
        ['人员主要信息', {
            'fields': ('name', 'email'),
        }],
        ['选项', {
            'classes': ('collapse',),  # CSS
            'fields': ('age',),
        }]
    )

admin.site.register(Contact,ContactAdmin)
