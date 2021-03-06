from django.contrib import admin
from rango.models import Category, Page
from rango.models import UserProfile

# Register your models here.
class PageInline(admin.TabularInline):
    model = Page
    extra = 0 # No extra blank line to be filled in

class CategoryAdmin(admin.ModelAdmin):
    inlines = [PageInline]
    list_display = ('name', 'views', 'likes')
    prepopulated_fields = {'slug':('name',)}

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)
