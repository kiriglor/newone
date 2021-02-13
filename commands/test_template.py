from .models import Command

for i in Command.group_members.all():
    print(i.fullname)