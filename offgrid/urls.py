"""
URL configuration for offgrid project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from agency.views import *
from account.views import *
from blog.views import *
from django.contrib.sitemaps.views import sitemap
from agency.sitemaps import StaticViewSitemap, BlogSitemap

#sitemaps configuration
sitemaps = {
    "static": StaticViewSitemap,
    'blog': BlogSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    
    # Sitemaps
    path("sitemap.xml/",sitemap,{"sitemaps": sitemaps},name="django.contrib.sitemaps.views.sitemap"),
    path('robots.txt/',TemplateView.as_view(template_name='robots.txt',content_type='text/plain')),
    
    #login/logout/password resets
    path("access/", include("django.contrib.auth.urls")),
    
    #Home
    path('', HomeView.as_view(), name='home'),
    
    #Services
    path('service/', ServiceListView.as_view(), name='services'),
    path('service/create/', ServiceCreateView.as_view(), name='service_create'),
    path('service/<int:pk>/update/', ServiceUpdateView.as_view(), name='service_update'),
    path('service/<int:pk>/', ServiceDetailView.as_view(), name='service_detail'),
    path('service/<int:pk>/delete', ServiceDeleteView.as_view(), name='service_delete'),
    
    #Testimonials
    path('testimonial/', TestimonialListView.as_view(), name='testimonials'),
    path('testimonial/create/', TestimonialCreateView.as_view(), name='testimonial_create'),
    path('testimonial/<int:pk>/update/', TestimonialUpdateView.as_view(), name='testimonial_update'),
    path('testimonial/<int:pk>/', TestimonialDetailView.as_view(), name='testimonial_detail'),
    path('testimonial/<int:pk>/delete', TestimonialDeleteView.as_view(), name='testimonial_delete'),
    
    #Package Logos
    path('package/create/', PackageCreateView.as_view(), name='package_create'),
    path('package/<int:pk>/update/', PackageUpdateView.as_view(), name='package_update'),
    path('package/<int:pk>/delete', PackageDeleteView.as_view(), name='package_delete'),
    
    #Client Logos
    path('logo/', LogoListView.as_view(), name='logos'),
    path('logo/create/', LogoCreateView.as_view(), name='logo_create'),
    path('logo/<int:pk>/update/', LogoUpdateView.as_view(), name='logo_update'),
    path('logo/<int:pk>/', LogoDetailView.as_view(), name='logo_detail'),
    path('logo/<int:pk>/delete', LogoDeleteView.as_view(), name='logo_delete'),
    
    #Account Creation
    path('account/', AccountListView.as_view(), name='accounts'),
    path('account/create/', AccountCreateView.as_view(), name='account_create'),
    path('account/me/', AccountDetailView.as_view(), name='account_detail'),
    path('account/me/update/', AccountUpdateView.as_view(), name='account_update'),
    path('account/me/delete/', AccountDeleteView.as_view(), name='account_delete'),
    path("account/me/password/",auth_views.PasswordChangeView.as_view(template_name="registration/password_change_form.html"), name="account_password_change"),
    path("account/me/password/done/",auth_views.PasswordChangeDoneView.as_view(template_name="registration/password_change_done.html"),name="password_change_done"),
    #Blogs
    path('blog/', BlogListView.as_view(), name='blogs'),
    path('blog/create/', BlogCreateView.as_view(), name='blog_create'),
    path('blog/<int:pk>/update/', BlogUpdateView.as_view(), name='blog_update'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('blog/<int:pk>/delete', BlogDeleteView.as_view(), name='blog_delete'),
    
    #Contact us
    path('contact/',  ContactView.as_view(), name='contact_us'),
    
    #newsletter
    path('newsletter/subscribe/', newsletter_subscribe, name='newsletter-subscribe'),
]
urlpatterns += [
    path("ckeditor5/", include('django_ckeditor_5.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
