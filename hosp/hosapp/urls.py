from django.urls import path
from .import views

urlpatterns = [
    
    path('',views.index,name='ho'),
    path('about',views.about,name='ab'),
    path('booking',views.booking,name='bo'),
    path('contact',views.contact,name='con'),
    path('dep',views.department,name='de'),
    path('doc',views.doctors,name='do'),
]