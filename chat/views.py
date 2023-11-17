from django.shortcuts import render

def main(request):
	return render(request,"chat/main.html")

def room(request,room_name):
	return render(request,"chat/room.html",{"room_name":room_name})