from django.urls import path
from .views import main,future,add_property,about_us,contact_us,ml_algo,profile,show


urlpatterns = [
    path('', main),
    path('home/',main),
    path('add/', add_property),
    path('aboutus/', about_us),
    path('contactus/',contact_us),
    path('mlalgo/',ml_algo),
    path('profile/',profile),
    path('show/<x>',show),
    path('future/',future)
]