#searching item in net---------------------------------
def browser(self):
    speak_text_cmd('What You want to search for...')
    class browser:
        website=""
    
    search=browser()
    search.website=speech.recognize_google(audio)
    find=search.website
    
    if len(find.split()) <= 1: 
        if(find.endswith(".com")):
            wb.open('{}'.format(find), new=3)
            print("searching... ",find)
            speak_text_cmd("Open the File..")
        
        elif(find.endswith(".net")):
            wb.open('{}'.format(find), new=2)
            print("searching... ",find)
            speak_text_cmd("Open the File..")
        
        elif(find.endswith(".in")):
            wb.open('{}'.format(find), new=2)
            print("searching... ",find)
            speak_text_cmd("Open the File..")
        
        elif(find.endswith(".org")):
            wb.open('{}'.format(find), new=2)
            print("searching... ",find)
            speak_text_cmd("Open the File..")
        
        else:
            com=find+".com"
            wb.open('{}'.format(com), new=2)
            print("searching... ",find)
            speak_text_cmd("Open the File..")
    
    else:
        find=("https://www.google.com/search?q={}".format(find))
        wb.open('{}'.format(find),new=2)
        print("finding using else")
        speak_text_cmd("Open the File..")
    
    
    speak_text_cmd()
