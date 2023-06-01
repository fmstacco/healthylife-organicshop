from django.contrib import admin
from .models import Post, Comment, Category

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_on', 'category')
    list_filter = ('author', 'created_on')
    search_fields = ('title', 'content')

    fieldsets = (
        (None, {
            'fields': ('title', 'author', 'content', 'category')
        }),
    )

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'created_on')
    list_filter = ('author', 'created_on')
    search_fields = ('post__title', 'author__username')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

