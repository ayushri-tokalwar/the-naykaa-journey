from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('success-story/', views.success_story, name='success_story'),
    path('achievements/', views.achievements, name='achievements'),
    path('personal-life/', views.personal_life, name='personal_life'),
    path('about-nykaa/', views.about_nykaa, name='about_nykaa'),
    path('gallery/', views.gallery, name='gallery'),
]
