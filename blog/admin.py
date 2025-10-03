from django.contrib import admin

from blog.models import Tag, Post

admin.site.register(Tag, PostAdmin)

class PostAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug": ("title",)}
