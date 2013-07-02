from django.contrib import admin

from node.models import AdminImageWidget
        
class LocalizedNodeAdmin(admin.StackedInline):
    fk_name = 'meta'
    extra = 3
    max_num = 3
    
class NodeAdmin(admin.ModelAdmin):
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'picture':
            request = kwargs.pop("request", None)
            kwargs['widget'] = AdminImageWidget
            return db_field.formfield(**kwargs)
        return super(NodeAdmin,self).formfield_for_dbfield(db_field, **kwargs)
