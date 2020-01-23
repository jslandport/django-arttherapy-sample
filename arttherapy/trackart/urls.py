# boards/urls.py

from django.urls import path
from . import views

urlpatterns = [
	path('', views.HomePageView.as_view()),
	path('viewclients', views.ClientCentricListView.as_view()),
	path('aptmonth', views.AppointmentCentricListView.as_view()),
	
	## view 1 record:
	path('client/<int:art_client_id>', views.ClientOneView.as_view()),
	path('appointment/<int:art_appointment_id>', views.AppointmentOneView.as_view()),
	path('painting/<int:art_painting_id>', views.PaintingOneView.as_view())
	
	## add/edit records(?)
]

###path('client/<int:art_client_id>', views.ClientOneView.as_view()),
	
