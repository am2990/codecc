try:
  from xml.etree import ElementTree
except ImportError:
  from elementtree import ElementTree
import gdata.calendar
import gdata.calendar.client
import gdata.calendar.service
import gdata.acl.data
import atom.data
import time

def ClearACL():
  client = gdata.calendar.client.CalendarClient( source = "http://codecc-iiitd.appspot.com" )
  client.ClientLogin( 'codecc.iiitd@gmail.com' , 'sas120811' , client.source )
  acl_feed = client.GetCalendarAclFeed()
  for i, a_rule in enumerate(acl_feed.entry):
    print '\t%s. %s %s' % (i, a_rule.title.text, type(a_rule.title.text))
    print '\t\t Role: %s' % (a_rule.role.value,)
    print '\t\t Scope %s - %s' % (a_rule.scope.type, a_rule.scope.value)
    if(a_rule.title.text != 'owner'):
      client.Delete(a_rule.GetEditLink().href)
      
  
                
def DeleteCalendars():
  CODECC = gdata.calendar.client.CalendarClient( source = "http://codecc-iiitd.appspot.com" )
  CODECC.ClientLogin( 'codecc.iiitd@gmail.com' , 'sas120811' , CODECC.source )
  feed = CODECC.GetOwnCalendarsFeed()
  for entry in feed.entry:
    print 'Deleting calendar: %s' % entry.title.text
    if(entry.title.text == 'CODECC'):
        print 'will not delete codecc'
        pass
    else:
        print 'deleting'
        CODECC.Delete(entry.GetEditLink().href)


def PrintACL():
  client = gdata.calendar.client.CalendarClient( source = "http://codecc-iiitd.appspot.com" )
  client.ClientLogin( 'codecc.iiitd@gmail.com' , 'sas120811' , client.source )
  acl_feed = client.GetCalendarAclFeed()
  for i, a_rule in enumerate(acl_feed.entry):
    print '\t%s. %s %s' % (i, a_rule.title.text, type(a_rule.title.text))
    print '\t\t Role: %s' % (a_rule.role.value,)
    print '\t\t Scope %s - %s' % (a_rule.scope.type, a_rule.scope.value)
    
def PrintUserCalendars(client):
  feed = client.GetAllCalendarsFeed()
  cal = gdata.calendar.data.CalendarEntry()
  print feed.title.text
  for i, a_calendar in enumerate(feed.entry):
    print '\t%s. %s' % (i, a_calendar.title.text,)
    
def PrintEvents(calendar_client,cid = None):
  feeduri =  client.GetCalendarEventFeedUri(cid)
  feed = calendar_client.GetCalendarEventFeed(feeduri)
  print 'Events on Calendar: %s' % (feed.title.text,)
  for i, an_event in enumerate(feed.entry):
    print '\t%s. %s' % (i, an_event.title.text,)
    for p, a_participant in enumerate(an_event.who):
      pass
      #print '\t\t%s. %s' % (p, a_participant.email,)
      #print '\t\t\t%s' % (a_participant.attendee_status.value,)
  print 'Events on Primary Calendar: %s' % (feed.title.text,)
  for i, an_event in enumerate(feed.entry):
    print '\t%s. %s' % (i, an_event.title.text,)
    '''
    for p, a_participant in enumerate(an_event.who):
      print '\t\t%s. %s' % (p, a_participant.email,)
      print '\t\t\t%s' % (a_participant.attendee_status.value,)
    '''

def UpdateEvent(calendar_service, Event, new_title='FOUR-Test'):

  calendar_service = gdata.calendar.service.CalendarService()
  calendar_service.email = 'codecc.iiitd@gmail.com'
  calendar_service.password = 'sas120811'
  calendar_service.source = 'Google-Calendar_Python_Sample-1.0'
  calendar_service.ProgrammaticLogin()
  event = Event[0]
  calendar_service.DeleteEvent(event.GetEditLink().href)
  
  client = gdata.calendar.client.CalendarClient( source = "http://codecc-iiitd.appspot.com" )
  client.ClientLogin( 'codecc.iiitd@gmail.com' , 'sas120811' , client.source )
  cid = '2ehe8f4i8fomokpbg3h1r9vu6o%40group.calendar.google.com'
  InsertSingleEvent(client, title='FIVE-Test',
                      content='Meet for a quick lesson', where='On the courts',
                      start_time=None, end_time=None,cid=cid)
  return

  event.content.text = 'my text'
  event.when.pop()
  start_time = time.strftime('%Y-%m-%dT%H:%M:%S.000Z', time.gmtime())
  end_time = time.strftime('%Y-%m-%dT%H:%M:%S.000Z', time.gmtime(time.time()+3600))
  event.when.append(gdata.calendar.data.When(start=start_time, end=end_time))
  print event.when
  print 'Updating title of event from:\'%s\' to:\'%s\'' % (previous_title, event.title.text,)
  return calendar_service.UpdateEvent(event.GetEditLink().href, event)

def GetEvent(client,cid=None, text_query='FOUR-Test'):
  print 'Full text query for events on Calendar: \'%s\'' % ( text_query,)

  calendar_service = gdata.calendar.service.CalendarService()
  calendar_service.email = 'codecc.iiitd@gmail.com'
  calendar_service.password = 'sas120811'
  calendar_service.source = 'Google-Calendar_Python_Sample-1.0'
  calendar_service.ProgrammaticLogin()

  cid = cid.replace('%40','@')
  query = gdata.calendar.service.CalendarEventQuery(cid,'private','full' ,text_query)
  feed = calendar_service.CalendarQuery(query)
  return feed.entry
  for i, an_event in enumerate(feed.entry):
    print '\t%s. %s' % (i, an_event.title.text,)
    print '\t\t%s. %s' % (i, an_event.content.text,)
    for a_when in an_event.when:
      print '\t\tStart time: %s' % (a_when.start_time,)
      print '\t\tEnd time:   %s' % (a_when.end_time,)
  

def PrintAllEvents(calendar_service):
  feed = calendar_service.GetCalendarEventFeed()
  print 'Events on Primary Calendar: %s' % (feed.title.text,)
  for i, an_event in enumerate(feed.entry):
    print '\t%s. %s' % (i, an_event.title.text,)
    
def InsertSingleEvent(calendar_client, title='FOUR-Test',
                      content='Meet for a quick lesson', where='On the courts',
                      start_time=None, end_time=None,cid=None):
    feeduri =  client.GetCalendarEventFeedUri(cid)
    print feeduri
    print '/calendar/feeds/default/private/full'
    event = gdata.calendar.data.CalendarEventEntry()
    event.title = atom.data.Title(text=title)
    event.content = atom.data.Content(text=content)
    event.where.append(gdata.calendar.data.CalendarWhere(value=where))
    print str(calendar_client)
    if start_time is None:
      # Use current time for the start_time and have the event last 1 hour
      start_time = time.strftime('%Y-%m-%dT%H:%M:%S.000Z', time.gmtime())
      end_time = time.strftime('%Y-%m-%dT%H:%M:%S.000Z', time.gmtime(time.time()+3600))
      end_time = '2011-11-15T08:16:00.000Z'
      print start_time,end_time  
    event.when.append(gdata.calendar.data.When(start=start_time, end=end_time))
    new_event = calendar_client.InsertEvent(event , feeduri)
    print 'New single event inserted: %s' % (new_event.id.text,)
    print '\tEvent edit URL: %s' % (new_event.GetEditLink().href,)
    print '\tEvent HTML URL: %s' % (new_event.GetHtmlLink().href,)

    return new_event


client = gdata.calendar.client.CalendarClient( source = "http://codecc-iiitd.appspot.com" )
client.ClientLogin( 'codecc.iiitd@gmail.com' , 'sas120811' , client.source )

cid = '2ehe8f4i8fomokpbg3h1r9vu6o%40group.calendar.google.com'
#InsertSingleEvent(client,cid=cid)
#event = GetEvent(client,cid)  
#UpdateEvent(client,event)
#ClearACL()
#DeleteCalendars()
PrintACL()
