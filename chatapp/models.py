from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.models import Group
# from django.contrib.auth.models import Permission

# # Define a permission
# permission = Permission.objects.create(
#     codename='can_access',
#     name='Can access'
# )

# # Get or create a user group
# group = Group.objects.get_or_create(name='normal')[0]

# # Associate the permission with the group
# group.permissions.add(permission)

# class User(AbstractUser):
#     # is_admin = models.ManyToManyField(ListItem, blank=True, related_name="watchlist")

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=100)


    def __str__(self):
        return "Room : "+ self.name + " | Id : " + self.slug



class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return "Message is :- "+ self.content