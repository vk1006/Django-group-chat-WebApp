from django.shortcuts import render
from .models import Room,Message
from django.contrib.auth.decorators import user_passes_test

def admin_required(login_url=None):
    return user_passes_test(lambda u: u.is_admin, login_url=login_url)

# @staff_required(login_url="../admin")
# def series_info(request)
def rooms(request):
    rooms=Room.objects.all()
    return render(request, "rooms.html",{"rooms":rooms})

def room(request,slug):
    room_name=Room.objects.get(slug=slug).name
    messages=Message.objects.filter(room=Room.objects.get(slug=slug))
    
    return render(request, "room.html",{"room_name":room_name,"slug":slug,'messages':messages})

