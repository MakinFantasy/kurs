from django.contrib import admin
from .models import Category, Post, Comment, Tag
# Register your models here.


class CategoryPostInline(admin.TabularInline):
    model = Post
    extra = 1


class AdminCategory(admin.ModelAdmin):
    inlines = [CategoryPostInline]
    list_display = ('title', 'date_created')
    list_filter = ['date_created']
    search_fields = ['title']
    date_hierarchy = 'date_created'


admin.site.register(Category, AdminCategory)


class AdminPost(admin.ModelAdmin):
    list_display = ('title', 'category',  'date_created')
    list_display_links = ['title', 'category', 'date_created']
    list_filter = ['category', 'date_created', 'tags']
    search_fields = ['title']
    date_hierarchy = 'date_created'
    filter_horizontal = ['tags']



class AdminComment(admin.ModelAdmin):
    list_display = ('title', 'post', 'email', 'content', 'status')
    list_filter = ['status', 'post']
    search_fields = ['post__title', 'title']
    raw_id_fields = ['post']


class AdminTag(admin.ModelAdmin):
    list_display = ('title', 'date_created')
    list_filter = ['date_created']
    search_fields = ['title']
    raw_id_fields = ['post']


admin.site.register(Post, AdminPost)
admin.site.register(Comment, AdminComment)
admin.site.register(Tag, AdminTag)

