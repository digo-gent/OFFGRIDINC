from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from blog.models import Post

class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = 'weekly'

    def items(self):
        return ['home', 'services', 'contact_us','testimonials'] 

    def location(self, item):
        return reverse(item)

class BlogSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.6

    def items(self):
        return Post.objects.filter(status='published')

    def lastmod(self, obj):
        return obj.updated_at
