import pyttsx3
import time

def readableTime():

    now = time.ctime()
    
    st1 = now.split(' ')
    
    st2 = [temp.strip() for temp in st1]

    day = getDay(st2[0])
    
    return(f"{day} {st2[1]} {st2[2]} {st2[3]} {st2[4]}")
    
###################### End Function CODE #########################

def speakableTime():

    now = time.ctime()
    
    st1 = now.split(' ')
    
    st2 = [temp.strip() for temp in st1]

    day = getDay(st2[0])
    
    st3 = st2[3].split(':')
    
    if st3[0][0] == '0': t = st3[0][1] + st3[1] + " AM" #This removes superfluos zeroes
    
    elif int(st3[0]) < 12 and int(st3[0]) >= 10: t = st3[0] + st3[1] + " AM"
    
    elif int(st3[0]) >= 12: 
    
        if st3[0] != '12':
            st3[0] = str(int(st3[0]) - 12)
        t =  st3[0] + st3[1] + " PM"
    
    return(f"{day} {st2[1]} {st2[2]} {t} {st2[4]}")
    
###################### End Function CODE #########################
    
def getDay(abbr):

    switcher = {
    
        "Sun": "Sunday",
        "Mon": "Monday",
        "Tue": "Tuesday",
        "Wed": "Wednesday",
        "Thu": "Thursday",
        "Fri": "Friday",
        "Sat": "Saturday"
    }
    
    return(switcher.get(abbr))
    
###################### End Function CODE #########################

djinn = pyttsx3.init()

voices = djinn.getProperty('voices')

djinn.setProperty('voice', voices[1].id)

djinn.runAndWait()

t = time.localtime()

if t.tm_hour < 12:

    djinn.say("Good morning Levi!")

    djinn.runAndWait()
    
elif t.tm_hour >= 12 and t.tm_hour < 17:

    djinn.say("Good afternoon Levi!")

    djinn.runAndWait()
    
else:

    djinn.say("Good evening Levi!")

    djinn.runAndWait()
    
djinn.say(f"today is, {speakableTime()}")
print(readableTime())

djinn.runAndWait()
