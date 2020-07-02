from django.contrib import admin
from django.utils.translation import ugettext_lazy as _ 
from .models import Research, ResearchCategory, Law, LawCategory
# Register your models here.

class ResearchAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'created_on')
    search_fields = ['title', 'content']
    readonly_fields = ('updated_on', 'created_on')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Research, ResearchAdmin)

class ResearchCategoryAdmin(admin.ModelAdmin):
    pass 

admin.site.register(ResearchCategory, ResearchCategoryAdmin)

class LawCategoryAdmin(admin.ModelAdmin):
    pass
admin.site.register(LawCategory, LawCategoryAdmin)

class LawAdmin(admin.ModelAdmin):
    search_fields = ('title', )
    list_filter = ('category', )
    list_display = ('title', 'category')
    
    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.updated_by = request.user
        super(LawAdmin, self).save_model(request, obj, form, change)
        
admin.site.register(Law, LawAdmin)