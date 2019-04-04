from django.urls import re_path
from .views import hello, start, one_video, form, addcom, get_title, addlike

urlpatterns = [
	re_path(r'^$', start),
	re_path(r'form/', form),
	re_path(r'addcomm/', addcom),
	re_path(r'get_title/', get_title),
	re_path(r'addlike/', addlike),
	re_path(r'(?P<slug>[-\w]+)/$', one_video),
]