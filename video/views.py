from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Comment, Video
from django.template.context_processors import csrf


def hello(request):
	names = ['Egor', 'Pavel', 'Evlampiy', 'Eva', 'Alukard']
	return render(request, "index.html", {'name':"Bogdan", 'names':names})
	return HttpResponse("<h1>Hello world</h1>")


def start(request):
	videos = Video.objects.all()
	comments = Comment.objects.all()
	return render(request, 'start.html', {'video':videos, "comment":comments})


def one_video(request, slug):
	mydict = {}
	mydict['video'] = Video.objects.get(slug=slug)
	mydict.update(csrf(request))
	return render(request, "onevideo.html", mydict)


def form(request):
	if request.POST:
		print("POST")
		print(request.POST['password'])
		print(request.POST['login'])
		return redirect("/hello/" + request.POST['slug'])
	if request.GET:
		print("GET")
		print(request.GET['password'])
		print(request.GET['login'])
		return redirect("/hello/" + request.GET['slug'])


def addcom(request):
	if request.GET:
		text = request.GET['comment']
		slug = request.GET['slug']
		video = Video.objects.get(slug = slug)
		newcomm = Comment()
		newcomm.video_id = video.id
		newcomm.user_id = request.user.id
		newcomm.text = text
		newcomm.save()
	return redirect('/hello/')

def get_title(request):
	video = Video.objects.filter(title=request.GET['title'])
	if video:
		return HttpResponse('Error')
	return HttpResponse('Hello')

def addlike(request):
	id = request.GET['id']
	if id[0] == 'l':
		id = id[4:]
	video = Video.objects.get(id=id)
	video.like += 1
	video.save()
	return HttpResponse(video.like)
# Create your views here.
