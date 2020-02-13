# boards/urls.py

from django.urls import path
from . import views

urlpatterns = [
	path('', views.HomePageView.as_view()),
	path('viewclients', views.ClientCentricListView.as_view()),
	path('viewappointments', views.AppointmentCentricListView.as_view()),
	path('viewpaintings', views.PaintingCentricListView.as_view()),
	
	## CLIENT
	path('client/<int:art_client_id>', views.ClientView.as_view()),
   path('clientnew', views.ClientNew.as_view()),
	path('clientwrite/<int:art_client_id>', views.ClientWrite.as_view()),
	path('clientdelete/<int:art_client_id>', views.ClientDelete.as_view()),
	path('clientnotfound', views.ClientNotFound.as_view()),
	
	## APPOINTMENT
	path('appointment/<int:art_appointment_id>', views.AppointmentView.as_view()),
	path('appointmentnew', views.AppointmentNew.as_view()),
   path('appointmentwrite/<int:art_appointment_id>', views.AppointmentWrite.as_view()),
	path('appointmentdelete/<int:art_appointment_id>', views.AppointmentDelete.as_view()),
	
	## PAINTING
	path('appointment/<int:art_appointment_id>/painting/<int:art_painting_id>', views.PaintingView.as_view()),
	path('appointment/<int:art_appointment_id>/paintingnew', views.PaintingNew.as_view()),
	path('appointment/<int:art_appointment_id>/paintingwrite/<int:art_painting_id>', views.PaintingWrite.as_view()),
	path('appointment/<int:art_appointment_id>/paintingdelete/<int:art_painting_id>', views.PaintingDelete.as_view())
	
	## add/edit records(?)
]

###path('client/<int:art_client_id>', views.ClientView.as_view()),
