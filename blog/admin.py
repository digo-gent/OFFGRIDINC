from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):	
    list_display = ('title', 'status',"published_at","updated_at","is_featured","created_at",)
    exclude = ("author",)
    readonly_fields=('slug',"updated_at","created_at",)	
    list_filter = ('status',"is_featured",)
    search_fields = ('title', 'content',"status",)
    
    def save_model(self, request, obj, form, change):
        if not obj.author_id:
            obj.author = request.user  # Automatically assign the logged-in user as author
        super().save_model(request, obj, form, change)
    
admin.site.register(Post, PostAdmin),
