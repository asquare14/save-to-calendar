from ics import Calendar, Event
c = Calendar()

my_events =[['Event1','2021-01-01 00:00:00','2021-01-01 00:00:01'],['Event2','2021-01-01 00:00:00','2021-01-01 00:00:02']]
for event in my_events:
    e = Event()
    e.name = event[0]
    e.begin = event[1]
    e.end = event[2]
    c.events.add(e)
    c.events

with open('schedule.ics', 'w') as my_file:
    my_file.writelines(c)
