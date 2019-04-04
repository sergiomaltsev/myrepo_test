from django.contrib import admin
from .models import Video, Comment


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 2

class VideoAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    readonly_fields = ['like']
    inlines = [CommentInline]

    class Media():
        js=['js/justscript.js']


admin.site.register(Video, VideoAdmin)