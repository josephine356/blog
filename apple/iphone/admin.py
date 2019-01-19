from django.contrib import admin
from iphone.models import Iphone, Comment


class CommentModelAdmin(admin.ModelAdmin):
    list_display = ['iphone', 'content']
    list_display_links = ['iphone']
    list_filter = ['iphone', 'content']
    search_fields = ['content']
 
    class Meta:
        model = Comment

admin.site.register(Iphone)
admin.site.register(Comment, CommentModelAdmin)
# Register your models here.
