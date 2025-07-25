from account.views import *
from django.contrib.auth import views as auth_views
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #login/logout/password resets
    path("access/", include("django.contrib.auth.urls")),
    
    #Account Creation
    path('account/', AccountListView.as_view(), name='accounts'),
    path('account/create/', AccountCreateView.as_view(), name='account_create'),
    path('account/me/', AccountDetailView.as_view(), name='account_detail'),
    path('account/me/update/', AccountUpdateView.as_view(), name='account_update'),
    path('account/me/delete/', AccountDeleteView.as_view(), name='account_delete'),
    path("account/me/password/",auth_views.PasswordChangeView.as_view(template_name="registration/password_change_form.html"), name="account_password_change"),
    path("account/me/password/done/",auth_views.PasswordChangeDoneView.as_view(template_name="registration/password_change_done.html"),name="password_change_done"),
    ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)