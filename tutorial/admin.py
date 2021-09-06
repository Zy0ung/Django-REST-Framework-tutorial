from django.contrib import admin
from tutorial.models import blog
# Register your models here.

class blogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created',)

admin.site.register(blog, blogAdmin)