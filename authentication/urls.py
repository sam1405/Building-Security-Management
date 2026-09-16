from django.urls import path, include
from .import views
from django.contrib import admin

urlpatterns = [
    path('', views.signup_view, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('homepagew/', views.homepagew_view, name='homepagew'),
    path('homepagepm/', views.homepagepm_view, name='homepagepm'),
    path('guestslist/', views.guestslist_view, name='guestslist'),
    path('addguests/', views.addguests_view, name='addguests'),
    path('about', views.about_view, name='about'),
    path('checkout/<int:guest_id>/', views.checkout_view, name='checkout'),
    path('checkin/<int:guest_id>/', views.checkin_view, name='checkin'),
]