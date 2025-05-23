from django.forms import ModelForm
from .models import team, invitation, participant

class teamform(ModelForm):
    class Meta:
        model = team
        fields = "__all__"
        exclude = ["member1", "member2", "teamleader","member_number"]


class invitationForm(ModelForm):
    class Meta:
        model = invitation
        fields = ["message"]

class register_participant_form(ModelForm):
    class Meta:
        model = participant
        fields = ["name", "username", "phone", "skills", "email", "password"]