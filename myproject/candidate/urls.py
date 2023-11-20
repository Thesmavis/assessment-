from django.urls import path
from . import views

urlpatterns = [
    path('post/',views.candidateview.as_view(),name='create'),
    path('get/',views.candidateview.as_view(),name='getall'),
    path('get/<int:id>/',views.candidateview.as_view(),name='byid'),
    path('patch/<int:id>/',views.candidateview.as_view(),name='patch'),
    path('delete/<int:id>/',views.candidateview.as_view(),name='delete'),
]