 # howdy2 /views.py
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect

from .forms import ClientForm
from .forms import AppointmentForm
from .forms import PaintingForm
## from trackart import templates
from .models import art_client
from .models import art_appointment
from .models import art_painting
from .models import paintcolor
from .models import clientmood

from .navhelper import getnavdictfromparamsdict


#############################
##
##    BASICS
##



# Create your views here.
class HomePageView(TemplateView):
   def get(self, request, **kwargs):
      dfeatures = {
         './viewclients': 'Client-centric View',
         './viewappointments':  'Appointment-centric View',
         './viewpaintings':  'Painting-centric View',
      }
      context = {
         'dfeatures': dfeatures
      }
      return render(request, 'trackart/index.html', context=context)


#####    X-CENTRIC VIEWS
 
class ClientCentricListView(TemplateView):
   def get(self, request, **kwargs):
      qclient = art_client.objects.all().order_by('art_clientlastname','art_clientfirstname')
      context = {
         'qclient': qclient
      }
      return render(request, 'trackart/clientlist.html', context=context)


class AppointmentCentricListView(TemplateView):
   def get(self, request, **kwargs):
      qsappointment = art_appointment.objects.all().order_by('-art_appointmenttime')
      context = {
         'qsappointment': qsappointment
      }
      print(qsappointment)
      return render(request, 'trackart/appointmentlist.html', context=context)


class PaintingCentricListView(TemplateView):
   def get(self, request, **kwargs):
      qpainting = art_painting.objects.all().order_by('-createDate')
      context = {
         'qpainting': qpainting
      }
      return render(request, 'trackart/paintinglist.html', context=context)


######   CLIENT

class ClientView(TemplateView):
   def get(self, request, art_client_id):
      qsclient = art_client.objects.filter(pk=art_client_id)
      dnavlinks = getnavdictfromparamsdict(
         dparams = { 'art_clientid': art_client_id },
         cururl = request.path_info
      )
      ##{ '/viewclients': 'Client-Centric View' }
      if len(qsclient) == 1:
         qrow = qsclient[0]
         qsapt = art_appointment.objects.filter(art_clientid = art_client_id)
         context = {
            'qoneclient': qrow,
            'qsappointment': qsapt,
            'pkid': art_client_id,
            'dnavlinks': dnavlinks
         }
         return render(request, 'trackart/clientone.html', context=context)


class ClientNotFound(TemplateView):
   def get(self, request):
      return render(request, 'trackart/clientnotfound.html')
      


#############################
##
##    CLIENT - WRITE
##


class ClientNew(TemplateView):
   def get(self, request):
      form = ClientForm()
      dnavlinks = getnavdictfromparamsdict(
         dparams = { 'art_clientid': 0 },
         cururl = request.path_info
      )
      context = {
         'form': form,
         'dnavlinks': dnavlinks
      }
      return render(request, 'trackart/clientwrite.html', context=context)

   def post(self, request):
      thisform = ClientForm(request.POST)
      dnavlinks = getnavdictfromparamsdict(
         dparams = { 'art_clientid': 0 },
         cururl = request.path_info
      )
      if thisform.is_valid():
         ## process:
         qc = art_client.objects.create(
            art_clientfirstname = thisform.cleaned_data.get("art_clientfirstname"),
            art_clientlastname = thisform.cleaned_data.get("art_clientlastname"),
            art_clientdob = thisform.cleaned_data.get("art_clientdob")
         )
         qc.save()
         ## go back to client:
         return HttpResponseRedirect('/client/' + str(qc.id));
      else:
         ## send them back to the form:
         ##   >> REFACTOR >>  WHY DO I HAVE TO REPLICATE THIS IN THE 'GET' AND POST?
         form = ClientForm(request.POST)
         context = {
            'form': thisform,
            'dnavlinks': dnavlinks
         }
         return render(request, 'trackart/clientwrite.html', context=context)


###
###

class ClientWrite(TemplateView):
   def get(self, request, art_client_id):
      qsclient = art_client.objects.filter(pk=art_client_id)
      if len(qsclient) == 1:
         qrow = qsclient[0]
         thisdata = {
            'art_clientfirstname': qrow.art_clientfirstname,
            'art_clientlastname': qrow.art_clientlastname,
            'art_clientdob': qrow.art_clientdob
         }
         thisform = ClientForm(thisdata)
         dnavlinks = getnavdictfromparamsdict(
            dparams = { 'art_clientid': art_client_id },
            cururl = request.path_info
         )
         thiscontext = {
            'qoneclient': qrow,
            'pkid': art_client_id,
            'form': thisform,
            'dnavlinks': dnavlinks
         }
         return render(request, 'trackart/clientwrite.html', context=thiscontext)
      else:
         return HttpResponseRedirect('/clientnotfound')
      
   def post(self, request, art_client_id):
      thisform = ClientForm(request.POST)
      if thisform.is_valid():
         ## process;
         art_client.objects.filter(id=art_client_id).update(
            art_clientfirstname = thisform.cleaned_data.get("art_clientfirstname"),
            art_clientlastname = thisform.cleaned_data.get("art_clientlastname"),
            art_clientdob = thisform.cleaned_data.get("art_clientdob")
         )
         ##qc.save()
         return HttpResponseRedirect('/client/' + str(art_client_id));
      else:
         ##   >> REFACTOR >>  WHY DO I HAVE TO REPLICATE THIS IN THE 'GET' AND POST?
         thisdata = {
            'art_clientfirstname': thisform.cleaned_data.get("art_clientfirstname"),
            'art_clientlastname': thisform.cleaned_data.get("art_clientlastname"),
            'art_clientdob': thisform.cleaned_data.get("art_clientdob")
         }
         thisform = ClientForm(thisdata)
         dnavlinks = getnavdictfromparamsdict(
            dparams = { 'art_clientid': art_client_id },
            cururl = request.path_info
         )
         thiscontext = {
            'pkid': art_client_id,
            'form': thisform,
            'dnavlinks': dnavlinks
         }
         return render(request, 'trackart/clientwrite.html', context=thiscontext)
         

####
class ClientDelete(TemplateView):
   def get(self, request, art_client_id):
      art_client.objects.filter(id=art_client_id).delete()
      return HttpResponseRedirect('/viewclients')
   

##
## /client write
##



######   APPOINTMENTS


class AppointmentView(TemplateView):
   def get(self, request, art_appointment_id):
      qsappointment = art_appointment.objects.filter(pk=art_appointment_id)
      if len(qsappointment) == 1:
         qrow = qsappointment[0]
         qspainting = art_painting.objects.filter(art_appointmentid = art_appointment_id).order_by('createDate')
         print(my_url_path)
         dnavlinks = getnavdictfromparamsdict(
            { 'art_appointmentid': art_appointment_id },
            my_url_path
         )
         context = {
            'qoneappointment': qrow,
            'qspainting': qspainting,
            'pkid': art_appointment_id,
            'dnavlinks': dnavlinks
         }
      else:
         context = {}
      return render(request, 'trackart/appointmentone.html', context=context)


#############################
##
##    APPOINTMENTS - WRITE
##

class AppointmentNew(TemplateView):
   def get(self, request):
      thisdata = {}
      if 'art_clientid' in request.GET.keys():
         thisdata['art_clientid'] = request.GET['art_clientid']
      thisform = AppointmentForm(thisdata)
      context = {
         'form': thisform
      }
      return render(request, 'trackart/appointmentwrite.html', context=context)

   def post(self, request):
      thisform = AppointmentForm(request.POST)
      if thisform.is_valid():
         ## process:
         print(thisform.cleaned_data.get('art_appointmenttime'))
         qa = art_appointment.objects.create(
            art_clientid = thisform.cleaned_data.get("art_clientid"),
            art_appointmenttime = thisform.cleaned_data.get("art_appointmenttime")
         )
         qa.save()
         ## go to Appointment:
         return HttpResponseRedirect('/appointment/' + str(qa.id));
      else:
         ## send them back to the form:
         ##   >> REFACTOR >>  WHY DO I HAVE TO REPLICATE THIS IN THE 'GET' AND POST?
         form = AppointmentForm(request.POST)
         context = {
            'form': thisform
         }
         return render(request, 'trackart/appointmentwrite.html', context=context)


###

class AppointmentWrite(TemplateView):
   def get(self, request, art_appointment_id):
      qsappointment = art_appointment.objects.filter(pk=art_appointment_id)
      if len(qsappointment) == 1:
         qrow = qsappointment[0]
         thisdata = {
            'art_clientid': qrow.art_clientid.pk,
            'art_appointmenttime': qrow.art_appointmenttime
         }
         thisform = AppointmentForm(thisdata)
         thiscontext = {
            'qoneappointment': qrow,
            'pkid': art_appointment_id,
            'form': thisform
         }
         return render(request, 'trackart/appointmentwrite.html', context=thiscontext)
      else:
         return HttpResponseRedirect('/appointmentnotfound')
      
   def post(self, request, art_appointment_id):
      thisform = AppointmentForm(request.POST)
      if thisform.is_valid():
         ## process;
         art_appointment.objects.filter(id=art_appointment_id).update(
            art_clientid = thisform.cleaned_data.get("art_clientid"),
            art_appointmenttime = thisform.cleaned_data.get("art_appointmenttime")
         )
         return HttpResponseRedirect('/appointment/' + str(art_appointment_id));
      else:
         ##   >> REFACTOR >>  WHY DO I HAVE TO REPLICATE THIS IN THE 'GET' AND POST?
         thisdata = {
            'art_clientid': thisform.cleaned_data.get("art_clientid"),
            'art_appointmenttime': thisform.cleaned_data.get("art_appointmenttime")
         }
         thisform = AppointmentForm(thisdata)
         thiscontext = {
            'pkid': art_appointment_id,
            'form': thisform
         }
         return render(request, 'trackart/appointmentwrite.html', context=thiscontext)


##

class AppointmentDelete(TemplateView):
   def get(self, request, art_appointment_id):
      art_appointment.objects.filter(id=art_appointment_id).delete()
      return HttpResponseRedirect('/viewappointments')



##
## /appointments write
##




######   PAINTINGS

class PaintingView(TemplateView):
   def get(self, request, art_appointment_id, art_painting_id):
      qspainting = art_painting.objects.filter(pk=art_painting_id)
      if len(qspainting) == 1:
         qrow = qspainting[0]
         context = {
            'qpainting': qrow,
            'pkid': art_painting_id
         }
      else:
         context = {}
      return render(request, 'trackart/paintingone.html', context=context)


#############################
##
##    PAINTING - WRITE
##

class PaintingNew(TemplateView):
   def get(self, request, art_appointment_id):
      thisdata = {}
      thisform = PaintingForm(thisdata)
      context = {
         'form': thisform,
         'art_appointmentid': art_appointment_id
      }
      return render(request, 'trackart/paintingwrite.html', context=context)

   def post(self, request, art_appointment_id):
      thisform = PaintingForm(request.POST)
      if thisform.is_valid():
         ## process:
         ## 1) write the painting:
         qpaint = art_painting.objects.create(
            art_appointmentid = art_appointment.objects.get(pk = art_appointment_id),
            art_paintingtitle = thisform.cleaned_data.get('art_paintingtitle')
         )
         qpaint.save()
         qpaint.paintcolors.set( thisform.cleaned_data.get('paintcolors') )
         qpaint.clientmoods.set( thisform.cleaned_data.get('clientmoods') )

         ## go to Painting:
         return HttpResponseRedirect('/appointment/' + str(art_appointment_id) + '/painting/' + str(qpaint.id));
      else:
         ## send them back to the form:
         ##   >> REFACTOR >>  WHY DO I HAVE TO REPLICATE THIS IN THE 'GET' AND POST?
         form = PaintingForm(request.POST)
         context = {
            'form': thisform,
            'art_appointmentid': art_appointment_id
         }
         return render(request, 'trackart/paintingwrite.html', context=context)


###

class PaintingWrite(TemplateView):
   def get(self, request, art_appointment_id, art_painting_id):
      qpaint = art_painting.objects.filter(pk=art_painting_id)
      if len(qpaint) == 1:
         qrow = qpaint[0]
         thisform = PaintingForm(
            initial={
               'art_paintingtitle': qrow.art_paintingtitle,
               'paintcolors': qrow.paintcolors.all(),
               'clientmoods': qrow.clientmoods.all()
            }
         )
         thiscontext = {
            'qonepainting': qrow,
            'pkid': art_painting_id,
            'art_appointmentid': art_appointment_id,
            'form': thisform
         }
         return render(request, 'trackart/paintingwrite.html', context=thiscontext)
      else:
         return HttpResponseRedirect('/paintingnotfound')
      
   def post(self, request, art_appointment_id, art_painting_id):
      thisform = PaintingForm(request.POST)
      if thisform.is_valid():
         ## process:
         ## 1:  (Update the core table)
         art_painting.objects.filter(id=art_painting_id).update(
            art_paintingtitle = thisform.cleaned_data.get("art_paintingtitle")
         )
         
         ## 2:  update the Set:
         art_painting.objects.filter(id=art_painting_id)[0].paintcolors.set( thisform.cleaned_data.get('paintcolors') )
         art_painting.objects.filter(id=art_painting_id)[0].clientmoods.set( thisform.cleaned_data.get('clientmoods') )
         ## redirect
         return HttpResponseRedirect('/appointment/' + str(art_appointment_id) + '/painting/' + str(art_painting_id));
      else:
         ##   >> REFACTOR >>  WHY DO I HAVE TO REPLICATE THIS IN THE 'GET' AND POST?
         form = PaintingForm(request.POST)
         context = {
            'form': thisform,
            'art_appointmentid': art_appointment_id
         }
         return render(request, 'trackart/paintingwrite.html', context=context)


##

class PaintingDelete(TemplateView):
   def get(self, request, art_appointment_id, art_painting_id):
      art_painting.objects.filter(id=art_painting_id).delete()
      return HttpResponseRedirect('/appointment/' + str(art_appointment_id))

