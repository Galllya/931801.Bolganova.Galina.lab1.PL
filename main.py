import json
from datetime import timezone, datetime
from pytz import timezone, UnknownTimeZoneError
from tzlocal import get_localzone
def app(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    #GET
    if environ['REQUEST_METHOD'] == 'GET':
        time_zon = environ['PATH_INFO'][1:]
        # for output
        try:
            zone = ' in ' + time_zon.split('/')[1]
        except:
            zone = ' on server'
        # error
        if time_zon:
            try:
                time_zon = timezone(time_zon)
            except UnknownTimeZoneError:
                return [b'Error: Unknown time zone']
        if time_zon == "":
            time_zon = None
        time_now = datetime.now(time_zon)
        return [bytes('Time'+str(zone)+' now:  '+str(time_now.hour)+':'+str(time_now.minute)+':'+str(time_now.second),
                      encoding='utf-8')]
    #POST
    else:
        received = environ['wsgi.input'].read().decode("utf-8")
        text = json.loads(received)
        try:
            tz_start = timezone(text['tz_start'])
        except KeyError:
            tz_start = get_localzone()
        try:
            tz_end = timezone(text['tz_end'])
        except KeyError:
            tz_end = get_localzone()

        try:
            typep = text['type']
        except KeyError:
            return [b'Error: Dont have "type" ']
        time_now = datetime.now(tz_start)
        timezon_start = datetime.now(tz_start).utcoffset()
        timezon_end = datetime.now(tz_end).utcoffset()
        if timezon_start <= timezon_end:
            beetween = timezon_end - timezon_start
        else:
            beetween = '-'+str(timezon_start-timezon_end)
        beetween = str(beetween)
        time = str(time_now.hour) + ':' + str(time_now.minute) + ':' + str(time_now.second)
        date = str(time_now.day) + '.' + str(time_now.month) + '.' + str(time_now.year)
        if text['type'] == 'time':
            return [bytes(json.dumps({'time': time, 'tz': str(tz_start)}), encoding='utf-8')]
        elif text['type'] == 'date':
            return [bytes(json.dumps({'date': date, 'tz': str(tz_start)}), encoding='utf-8')]
        elif text['type'] == 'datediff':
            return [bytes(json.dumps({'time_beetween': beetween, 'tz_start': str(tz_start), 'tz_end': str(tz_end)}), encoding='utf-8')]
from paste.httpserver import serve
serve(app)

