from django.contrib import admin
from watch.models import Watch, Comment


class CommentModelAdmin(admin.ModelAdmin):
    list_display = ['watch', 'content']
    list_display_links = ['watch']
    list_filter = ['watch', 'content']
    search_fields = ['content']
 
    class Meta:
        model = Comment

admin.site.register(Watch)
admin.site.register(Comment, CommentModelAdmin)
# Register your models here.
