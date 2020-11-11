from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('core_engineer', views.core_engineer, name='core_engineer'),
    path('vfx_artist', views.vfx_artist, name='vfx_artist'),
    path('ui_designer', views.ui_designer, name='ui_designer'),
    path('data_scientist', views.data_scientist, name='data_scientist'),
]
