from os import popen,system
from time import sleep
import datetime

home_state = 1
time_state = 1

def set_vars():
    global home_state,time_state
    home_state = 1 #State of the display 1 On 0 Off
    time_state = 1 #State of the display 1 On 0 Off

def check_phone_home():
    global home_state
    ip_1="192.168.80.207" #Enter the IP address of the device that should keep the display awake
    ip_2="192.168.40.51"
    nmap_out=str(popen('nmap -sP '+ip_1).read()) #nmap command to scan on the given IP address
    nmap_out_2=str(popen('nmap -sP '+ip_2).read())
    sleep(4)
    
    if nmap_out.find('latency') == -1 and nmap_out_2.find('latency') == -1:  #looks for the word "latency" in the output
        if home_state==0 :                   #this nested if makes sure that commands are not repeated
            pass
        else :
            #system('xset -display :0 dpms force off')  #Bash command that turns off the display
            home_state=0                             #Updating the display state variable

    elif nmap_out.find('latency') > 1 or nmap_out_2.find('latency') > 1:
        if home_state==1:
            pass
        else :
            #system('xset -display :0 dpms force on') #Bash command to turn on the display
            home_state=1
    return home_state

def check_time():
    global time_state
    current_time = datetime.datetime.now()
    hour = current_time.hour
    
    if hour>=6 and hour<=22:  #looks for the word "latency" in the output
        if time_state==1:                   #this nested if makes sure that commands are not repeated
            pass
        else :
            #system('xset -display :0 dpms force off')  #Bash command that turns off the display
            time_state=1                             #Updating the display state variable

    elif hour<=6 or hour>=22:
        if time_state==0:
            pass
        else :
            #system('xset -display :0 dpms force on') #Bash command to turn on the display
            time_state=0
    return time_state

def main():
    set_vars()
    while True:
        time_state = check_time()
        home_state = check_phone_home()
        if home_state==0 or time_state==0:
            system('xset -display :0 dpms force off')
        elif home_state==1 and time_state==1:
            system('xset -display :0 dpms force on')
        sleep(10) #Scan rate in seconds

if __name__ == "__main__":
    main()
