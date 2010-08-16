from django.contrib import admin

from models import *

class TemplateFieldInline(admin.TabularInline):
    model = TemplateField

class TemplateAdmin(admin.ModelAdmin):
    inlines = [TemplateFieldInline]
    save_as = True
    
class FieldParameterInline(admin.TabularInline):
    model = FieldParameter

class TemplateFieldAdmin(admin.ModelAdmin):
    inlines = [FieldParameterInline]
    
class FieldParameterAdmin(admin.ModelAdmin):
    pass
    
class RecordAdmin(admin.ModelAdmin):
    pass
    
admin.site.register(Template, TemplateAdmin)
admin.site.register(TemplateField, TemplateFieldAdmin)
admin.site.register(FieldParameter, FieldParameterAdmin)
admin.site.register(Record, RecordAdmin)
