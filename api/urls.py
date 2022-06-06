from django.urls import path
from . import views

urlpatterns = [
    path('p1/', views.NEquipos, name='todos los equipos'),
    path('p2/', views.allPalyers, name='todos los jugadores'),
    path('p3/', views.Youngest, name='jugador mas joven'),
    path('p4/', views.oldest, name='jugador mas viejo'),
    path('p5/', views.substitute_players, name='cantidad de suplentes'),
    path('p6/', views.average_substitute_each_team, name='promedio suplentes de cada equipo'),
    path('p7/', views.Number_players, name='cantidad de jugadores por equipo'),
    path('p8/', views.average_age, name='promedio de edad'),
    path('p9/', views.average_players_ByTeam, name='promedio de jugadores por equipo'),
    path('p10/', views.technical_oldest, name='tecnico mas viejo'),
    # path('api/<int:pk>/', views., name=''),
]