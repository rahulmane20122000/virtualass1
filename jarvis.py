import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import smtplib

engine = pyttsx3.init()
sound = engine.getProperty('voices')
# print(sound[1].id)
engine.setProperty('voice', sound[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        speak('good morning!')
    elif hour>12 or hour<16:
        speak('good afternoon!!')
    else:
        speak('good evening!!')
    speak('i am binod sir please tell me how may i help you')

def takecommand():
    #it takes input from mic
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold=1
        r.energy_threshold=3000
        audio=r.listen(source)

    try:
        print('reconising..')
        query=r.recognize_google(audio, language='en-in')
        # print(f"user said:{query}\n")
        print("user said:"+query)

    except Exception as e:
         print(e)  
         print("say that again pls...")
         return "None"
    return query
def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('rahulmane20122000@gmail.com','rahulmane123')
    server.sendmail('rahulmane2012000@gmail.com',to,content)
    server.close()

if __name__ == '__main__':
    wishme()
    while True:
          query=takecommand().lower()


          if 'who' in query:
            speak('searching wikipedia')
            query=query.replace("wikipedia","")
            results= wikipedia.summary(query,sentences=2)
            speak('According to wikipedia')
            speak(results)
          elif 'tell me something about your creator' in query:
              speak('rahul mane is my creator and i am manufactured in india')

          elif 'open youtube' in query:
              speak('sure sir')
              webbrowser.open("youtube.com")

          elif 'open google' in query:
              speak('sure sir')
              webbrowser.open("google.com")

          elif 'open facebook' in query:
              speak('sure sir')
              webbrowser.open("facebook.com")
          elif 'open instagram' in query:
              speak('sure sir')
              webbrowser.open("instagram.com")

          elif 'open stackoverflow' in query:
              speak('sure sir')
              webbrowser.open("stackoverflow.com")

          elif 'the time' in query:
              time=datetime.datetime.now().strftime("%H:%M:%S")
              speak(f"sir,the time is{time}")

          elif 'send email to dharmendra mane' in query:
                 try:
                     speak('what should i say')
                     content=takecommand()
                     to="dharmendrakumarhmane@gmail.com"
                     sendEmail(to, content)
                     speak("email has been sent")
                 except Exception as e:
                      speak('sorry my friend rahul i am not able to send the email')


          elif 'what is name of your creator' in query:
              speak('i am created by rahul an indian electronincs and telecommunication engineer')

          elif 'i am hungry' in query:
              speak('i have best thing for you on this hungry moment')
              webbrowser.open("swiggy.com")
          elif 'quit' in query:
              speak('ok sir thankyou for using me call me if you need me again')
              exit()
        








