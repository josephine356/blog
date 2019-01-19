from django.contrib import admin
from ipad.models import Ipad, Comment


class CommentModelAdmin(admin.ModelAdmin):
    list_display = ['ipad', 'content']
    list_display_links = ['ipad']
    list_filter = ['ipad', 'content']
    search_fields = ['content']
 
    class Meta:
        model = Comment

admin.site.register(Ipad)
admin.site.register(Comment, CommentModelAdmin)
# Register your models here.
