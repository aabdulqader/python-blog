from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from accounts import views as account_views
admin.site.site_header = 'Python Blog'
admin.site.site_title = 'Welcome to the Python Blog'
admin.site.index_title = 'Welcome to this Portal'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('articles.urls')),
    path('signup/', account_views.signup_view, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name= 'logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'), name= 'password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name= 'password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name= 'password_reset_confirm'),
    path('password-reset-complete', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_complete.html'), name= 'password_reset_complete'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
