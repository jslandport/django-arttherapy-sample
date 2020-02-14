# boards/urls.py

from django.urls import path
from . import views

urlpatterns = [
	path('', views.HomePageView.as_view()),
	path('viewclients', views.ClientCentricListView.as_view()),
	path('viewappointments', views.AppointmentCentricListView.as_view()),
	path('viewpaintings', views.PaintingCentricListView.as_view()),

   ## ('error' handling)
   path('notfound/<whatnotfound>/<int:idnotfound>', views.NotFound.as_view()),
	
	## CLIENT
	path('client/<int:art_clientid>', views.ClientView.as_view()),
   path('clientnew', views.ClientNew.as_view()),
	path('clientwrite/<int:art_clientid>', views.ClientWrite.as_view()),
	path('clientdelete/<int:art_clientid>', views.ClientDelete.as_view()),
	path('clientnotfound', views.ClientNotFound.as_view()),
	
	## APPOINTMENT
	path('appointment/<int:art_appointmentid>', views.AppointmentView.as_view()),
	path('appointmentnew', views.AppointmentNew.as_view()),
   path('appointmentwrite/<int:art_appointmentid>', views.AppointmentWrite.as_view()),
	path('appointmentdelete/<int:art_appointmentid>', views.AppointmentDelete.as_view()),
	
	## PAINTING
	path('appointment/<int:art_appointmentid>/painting/<int:art_paintingid>', views.PaintingView.as_view()),
	path('appointment/<int:art_appointmentid>/paintingnew', views.PaintingNew.as_view()),
	path('appointment/<int:art_appointmentid>/paintingwrite/<int:art_paintingid>', views.PaintingWrite.as_view()),
	path('appointment/<int:art_appointmentid>/paintingdelete/<int:art_paintingid>', views.PaintingDelete.as_view())
	
	## add/edit records(?)
]

###path('client/<int:art_clientid>', views.ClientView.as_view()),
