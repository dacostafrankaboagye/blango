from django.contrib import admin

from blog.models import Tag, Post, Comment


class PostAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug": ("title",) }
  # list_display = ["slug", "published_at"] # show the slug and published_at in the Post list


admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
