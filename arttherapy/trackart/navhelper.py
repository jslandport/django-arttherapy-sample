def getnavdictfromparamsdict(dparams, cururl):
   dnav = { }
   for thiskey in dparams:
      if thiskey == 'art_clientid':
         ## should we link to this client?
         if dparams[thiskey] > 0:
            clink = '/client/' + str(dparams[thiskey])
            if cururl != clink:
               dnav[clink] = 'View Client'
         ## link to the List-of-clients
         dnav['/viewclients'] = 'Client-Centric View'
      elif thiskey == 'art_appointmentid':
         dnav['/viewappointments'] = 'Appointment-Centric View'
   return dnav