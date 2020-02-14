def getnavdictfromparamsdict(dparams, cururl):
   dnav = { }
   for thiskey in dparams:
      if thiskey == 'art_clientid':
         ## should we link to this client?
         if dparams[thiskey] > 0:
            thislink = '/client/' + str(dparams[thiskey])
            if cururl != thislink:
               dnav[thislink] = 'This Client'
         ## link to the List-of-clients
         dnav['/viewclients'] = 'All Clients'
      elif thiskey == 'art_appointmentid':
         if dparams[thiskey] > 0:
            thislink = '/appointment/' + str(dparams[thiskey])
            if cururl != thislink:
               dnav[thislink] = 'This Appointment'
         dnav['/viewappointments'] = 'All Appointments'
      elif thiskey == 'art_paintingid':
         if dparams[thiskey] > 0 & dparams['art_appointmentid'] > 0:
            thislink = '/appointment/' + dparams['art_appointmentid'] + '/painting/' + str(dparams[thiskey])
            if cururl != thislink:
               dnav[thislink] = 'This Painting'
         dnav['/viewappointments'] = 'All Paintings'
   return dnav
