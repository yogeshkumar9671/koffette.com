import imp
from unicodedata import name
from xml.dom.minidom import Document
from django.conf import settings
from django.urls import path
from app import views
from django.conf.urls.static import static
from app.forms import ForgotPasswordForm, PasswordChangeForm, SetForgotPasswordForm
from django.contrib.auth import views as auth_views
import uuid

urlpatterns = [
    # authentication related urls
    path('registration/', views.customerregistration, name='customerregistration'),
    path('login/', views.login, name='login'),
    path('logout/', views.LogOut, name='logout'),
    path('changepassword/', auth_views.PasswordChangeView.as_view(template_name="app/changepassword.html", form_class=PasswordChangeForm, success_url="/changesdone/"), name="changepassword"),
    path('changesdone/', auth_views.PasswordChangeView.as_view(template_name="app/changesdone.html"), name="changesdone"),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='app/password_reset.html', form_class=ForgotPasswordForm),name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html', success_url="/login", form_class=SetForgotPasswordForm),name='password_reset_confirm'),
    # path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'), name='password_reset_complete'),





    path("",views.ProductView.as_view(), name="home"),
    path('<pk>/product-detail/', views.product_detail, name='product-detail'),
    path('buy/', views.buy_now, name='buy-now'),
    path('orders/', views.orders, name='orders'), 
    path('mobile/', views.mobile, name='mobile'),
    path('checkout/', views.checkout, name='checkout'),
    path('coffee/', views.coffee, name='coffee'),
    path('coffee/<slug:data>', views.coffee, name='coffeedata'),
    path('clothes/', views.clothes, name='clothes'),
    path('clothes/<slug:data>', views.clothes, name='clothesdata'),
    path('shoes/', views.shoes, name='shoes'),
    path('beauty_product/', views.beauty_product, name='beauty_product'),
    path('grocery/', views.grocery, name='grocery'),
    path('accessories/', views.accessories, name='accessories'),

    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_cart, name='add-to-cart'),
    path('minuscart/', views.minus_cart, name='minuscart'),
    path('pluscart/', views.plus_cart, name='pluscart'),
    path('remove_cart/', views.remove_cart, name='pluscart'),
    
    path('address/', views.address, name='address'),
    path("profile/", views.ProfileView.as_view(), name="profile"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)