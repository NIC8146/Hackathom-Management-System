from django.urls import path
from . import views

urlpatterns = [

    # page links
    path("", views.home, name="home"), # home page
    path("teams", views.teams, name="teams"), # teams page
    path("find_members", views.find_members, name="find_members"), # find member page
    path("invitations", views.invitations, name="invitations"), # user invitations page
    path("invite_participant/<str:pk>",views.invite_participant,name="invite_participant"), # invitation page
    path("problem_statement", views.problem_statements, name="problem_statement"), # problem statements page
    path("add_problem_statment", views.add_problem_statment, name="add_problem_statment"),
    # invitation operation links
    path("accept_invitation/<str:pk>",views.accept_invitation, name="accept_invitation"), # delete invitation card
    path("delete_invitation/<str:pk>",views.delete_invitaion, name="delete_invitation"), # delete invitation card

    # login logout links
    path("loginpage", views.loginpage, name="loginpage"), # login page
    path("logoutuser", views.logoutuser, name="logoutuser"), # logout the user

    # register links
    path("registerpage",views.registerpage,name="registerpage"), # register the new user
    path("register_participant", views.register_participant, name="register_participant"), # register the participant
    path("register_team", views.register_team, name="register_team"), #register team page

    # profile links
    path("participant_profile/<str:pk>/", views.participant_profile, name="participant_profile"), # participant profile page
    path("team_profile/<str:pk>/", views.team_profile, name="team_profile"), # team profile page 
    path("profilepage/<str:pk>/", views.profilepage, name="profilepage"), # logined user profile page

    # update link
    path("update_profile", views.update_profile, name="update_profile"),

    # problem statment
    path("add_problem_statment", views.add_problem_statment, name="add_problem_statment"),
    path("delete_problem_statment/<str:pk>/", views.delete_problem_statment, name="delete_problem_statment"),
] 