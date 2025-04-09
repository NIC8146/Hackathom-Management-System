from django.db import models
from django.contrib.auth.models import AbstractUser

class participant(AbstractUser):
    name = models.CharField(max_length=25)
    username = models.CharField(max_length=15, unique=True)
    branch = models.CharField(max_length=25)
    dob = models.DateField(null=True) # date of birth
    teamname = models.ForeignKey("team", on_delete=models.SET_NULL, null=True, blank=True, related_name="team")
    creation_time = models.DateTimeField(auto_now_add=True)
    skills = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    is_registered = models.BooleanField(default=False)
    in_team = models.BooleanField(default=False)
    isleader = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username","name"]

    def __str__(self):
        return self.name

class team(models.Model):
    name = models.CharField(max_length=35, unique=True)
    member_number = models.CharField(max_length=1, default="1")
    problem_statement = models.ForeignKey("problem_statement", on_delete=models.SET_NULL, null=True)
    teamleader = models.CharField(max_length=25, null=True)
    member1 = models.CharField(max_length=25,null=True,blank=True)
    member2 = models.CharField(max_length=25, null=True,blank=True)

    def __str__(self):
        return self.name

class problem_statement(models.Model):
    description = models.TextField()

    def __str__(self):
        return self.description

class invitation(models.Model):
    sent_by = models.ForeignKey("participant", on_delete=models.SET_NULL, null=True, related_name="invitation_sent_by")
    sent_to = models.ForeignKey("participant", on_delete=models.SET_NULL, null=True, related_name="invitation_sent_to")
    message = models.TextField(default="hi, i want you to be member of my team")
    timedate = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-timedate"]

    def __str__(self):
        return self.message
