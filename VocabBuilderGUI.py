
#!/bin/bash/python3
#Creating GUI with tkinter
import speech_recognition as sr 
from tkinter import *
import random
import pyttsx3

vocab_list = ['were','does','came','full','over']
r = sr.Recognizer()

def get_word():
    return vocab_list[random.randint(0,len(vocab_list)-1)]
global current_word
current_word = get_word()

def speak_text(message):      
    # Initialize the engine 
    engine = pyttsx3.init()
    # engine.setProperty('voice', 'en-scottish') # Raspberry
    # engine.setProperty('rate', 110) # Raspberry?
    engine.setProperty('rate', 180) # mac?
    engine.say(message)  
    engine.runAndWait() 

def start():
    ChatLog.config(state=NORMAL)
    ChatLog.insert(END, current_word + '\n\n')
    ChatLog.config(foreground="#442265", font=("Verdana", 12 ))
    ChatLog.config(state=DISABLED)
    ChatLog.yview(END)


def send():
    global current_word
    try: 
        # use the microphone as source for input. 
        with sr.Microphone() as source: 
            # wait for a second to let the recognizer 
            # adjust the energy threshold based on 
            # the surrounding noise level  
            r.adjust_for_ambient_noise(source, duration=0.2) 
              
            #listens for the user's input  
            audio = r.listen(source) 
              
            # Using ggogle to recognize audio 
            return_text = r.recognize_google(audio) 
            return_text = return_text.lower()
            # print(return_text)
            if return_text == current_word:
                ChatLog.config(state=NORMAL)
                ChatLog.insert(END, "Good Job!" + '\n\n')
                ChatLog.config(foreground="#442265", font=("Verdana", 12 ))
                # speak_text(res)
            else:
                ChatLog.config(state=NORMAL)
                ChatLog.insert(END, "Sorry Try The Next One!" + '\n\n')
                ChatLog.config(foreground="#442265", font=("Verdana", 12 ))
            current_word =  get_word()
            start()



    except sr.RequestError as e:
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "Sorry Currently I am Having Connection Issues!" + '\n\n')
        ChatLog.config(foreground="#442265", font=("Verdana", 12 ))
        print("Could not request results; {0}".format(e)) 
          
    except sr.UnknownValueError:
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "Sorry, I didn't get that. Try Again" + '\n\n')
        ChatLog.config(foreground="#442265", font=("Verdana", 12 ))
        print("No Speech Detected")




base = Tk()
base.title("Hello")
base.geometry("400x500")
base.resizable(width=FALSE, height=FALSE)

#Create Chat window
ChatLog = Text(base, bd=0, bg="white", height="8", width="50", font="Arial",)

ChatLog.config(state=DISABLED)

#Bind scrollbar to Chat window
scrollbar = Scrollbar(base, command=ChatLog.yview, cursor="heart")
ChatLog['yscrollcommand'] = scrollbar.set

#Create Button to send message
SendButton = Button(base, font=("Verdana",12,'bold'), text="Read", width="12", height=5,
                    bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff',
                    command= send )

#Create the box to enter message
EntryBox = Text(base, bd=0, bg="white",width="29", height="5", font="Arial")
#EntryBox.bind("<Return>", send)


#Place all components on the screen
scrollbar.place(x=376,y=6, height=386)
ChatLog.place(x=6,y=6, height=386, width=370)
EntryBox.place(x=128, y=401, height=90, width=265)
SendButton.place(x=6, y=401, height=90)

start()
base.mainloop()


# who do you work for
# <HUMAN>

