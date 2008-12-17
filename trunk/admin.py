from django.contrib import admin

from models import *

class TemplateAdmin(admin.ModelAdmin):
    pass
    
class TemplateFieldAdmin(admin.ModelAdmin):
    pass
    
class FieldParameterAdmin(admin.ModelAdmin):
    pass
    
class RecordAdmin(admin.ModelAdmin):
    pass
    
admin.site.register(Template, TemplateAdmin)
admin.site.register(TemplateField, TemplateFieldAdmin)
admin.site.register(FieldParameter, FieldParameterAdmin)
admin.site.register(Record, RecordAdmin)
