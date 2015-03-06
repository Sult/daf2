from django.contrib.auth.models import User, Group
from apps.users.models import UserControl

#add user
user = User.objects.create_user("sult", "123@234.com", "1234")
user.is_superuser = True
user.save()
UserControl.objects.create(user=user, confirmed=True)


#set initial data
print "Adding misc"
execfile("populate/misc.py")

print "Adding all skills"
execfile("populate/skills.py")


#setup usergroups
#DRYA moderators
moderator = Group(name="moderator")
moderator.save()



