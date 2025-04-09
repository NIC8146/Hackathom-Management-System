from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("teams", views.teams, name="teams"),
    path("find_members", views.find_members, name="find_members"),
    path("invitations", views.invitations, name="invitations"),
    path("loginpage", views.login_register, name="loginpage"),
    path("logoutuser", views.logoutuser, name="logoutuser"),
    path("register_participant", views.register_participant, name="register_participant"),
    path("register_team", views.register_team, name="register_team"),
    path("participant_profile/<str:pk>/", views.participant_profile, name="participant_profile"),
    path("team_profile/<str:pk>/", views.team_profile, name="team_profile"),
    path("profilepage/<str:pk>/", views.profilepage, name="profilepage"),
] 