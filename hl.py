from xml.etree import ElementTree
import gdata.calendar.data
import gdata.calendar.client
import gdata.acl.data
import atom.data
import time
import re


def PrintUserCalendars(calendar_client):
  feed = calendar_client.GetAllCalendarsFeed()
  print feed.title.text
  for i, a_calendar in enumerate(feed.entry):
    print '\t%s. %s' % (i, a_calendar.title.text,)

'''
client = gdata.calendar.client.CalendarClient(source='http://iiitd-codecc.appspot.com')
client.ClientLogin('anjishnu.22@gmail.com', 'anjishnu22', client.source)
PrintUserCalendars(client)
'''
#calendar = gdata.calendar.data.CalendarEntry()
#calendar.title = atom.data.Title(text='Little League Schedule')
#calendar.color = gdata.calendar.data.ColorProperty(value='#A32929')
'''
feed = client.GetCalendarAclFeed()
print feed.title.text
for i, a_rule in enumerate(feed.entry):
  print '\t%s. %s' % (i, a_rule.title.text,)
  print '\t\t Role: %s' % (a_rule.role.value,)
  print '\t\t Scope %s - %s' % (a_rule.scope.type, a_rule.scope.value)


rule = gdata.calendar.data.CalendarAclEntry()
rule.scope = gdata.acl.data.AclScope(value='swetank20@gmail.com', type='user')
roleValue = 'http://schemas.google.com/gCal/2005#%s' % ('editor')
rule.role = gdata.acl.data.AclRole(value=roleValue)
aclUrl = 'https://www.google.com/calendar/feeds/anjishnu.22@gmail.com/acl/full'
returned_rule = client.InsertAclEntry(rule, aclUrl)
print returned_rule

#updated_calendar = client.Update(calendar)
'''
calendar = gdata.calendar.data.CalendarEntry()
calendar.title = atom.data.Title(text='Little League Schedule 4')
calendar.summary = atom.data.Summary(text='This calendar contains practice and game times')
calendar.where.append(gdata.calendar.data.CalendarWhere(value='IIIT-Delhi'))
calendar.color = gdata.calendar.data.ColorProperty(value='#2952A3')
calendar.timezone = gdata.calendar.data.TimeZoneProperty(value='Asia/Kolkata')
calendar.hidden = gdata.calendar.data.HiddenProperty(value='false')

new_calendar = client.InsertCalendar(new_calendar=calendar)

print new_calendar

cal_id = '<ns0:entry ns1:etag="W/&quot;Ak8MRn47eCp7JGA9WhRTFUw.&quot;" ns1:kind="calendar#calendar" xmlns:ns0="http://www.w3.org/2005/Atom" xmlns:ns1="http://schemas.google.com/g/2005"><ns0:link href="https://www.google.com/calendar/feeds/lnp9puup56dpufc1npid7itauk%40group.calendar.google.com/private/full" rel="alternate" type="application/atom+xml" /><ns0:link href="https://www.google.com/calendar/feeds/lnp9puup56dpufc1npid7itauk%40group.calendar.google.com/private/full" rel="http://schemas.google.com/gCal/2005#eventFeed" type="application/atom+xml" /><ns0:link href="https://www.google.com/calendar/feeds/lnp9puup56dpufc1npid7itauk%40group.calendar.google.com/acl/full" rel="http://schemas.google.com/acl/2007#accessControlList" type="application/atom+xml" /><ns0:link href="https://www.google.com/calendar/feeds/default/owncalendars/full/lnp9puup56dpufc1npid7itauk%40group.calendar.google.com" rel="self" type="application/atom+xml" /><ns0:link href="https://www.google.com/calendar/feeds/default/owncalendars/full/lnp9puup56dpufc1npid7itauk%40group.calendar.google.com" rel="edit" type="application/atom+xml" /><ns0:category scheme="http://schemas.google.com/g/2005#kind" term="http://schemas.google.com/gCal/2005#calendarmeta" /><ns0:id>http://www.google.com/calendar/feeds/default/calendars/lnp9puup56dpufc1npid7itauk%40group.calendar.google.com</ns0:id><ns0:author><ns0:name>Little League Schedule 4</ns0:name></ns0:author><ns0:content src="https://www.google.com/calendar/feeds/lnp9puup56dpufc1npid7itauk%40group.calendar.google.com/private/full" type="application/atom+xml;type=feed" /><ns2:timezone value="Asia/Kolkata" xmlns:ns2="http://schemas.google.com/gCal/2005" /><ns0:updated>2011-11-05T18:48:07.000Z</ns0:updated><ns0:published>2011-11-05T18:48:07.938Z</ns0:published><ns2:color value="#2952A3" xmlns:ns2="http://schemas.google.com/gCal/2005" /><ns2:accesslevel value="owner" xmlns:ns2="http://schemas.google.com/gCal/2005" /><ns0:title>Little League Schedule 4</ns0:title><ns0:summary>This calendar contains practice and game times</ns0:summary><ns2:timesCleaned value="0" xmlns:ns2="http://schemas.google.com/gCal/2005" /><ns2:selected value="false" xmlns:ns2="http://schemas.google.com/gCal/2005" /><ns2:hidden value="false" xmlns:ns2="http://schemas.google.com/gCal/2005" /><ns1:where valueString="IIIT-Delhi" /><ns2:edited xmlns:ns2="http://www.w3.org/2007/app">2011-11-05T18:48:07.000Z</ns2:edited></ns0:entry>'
object1 = re.search( r"(https://www.google.com/calendar/feeds/)(.*)" , str(new_calendar) )
str1 = object1.group(2).split('/')[0]
print str1
'''
rule = gdata.calendar.data.CalendarAclEntry()
rule.scope = gdata.acl.data.AclScope(value= 'anjishnu.33@gmail.com', type='user')
roleValue = 'http://schemas.google.com/gCal/2005#%s' % ('read')
rule.role = gdata.acl.data.AclRole(value=roleValue)
aclUrl = 'https://www.google.com/calendar/feeds/anjishnu.22@gmail.com/acl/full'
returned_rule = client.InsertAclEntry(rule, aclUrl)
'''
