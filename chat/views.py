from django.shortcuts import render

# Create your views here.


def room(request, room_name ,username ):

    return render(request, 'chat/room.html', {
        'room_name': room_name,
        'username' : username
    })

def base_view(request):

    return render(request,'chat/base.html')

