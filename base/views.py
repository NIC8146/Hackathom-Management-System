from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# from django.http.request import QueryDict

from .models import team, participant, invitation
from .forms  import teamform, invitationForm

# Create your views here
def home(request):
    return render(request, 'base/home.html')


def login_register(request):
    if request.method == "POST":
        email = request.POST.get("Username")
        password = request.POST.get("Password")

        try:
            user = participant.objects.get(email=email)
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request,user)
                return redirect("/")
            else:
                messages.error(request, "wrong username or password")
        except Exception as e:
            print(str(e))
            messages.error(request, "wrong username or password")

    return render(request, 'base/login_register.html')

def logoutuser(request):
    logout(request)
    return redirect("/")

@login_required(login_url="/loginpage")
def invitations(request):
    type = request.GET.get("q",None)

    if type == "sent":
        i = invitation.objects.filter(sent_by=request.user)
    else:
        i = invitation.objects.filter(sent_to=request.user)
    context = {"invitations" : i}

    return render(request,"base/invitations.html", context)

@login_required(login_url="/loginpage")
def invite_participant(request, pk):

    participant_instance = participant.objects.get(id=pk)
    if request.user.isleader:
        if not participant_instance.in_team:
            if request.method == "POST":
                form = invitationForm(request.POST) # get data of form fields from http request
                if form.is_valid():
                    invitation_instance = form.save(commit=False) 
                    invitation_instance.sent_to = participant_instance
                    invitation_instance.sent_by = request.user
                    invitation_instance.save()
                return redirect("teams")
            else:
                form = invitationForm()
                context = {"form" : form}
        else:
            messages.error(request, "Participant is already in team")
    else:
        messages.error(request, "You are not a team leader")
    return render(request, 'base/invitationPage.html', context)

@login_required(login_url="/loginpage")
def accept_invitation(request, pk):
    p = participant.objects.get(name=request.user)
    invitation_instance = invitation.objects.get(id=pk)
    p.in_team = True
    p.teamname = invitation_instance.sent_by.teamname
    p.save()
    invitation_instance.delete()
    return redirect(invitations)

@login_required(login_url="/loginpage")
def delete_invitaion(request, pk):
    obj = invitation.objects.get(id=pk)
    obj.delete()
    return redirect(invitations)

###########################################################################################
def find_members(request):
    
    p = participant.objects.filter(is_registered=True)
    context = {"participants" : p}
    return render(request, 'base/find_members.html', context)

def participant_profile(request, pk):
    p = participant.objects.get(id=pk)
    skills = [x.strip() for x in p.skills.split(",")]
    context = {"participant" : p, "skills" : skills}
    return render(request, 'base/participant_profile.html', context)

@login_required(login_url="/loginpage")
def register_participant(request):
    if request.user.is_registered :
        messages.error(request, "You are already registered")
        return redirect('find_members')
    
    p = participant.objects.get(name=request.user)
    p.is_registered= True
    p.save()
    messages.success(request, "you are registered as participant")
    return find_members(request)

#############################################################################################

def teams(request):
    teams = team.objects.all()
    context = {"teams" : teams }
    return render(request, 'base/teams.html', context)

def team_profile(request, pk):
    t = team.objects.get(id=pk)
    context = {"team" : t}
    return render(request, 'base/team_profile.html', context)

@login_required(login_url="/loginpage")
def register_team(request):
    if request.user.in_team :
        messages.error(request, "You team is already registered")
        return redirect('teams')
    else:
        
        if request.user.is_registered:
            
            if request.method == "POST":
                
                
                form = teamform(request.POST) # get data of form fields from http request
                if form.is_valid():

                    # update team values
                    team_instance = form.save(commit=False)  # Don't save to DB
                    team_instance.teamleader = request.user  # Assign the team leader manually
                    team_instance.save() # team object formed in database

                    # update user fields
                    participant_instance = participant.objects.get(name=request.user)
                    participant_instance.in_team = True
                    participant_instance.isleader = True
                    participant_instance.teamname = team.objects.get(name=request.POST.get("name"))
                    participant_instance.save()

                    return redirect("teams")
                else:
                    messages.error(request, "form is not valid")
                    return redirect("teams")
            else:
                form = teamform()
                context = {"form" : form}
                return render(request, 'base/register_team.html', context)
               
        else:
            messages.error(request, "you are not registered participant")
            return redirect("teams")

@login_required(login_url="/loginpage")
def profilepage(request, pk):
    skills = [x.strip() for x in request.user.skills.split(",")]
    if pk == request.user.__str__():
        p = participant.objects.get(name=pk)
        context = {"participants" : p, "skills" : skills}
    else:
        messages.error(request, "user error")
        context = {}
    return render(request, "base/profilepage.html", context)
      