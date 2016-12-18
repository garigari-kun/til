from django.contrib import admin

from .models import Post

class PostModelAdmin(admin.ModelAdmin):
    class Meta:
        model = Post

    list_display = ['title', 'updated', 'timestamp']
    list_filter = ['updated', 'timestamp']
    search_fields = ['title', 'content']

admin.site.register(Post, PostModelAdmin)
