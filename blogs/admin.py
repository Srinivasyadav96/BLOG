from django.contrib import admin
from blogs.models import Category, Blog, Comment

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'author', 'category', 'status', 'is_featured', 'created_at')
    search_fields = ('id', 'title', 'category__category_name', 'status')
    list_editable = ('status', 'is_featured')

# Register your models here.
admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment)