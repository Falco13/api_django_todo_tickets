from django.contrib import admin
from django.utils.html import format_html
from todo_api.models import Todo, Image, Status, Comment


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text', 'status', 'author', 'created_at', 'updated_at')
    fields = ('title', 'text',
              ('status', 'author',),
              ('assigned_to', 'image'),
              'created_at', 'updated_at',
              )
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Image)
class PhotoAdmin(admin.ModelAdmin):
    def img_tag(self, obj):
        return format_html('<img src="{}" style="max-width:50px; max-height:50px"/>'.format(obj.img.url))

    list_display = ('id', 'img_tag', 'img_title', 'creator', 'created_at')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'author', 'todo', 'parent', 'created_at')
    readonly_fields = ('created_at',)


admin.site.register(Status)
