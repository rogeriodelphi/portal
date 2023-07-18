from django.urls import path

from . import views

urlpatterns = [
    path('', views.TestView.as_view(), name='index'),
    path('pagina2/', views.Pagina2View.as_view(), name='index2')
]