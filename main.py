from os import popen,system
from time import sleep
import datetime

state=1 #State of the display 1 On 0 Off
ip_1="192.168.80.207" #Enter the IP address of the device that should keep the display awake
ip_2="192.168.40.51"


while True:
    current_time = datetime.datetime.now()
    hour = current_time.hour

    while hour <= 22 or hour >= 6:

        nmap_out=str(popen('nmap -sP '+ip_1).read()) #nmap command to scan on the given IP address
        nmap_out_2=str(popen('nmap -sP '+ip_2).read())
        sleep(4)
    
        if nmap_out.find('latency') == -1 and nmap_out_2.find('latency') == -1:  #looks for the word "latency" in the output
            if state==0 :                   #this nested if makes sure that commands are not repeated
                pass
            else :
                system('xset -display :0 dpms force off')  #Bash command that turns off the display
                state=0                             #Updating the display state variable

        elif nmap_out.find('latency') > 1 or nmap_out_2.find('latency') > 1:
            if state==1:
                pass
            else :
                system('xset -display :0 dpms force on') #Bash command to turn on the display
                state=1

    system('xset -display :0 dpms force off')

    sleep(10) #Scan rate in seconds
