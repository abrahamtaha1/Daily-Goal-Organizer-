from setupCalender import getCalService
import datetime

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']


def APICalendar(USER_STORAGE):
    today = datetime.datetime.now().isoformat()
    Calendar = getCalService()
    
    for singleString in USER_STORAGE:
        events_result = Calendar.events().list(calendarId = 'primary', singleEvents = True, timeMin = str(today)[0:11] + '00:00:00Z', orderBy = 'startTime').execute()
        events = events_result.get('items', [])
    
        TIME = datetime.time(7,0,0)
        
        for event in events:
            hourStart = event['start'].get('dateTime', event['start'].get('date'))[11:13]
            #minuteStart = event['start'].get('dateTime', event['start'].get('date'))[14:16]
            
            hourEnd = event['end'].get('dateTime', event['end'].get('date'))[11:13]
            minuteEnd = event['end'].get('dateTime', event['end'].get('date'))[14:16]
            
            if (int(hourStart) == TIME.hour):
                hourDiff = int(hourEnd) - int(hourStart)
                if hourDiff == 0:
                    TIME = datetime.time(TIME.hour + 1, 0, 0)
                else:
                    TIME = datetime.time(TIME.hour + hourDiff, 0, 0)
                
        ENDTIME = TIME
        if int(singleString[-1]) == 1:
            ENDTIME = datetime.time(TIME.hour + 3, 0, 0)
        elif int(singleString[-1]) == 2:
            ENDTIME = datetime.time(TIME.hour + 2, 0, 0)
        else:
            ENDTIME = datetime.time(TIME.hour + 1, 0, 0)

        string = singleString.split("|")
        sendToCalendar = {
            'summary' : string[0],
            'description' : string[1],
            'start': {
                'timeZone' : 'America/Toronto',
                'dateTime' : str(today)[0:11] + str(TIME)
            },
            'end' : {
                'timeZone' : 'America/Toronto',
                'dateTime' : str(today)[0:11] + str(ENDTIME)
                
            },
        }
        Calendar.events().insert(calendarId='primary', body=sendToCalendar).execute()

def sorting(USER_STORAGE):
    for i in range(0, len(USER_STORAGE)):
        key = USER_STORAGE[i]
        j = i-1
        while j >= 0 and int(key[-1]) < int(USER_STORAGE[j][-1]):
            USER_STORAGE[j+1] = USER_STORAGE[j]
            j -= 1
        USER_STORAGE[j+1] = key

    return USER_STORAGE
