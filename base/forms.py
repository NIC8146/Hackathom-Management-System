from django import forms
# from django.forms import form.ModelForm
from .models import team, invitation, participant, problem_statement
from django.contrib.auth.forms import PasswordChangeForm

class teamform(forms.ModelForm):
    class Meta:
        model = team
        fields = "__all__"
        exclude = ["member1", "member2", "teamleader","member_number"]


class invitationForm(forms.ModelForm):
    class Meta:
        model = invitation
        fields = ["message"]

class register_participant_form(forms.ModelForm):
    class Meta:
        model = participant
        fields = ["name", "username", "phone", "skills", "email", "password"]
    
    def __init__(self, *args, **kwargs):
        super(register_participant_form, self).__init__(*args, **kwargs)
        self.fields['password'].widget = forms.PasswordInput()
    
class UpdateParticipantForm(forms.ModelForm):
    class Meta:
        model = participant
        fields = ['name', 'branch', 'dob', 'skills', 'phone', 'email']  # exclude password here
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
        }

class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Old Password'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'New Password'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm New Password'}))


class ProblemStatmentForm(forms.ModelForm):
    class Meta:
        model = problem_statement
        fields = "__all__"