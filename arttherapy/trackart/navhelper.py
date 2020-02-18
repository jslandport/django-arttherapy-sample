def getnavdictfromparamsdict(dparams, cururl):
   dnav = { }
   dcrumb = {}
   dback = {}
   for thiskey in dparams:
      if thiskey == 'art_clientid':
         ## should we link to this client?
         if dparams[thiskey] > 0:
            thislink = '/client/' + str(dparams[thiskey])
            if cururl != thislink:
               dcrumb[thislink] = 'This Client'
         ## link to the List-of-clients
         dback['/viewclients'] = 'All Clients'
      elif thiskey == 'art_appointmentid':
         if dparams[thiskey] > 0:
            thislink = '/appointment/' + str(dparams[thiskey])
            if cururl != thislink:
               dcrumb[thislink] = 'This Appointment'
         dback['/viewappointments'] = 'All Appointments'
      elif thiskey == 'art_paintingid':
         ## should we link to this painting?
         if dparams[thiskey] > 0 and dparams.get('art_appointmentid') > 0:
            thislink = '/appointment/' + str(dparams['art_appointmentid']) + '/painting/' + str(dparams[thiskey])
            if cururl != thislink:
               dcrumb[thislink] = 'This Painting'
         ## link to list-of-paintings
         dback['/viewpaintings'] = 'All Paintings'
   if dcrumb:
      dnav['dcrumb'] = dcrumb
   if dback:
      dnav['dback'] = dback
   return dnav
