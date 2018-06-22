#!/usr/bin/python
import os
import time
import commands
import webbrowser
option='''
1 To check current date and time 
2 To scan all your mac address in your connected network
3 To shutdown your pc after 15 minutes
4 To search something on google
5 To logout your current machine
6 To shutdown all machines connected on your network
7 To update status in facebook
8 To list ip address of given website
'''
print option 


choice =raw_input("enter your choice")


if choice=="1":
	print time.ctime()
elif choice=="2":
	print commads.getoutput("arp -a")
elif choice=="3":
        print "pc is going to shut down"
	print time.sleep(5)
	os.system("poweroff")
elif choice=="4":
	k=raw_input("enter what you want to search")
	print webbrowser.open_new_tab("https://www.google.com/search?q="+k)
elif choice=="5":
	commands.getoutput("exit")
elif choice=="6":
	print "wait"
elif choice=="7":
	print webbrowser.open_new_tab("https://www.facebook.com")
elif choice=="8":
	ip=raw_input("give website name to seacrch ip")
	print commands.getoutput("host "+ip)
