 # howdy2 /views.py
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect

## from .forms import ArtTherapyForm
## from trackart import templates
from .models import art_client
from .models import art_appointment
from .models import art_painting
from .models import art_paintingXpaintcolor
from .models import art_paintingXclientmood


# Create your views here.
class HomePageView(TemplateView):
   def get(self, request, **kwargs):
      '''
      qcolor = paintcolor.objects.all().order_by('paintcolortitle')
      '''
      dfeatures = {
         './viewclients': 'Client-centric View',
         './aptmonth':  'Appointment-centric View',
      }
      context = {
         'dfeatures': dfeatures
      }
      return render(request, 'trackart/index.html', context=context)

 
class ClientCentricListView(TemplateView):
   def get(self, request, **kwargs):
      qclient = art_client.objects.all().order_by('art_clientlastname','art_clientfirstname')
      context = {
         'qclient': qclient
      }
      return render(request, 'trackart/clientlist.html', context=context)


class AppointmentCentricListView(TemplateView):
   def get(self, request, **kwargs):
      qsappointment = art_appointment.objects.all().order_by('art_appointmenttime')
      context = {
         'qsappointment': qsappointment
      }
      print(qsappointment)
      return render(request, 'trackart/appointmentlist.html', context=context)



class ClientOneView(TemplateView):
   def get(self, request, art_client_id):
      qsclient = art_client.objects.filter(pk=art_client_id)
      if len(qsclient) == 1:
         qrow = qsclient[0]
         qsapt = art_appointment.objects.filter(art_clientid = art_client_id)
         context = {
            'qoneclient': qrow,
            'qsappointment': qsapt,
            'pkid': art_client_id
         }
      else:
         context = {}
      return render(request, 'trackart/clientone.html', context=context)


class AppointmentOneView(TemplateView):
   def get(self, request, art_appointment_id):
      qsappointment = art_appointment.objects.filter(pk=art_appointment_id)
      if len(qsappointment) == 1:
         qrow = qsappointment[0]
         qspainting = art_painting.objects.filter(art_appointmentid = art_appointment_id)
         context = {
            'qoneappointment': qrow,
            'qspainting': qspainting,
            'pkid': art_appointment_id
         }
      else:
         context = {}
      return render(request, 'trackart/appointmentone.html', context=context)


class PaintingOneView(TemplateView):
   def get(self, request, art_painting_id):
      qspainting = art_painting.objects.filter(pk=art_painting_id)
      if len(qspainting) == 1:
         qrow = qspainting[0]
         qsxpaintcolor = art_paintingXpaintcolor.objects.filter(art_paintingid = art_painting_id)
         qsxclientmood = art_paintingXclientmood.objects.filter(art_paintingid = art_painting_id)
         context = {
            'qonepainting': qrow,
            'qsxpaintcolor': qsxpaintcolor,
            'qsxclientmood': qsxclientmood,
            'pkid': art_painting_id
         }
      else:
         context = {}
      return render(request, 'trackart/paintingone.html', context=context)
