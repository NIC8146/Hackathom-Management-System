from django.forms import ModelForm
from .models import team, invitation

class teamform(ModelForm):
    class Meta:
        model = team
        fields = "__all__"
        exclude = ["member1", "member2", "teamleader","member_number"]


class invitationForm(ModelForm):
    class Meta:
        model = invitation
        fields = ["message"]