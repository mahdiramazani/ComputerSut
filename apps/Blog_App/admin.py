from django.contrib import admin

from .models import Tag,BlogModel,Comment


admin.site.register(Tag)

admin.site.register(BlogModel)
admin.site.register(Comment)