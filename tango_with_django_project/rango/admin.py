from django.contrib import admin
from rango.models import Category, Page
from rango.models import UserProfile
admin.site.register(UserProfile)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

# Update the registeration to include this customised interface
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page)