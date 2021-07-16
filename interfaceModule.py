import webbrowser 
import os
import subprocess

def mapper(val) :
    if val == 'one':
        return 1
    elif val == 'two':
        return 2
    elif val == 'three':
        return 3
    elif val == 'four':
        return 4
    elif val == 'five':
        return 5
    elif val == 'open':
        return 6
    elif val == 'close':
        return 7
    elif val == 'rock':
        return 8
    else:
        return 0
    

def interfacer(i, trueVal):
    i=int(mapper(i))
    if trueVal == True :
        if i==1 :
            print('Gesture - 1')
            webbrowser.open("http://www.google.com") 
            return
        elif i==2 :
            print('Gesture - 2')
            subprocess.Popen('C:\\Windows\\System32\\calc.exe')
            return
        elif i==3 :
            print('Gesture - 3')
            os.system("C:\\Windows\\notepad.exe")
            return
        elif i==4 :
            print('Gesture - 4')
            os.system("C:\\Windows\\vlc.exe")
        elif i==5 :
            print('Gesture - 5')
            # os.system("C:\\Windows\\notepad.exe")
        elif i==6 :
            print('Gesture - open')
            # os.system("C:\\Windows\\notepad.exe")
        elif i==7 :
            print('Gesture - close')
            # os.system("C:\\Windows\\notepad.exe")
        elif i==8 :
            print('Gesture - rock')
            # os.system("C:\\Windows\\notepad.exe")
        else :
            print("Gesture not defined")
    
    else :
        if i==1 :
            print('Gesture - 1-closer')
            #webbrowser.close("http://www.google.com")
        elif i==2 :
            print('Gesture - 2-closer')
            # subprocess.Popen('C:\\Windows\\System32\\calc.exe')
        elif i==3 :
            print('Gesture - 3-closer')
            # os.system("C:\\Windows\\notepad.exe")
        elif i==4 :
            print('Gesture - 4-closer')
            # os.system("C:\\Windows\\notepad.exe")
        elif i==5 :
            print('Gesture - 5-closer')
            # os.system("C:\\Windows\\notepad.exe")
        elif i==6 :
            print('Gesture - open-closer')
            # os.system("C:\\Windows\\notepad.exe")
        elif i==7 :
            print('Gesture - close-closer')
            # os.system("C:\\Windows\\notepad.exe")
        elif i==8 :
            print('Gesture - rock-closer')
            # os.system("C:\\Windows\\notepad.exe")
        else :
            print("Gesture not defined-closer")