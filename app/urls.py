from django.urls import path
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from . forms import LoginForm, MyPasswordResetForm, MyPasswordChangeForm, MySetPasswordForm

urlpatterns = [
    path("", views.home, name='home'),
    path("about/", views.about, name="About"),
    path("contact/", views.contact, name="Contact"),
    path("category/<slug:val>", views.CategoryView.as_view(), name="category"),
    path("category-title/<val>", views.CategoryTitle.as_view(), name="category-title"),
    path("brand/<val>", views.Brand.as_view(), name="brand"),
    path("product-detail/<int:pk>", views.ProductDetail.as_view(), name="product-detail"),
    path("pluswishlist/", views.plus_wishlist),
    path("minuswishlist/", views.minus_wishlist),
    path("search/", views.search, name="search"),
    path("advancedsearch/", views.AdvancedSearch, name="advancedsearch"),
    path("wishlist/", views.show_wishlist, name="showwishlist"),
    path("profile/", views.ProfileView.as_view(), name='profile'),
    path("address/", views.address, name='address'),
    path("updateaddress/<int:pk>", views.UpdateAddress.as_view(), name='UpdateAddress'),
    path('registration/', views.CustomerRegistrationView.as_view(), name="customer-registration"),
    path('login/', auth_view.LoginView.as_view(template_name = 'app/login.html', authentication_form = LoginForm), name="login"),
    path('passwordchange/', auth_view.PasswordChangeView.as_view(template_name='app/changepassword.html', form_class=MyPasswordChangeForm, success_url='/passwordchangedone'), name='passwordchange'),
    path('passwordchangedone/', auth_view.PasswordChangeDoneView.as_view(template_name='app/passwordchangedone.html'), name='passwordchangedone'),
    path('userlogout/', auth_view.LogoutView.as_view(next_page='login'), name='userlogout'),
    path('password-reset/',auth_view.PasswordResetView.as_view(template_name='app/passwordreset.html'), name='password_reset'),
    path('password-reset-done/',auth_view.PasswordResetDoneView.as_view(template_name='app/passwordresetdone.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_view.PasswordResetConfirmView.as_view(template_name='app/passwordresetconfirm.html', form_class=MySetPasswordForm), name='password_reset_confirm'),
    path('password-reset-complete/',auth_view.PasswordResetCompleteView.as_view(template_name='app/passwordresetcomplete.html'), name='password_reset_complete'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Manguli Car"
admin.site.site_title = "Manguli Super Car"
admin.site.site_index_title = "Welcome to Manguli Car"