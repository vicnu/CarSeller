"""CarSeller URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path

from carseller_app import views
from django.contrib.auth import views as auth_views

from user import views as user_views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    # path("",views.index,name="home"),
    path('about/',views.dabout,name="about"),
    path('contacts/',views.contacts,name="contacts"),
    path('questions/',views.faq,name="faq"),

    path('profile/', user_views.profile, name="users-profile"),
    path('register/', user_views.register, name="users-register"),
    path('login/',auth_views.LoginView.as_view(template_name="users/login.html"),name="users-login"),
    path('logout/',auth_views.LogoutView.as_view(template_name="users/logout.html"),name="users-logout"),

    path("", views.SellListView.as_view(), name="carseller_app-home"),

    path('sell/<int:pk>',
         views.SellDetailView.as_view(template_name="carseller_app/sell_detail.html"),
         name="sell_detail"),
    path('sell/new/',views.SellCreateView.as_view(template_name="carseller_app/sellrequest_form.html"),name="sell-create"),
    path('sell/<int:pk>/update/', views.SellUpdateView.as_view(), name="sell-update"),
    path('sell/<int:pk>/delete/', views.SellDeleteView.as_view(), name="sell-delete"),
]

handler404='carseller_app.views.page_not_found'
handler403='carseller_app.views.error403'


handler500='carseller_app.views.error500'

if settings.DEBUG :
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)