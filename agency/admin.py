from django.contrib import admin
from .models import Contact, Testimonial, ClientLogo, Service, Package, NewsLetter, ServiceInquiry, SEOSettings

admin.site.register(Contact),
admin.site.register(Testimonial),
admin.site.register(ClientLogo),
admin.site.register(Service),
admin.site.register(Package),
admin.site.register(NewsLetter),
admin.site.register(ServiceInquiry),

@admin.register(SEOSettings)
class SEOSettingsAdmin(admin.ModelAdmin):
    list_display = ('page', 'title', 'updated_at')
    search_fields = ('title', 'description', 'keywords')
    list_filter = ('page',)
    readonly_fields = ('updated_at',)
    fieldsets = (
        ("Page Info", {
            'fields': ('page',)
        }),
        ("Meta Tags", {
            'fields': ('title', 'description', 'keywords')
        }),
        ("Open Graph & Twitter", {
            'fields': ('og_image', 'twitter_card_type')
        }),
        ("Timestamps", {
            'fields': ('updated_at',)
        }),
    )


