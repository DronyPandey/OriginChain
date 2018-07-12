from django.urls import path
from . import views

app_name = "mobileapp"
urlpatterns = [
    path('', views.index, name='index'),
    path('viewant/', views.ViewAntecedents, name='ViewAntecedents'),
    path('showant/', views.ShowAntecedents, name='ShowAntecedents'),
    path('move/', views.MoveInput, name='MoveInput'),
    path('movement/', views.Movement, name='Movement'),
    path('move/confirm/', views.MovementConfirm, name='MovementConfirm'),
]