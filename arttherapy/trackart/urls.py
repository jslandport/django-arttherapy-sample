# boards/urls.py
from django.conf.urls import url
from trackart import views

## 	url(r'^$', views.HomePageView, name='home'), ## .as_view()),

urlpatterns = [
	url(r'^$', views.HomePageView.as_view()),
	## url(r'^about/$', views.AboutPageView.as_view()),
	## url(r'^fink/$', views.FinkPageView.as_view()),
	## url(r'^arty/$', views.artTherapyPageView.as_view()),
	## url(r'^thanks/$', views.thanksPageView.as_view()),
]

	
