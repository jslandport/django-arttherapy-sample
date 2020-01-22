# boards/urls.py

from django.urls import path
from . import views

urlpatterns = [
	path('', views.HomePageView.as_view()),
	path('viewclients', views.ClientCentricListView.as_view()),
	path('aptmonth', views.AppointmentCentricListView.as_view()),
	
	path('client/<int:art_client_id>', views.ClientOneView.as_view(), name='viewoneclient')
]

###path('client/<int:art_client_id>', views.ClientOneView.as_view()),
	
