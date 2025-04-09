from django.contrib import admin
from .models import participant, team, problem_statement, invitation
# Register your models here.

admin.site.register(participant)
admin.site.register(team)
admin.site.register(problem_statement)
admin.site.register(invitation)