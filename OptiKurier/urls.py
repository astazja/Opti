"""OptiKurier URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from transport import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.LandingPageView.as_view(), name="url_landing_page"),
    path('courier/', views.CourierView.as_view(), name="url_courier"),
    path('sample/recive/', views.SampleReciveView.as_view(), name="url_sample_recive"),
    path('sample/delivery/', views.SampleDeliveryView.as_view(), name="url_sample_delivery"),
    path('sample/list/', views.SampleListView.as_view(), name="url_sample_list"),
    path('management/', views.ManagementView.as_view(), name="url_managment"),
    path('management/cars/', views.CarsManagementView.as_view(), name="url_cars_management"),
    path('car/details/<int:id>/', views.CarDetailView.as_view(), name="url_car_details"),
    path('car/add/', views.CarAddView.as_view(), name="url_car_add"),
    path('car/modyfy/<int:id>/', views.CarModyfyView.as_view(), name="url_car_modyfy"),
    path('management/drivers/', views.DriversManagementView.as_view(), name="url_drivers_management"),
    path('driver/details/<int:id>/', views.DriverDetailView.as_view(), name="url_driver_details"),
    path('driver/add/', views.DriverAddView.as_view(), name="url_driver_add"),
    path('driver/modyfy/<int:id>/', views.DriverModyfyView.as_view(), name="url_driver_modyfy"),
    path('management/locations/', views.LocationsManagementView.as_view(), name="url_locations_management"),
    path('location/details/<int:id>/', views.LocationDetailView.as_view(), name="url_location_details"),
    path('location/add/', views.LocationAddView.as_view(), name="url_location_add"),
    path('location/modyfy/<int:id>/', views.LocationModyfyView.as_view(), name="url_location_modyfy"),

    path('accounts/', include('users.urls')),
]
