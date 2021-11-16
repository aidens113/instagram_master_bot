import pyautogui
import time
import math
import random
import os
import sys
import requests
import wmi
import imaplib
import email
from email.header import decode_header
import webbrowser
import threading
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from os.path import expanduser
import concurrent.futures
from datetime import datetime
import urllib.request
import cv2
import random
import math
import os
import sys
import requests
import selenium


#os.system("taskkill /im chrome.exe")


def checkaccmade(user, passw):
    mac = str(str(random.randint(0,9))+'BD87DF'+str(random.randint(0,9))+'-'+str(random.randint(1111,9999))+'-'+str(random.randint(1111,9999))+'-2D2G-7A0FA9E0BE29')
    header1 = {
        'content-type':'application/json',
        'accept':'*/*',
        'appversion':'7.9.0.00396',
        'sku':'com.gogii.textplus',
        #'if-none-match':donotmatch,
        'accept-encoding':'gzip, deflate',
        'platform':'iOS',
        'accept-language':'en-CA;q=1',
        'user-agent':'textPlus/7.9.0 (iPhone; iOS 13.7; Scale/2.00)',#'textPlus/7.9.0 (iPhone; iOS 13.7; Scale/2.00)',
        'network':'nextplus',
        'device':'iPhone8,1',
        'carrier':'Telus',
        'udid':mac
    }
    jsondata = {
         "password": passw,
         "username": user 
     }

    response = requests.post("https://cas.prd.gii.me/v2/ticket/ticketgranting/user", headers=header1, json=jsondata)
    if "400" in str(response) or "401" in str(response) or "403" in str(response) or "404" in str(response):
        print("Error code on making ticket. Account was not made. Trying again")
        return False
    else:
        print("Made acc successfully")
        return True

def randkeys(element, keys):
    for myi in keys.split():
        element.send_keys(keys)
        time.sleep(random.uniform(0.05, 0.25))

def clickpy(element):
    pyautogui.moveTo(element)
    time.sleep(1)
    pyautogui.click()
    time.sleep(0.5)


def getsms():
    
    return sms

def changenum():
    
    return num



def getopen():
    try:
        openamnt = 0
        processes = wmi.WMI()
        for process in processes.Win32_Process():
            if "igbotcreator.exe" in process.Name :
                openamnt += 1
                print(process.Name)

        if openamnt >= 3:
            print("Returning true")
            return True
        else:
            return False
    except Exception as r:
        print("getopenpy error"+str(r))        



#######################################
#BLUESTACKS FUNCTIONS

def bsimg(path):
    
    return pyautogui.locateCenterOnScreen(str("bsimg/"+str(path)+".PNG"),confidence=0.95)

def proxyimg(path):
    return pyautogui.locateCenterOnScreen(str("proxyimg/"+str(path)+".PNG"),confidence=0.8)

def tpimg(path):
    return pyautogui.locateCenterOnScreen(str("textplusimg/"+str(path)+".PNG"),confidence=0.8)

def proxyimg(path):
    return pyautogui.locateCenterOnScreen(str("proxyimg/"+str(path)+".PNG"),confidence=0.8)



def newbsinstance():
    try:
        clickpy(bsimg("newinstance") )
        time.sleep(2)
        clickpy(bsimg("cloneinstance"))
        time.sleep(2)
        if bsimg("clonenum") != None:
            
            clickpy(bsimg("clonenum"))
            time.sleep(1)
            pyautogui.keyDown("ctrl")
            time.sleep(0.3)
            pyautogui.press("a")
            time.sleep(0.3)
            pyautogui.keyUp("ctrl")
            time.sleep(2)
            pyautogui.write("1")
            time.sleep(2)
            
            
        time.sleep(2)
        clickpy(bsimg("create"))
        while True:
            if bsimg("2starts") != None:
                print("Finished cloning")
                break
        
    except Exception as ee:
        print("Error with new bs image: "+str(ee))

def startbsinstance():
    try:
        time.sleep(5)
        clickpy((bsimg("starticon").x , (bsimg("starticon").y + 30)))
        while True:
            if bsimg("loaded") != None:
                print("Finished loaded")
                break
            
        clickpy(bsimg("maximize"))
        for _ in range(15):
            if bsimg("exitad") != None:
                clickpy(bsimg("exitad"))
                break
            time.sleep(0.5)
        time.sleep(2)
        
    except Exception as ee:
        print("Error with starting bs image: "+str(ee))


def deleteinstance():
    try:
        clickpy(bsimg("xbutton"))
        time.sleep(6)
        clickpy((bsimg("delete").x , bsimg("delete").y))
        time.sleep(3)
        clickpy(bsimg("delete2"))
        
    except Exception as ee:
        print("Error in deleteinstance: "+str(ee))

#####################################
#TEXTPLUS FUNCTIONS


def checkerrors():
    if pyautogui.locateCenterOnScreen("textplusimg/unavailable1.PNG", confidence=0.8) != None:
        print("Found error. Restarting loop")
        clickpy((707, 723))
        clickpy((707, 723))
        clickpy((707, 723))
        return True
    if pyautogui.locateCenterOnScreen("textplusimg/unknownerror.PNG", confidence=0.8) != None:
        print("Found error. Restarting loop")
        clickpy((707, 723))
        clickpy((707, 723))
        clickpy((707, 723))
        return True
    if pyautogui.locateCenterOnScreen("textplusimg/signuperror.PNG", confidence=0.8) != None:
        print("Found error. Restarting loop")
        
        return "signuper"
    

def textpluspopups():
    try:
        checkerrors()
        while tpimg("continue") != None:
            clickpy(tpimg("continue"))
        while tpimg("deny") != None:
            clickpy(tpimg("deny"))
        while tpimg("saveandclose") != None:
            clickpy(tpimg("saveandclose"))
    except:
        print("Error with textpluspopups")

def signuptextplus(user, passw):
    totali = 0
    while True:
        try:
            totali += 1
            print("Starting textplus signup loop")
            breakl = False
            clickpy(bsimg("exitad"))
            clickpy((937, 293))
            time.sleep(1)
            pyautogui.moveTo(tpimg("close1"))
            time.sleep(1)
            clickpy(bsimg("home2"))
            time.sleep(1)
            clickpy(tpimg("textplus2"))
            clickpy(tpimg("textplus"))
            time.sleep(4)
            clickpy((741, 99))
            time.sleep(1)
            while True:
                if bsimg("exitad") != None:
                    clickpy(bsimg("exitad"))
                if checkerrors() == True:
                    breakl = True
                    break
                time.sleep(1)
                if tpimg("signup") != None:
                    clickpy(tpimg("signup"))
                    time.sleep(1)
                    break
                if tpimg("textplus2") != None or tpimg("textplus") != None:
                    breakl = True
                    break
            textpluspopups()

            while True:
                if checkerrors() == True:
                    breakl = True
                    break
                if tpimg("username") != None:
                    clickpy(tpimg("username"))
                    break
                if tpimg("signup") != None:
                    breakl = True
                    break
                if tpimg("textplus2") != None or tpimg("textplus") != None:
                    breakl = True
                    break
                textpluspopups()
                
            if breakl == False:
                time.sleep(1)
                pyautogui.write(str(user))
                time.sleep(2)
                clickpy(tpimg("password"))
                time.sleep(1)
                pyautogui.write(str(passw))
                time.sleep(1)
                clickpy(tpimg("tos"))
                time.sleep(1.5)
                clickpy(tpimg("signup2"))
                time.sleep(2)
            i = 0
            while True:
                i += 1
                if tpimg("signup") != None:
                    if i >= 25:
                        clickpy(tpimg("signup2"))
                        i = 0
                if checkerrors() == True:
                    breakl = True
                    break
                if bsimg("captcha") != None:
                    break
                
                if tpimg("signup") != None:
                    breakl = True
                    break
                if tpimg("textplus2") != None or tpimg("textplus") != None:
                    breakl = True
                    break
                textpluspopups()
                time.sleep(1)
                
            if checkerrors() != True and breakl == False:
                os.system("start recaptchasolver.pyw")
            time.sleep(3)
            i = 0
            while True:
                i += 1
                if checkerrors() == True:
                    breakl = True
                    break
                if i > 60:
                    breakl = True
                    break
                if bsimg("verify") == None:
                    break
                if tpimg("signup") != None:
                    breakl = True
                    break
                if tpimg("textplus2") != None or tpimg("textplus") != None:
                    breakl = True
                    break
                
                textpluspopups()
                time.sleep(0.8)
                
            if breakl == False:                
                
                time.sleep(20)
                textpluspopups()
                time.sleep(2)
                textpluspopups()
                time.sleep(2)
                textpluspopups()
                #madeacc = checkaccmade(user, passw)
                #if madeacc == True:
                if checkerrors() != "signuper":
                    f = open("textplusaccs.txt","a")
                    f.write(str(user)+"-1:"+str(passw)+"\n")
                    f.close()
                return
            else:
                print("Breaking first loop to restart on crash")
                
            time.sleep(8)
                
        except Exception as ee:
            print("Error with signing up textplus: "+str(ee))



################################
#Proxifier Functions

def changeproxy(proxy):
    clickpy(proxyimg("icon"))
    time.sleep(0.2)
    pyautogui.click()
    time.sleep(1)
    pyautogui.click()
    time.sleep(0.2)
    pyautogui.click()
    time.sleep(3)
    while True:
        if proxyimg("profile") != None:
            clickpy(proxyimg("profile"))
            break

    time.sleep(1)
    clickpy(proxyimg("proxyservers"))
    time.sleep(2)
    clickpy(proxyimg("edit"))
    time.sleep(3)
    pyautogui.write(proxy)
    time.sleep(3)
    clickpy(proxyimg("ok"))
    time.sleep(2)
    clickpy(proxyimg("ok"))
    time.sleep(3)
    clickpy(proxyimg("xbutton"))
    
def closeproxy():
    for i in range(7):
        os.system("taskkill /F /IM Proxifier.exe")
        time.sleep(0.1)

def openproxy():
    clickpy(proxyimg("icon"))
    time.sleep(0.2)
    pyautogui.click()
    time.sleep(1)
    pyautogui.click()
    time.sleep(0.2)
    pyautogui.click()
    time.sleep(1)


def gentpuser():
    chars = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    user = ""
    for i in range(random.randint(7, 10)):
        user = str(user + chars[random.randint(0, 24)])
    user = str(user+str(random.randint(0,9)))
    
    return user

def gentppass():
    chars = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    passw = ""
    for i in range(random.randint(7, 10)):
        passw = str(passw + chars[random.randint(0, 24)])
    passw = str(passw+str(random.randint(0,9)))
    passw = str(passw+"$!!")
    
    return passw

time.sleep(5)
print("Starting...")
while True:
    file = open("textplusproxies.txt","r")
    proxies = file.readlines()
    file.close()
    for proxy in proxies:
        changeproxy(str(proxy))
        newbsinstance()
        startbsinstance()
        signuptextplus(gentpuser(), gentppass())
        deleteinstance()
        


#while True:
    #file = open("newaccounts.txt","r")
    #newaccs = file.readlines()
    #file.close()
    #if len(newaccs) <= 30:
        #acc = createaccount()
        #if acc != "none":
            #file = open("newaccounts.txt","w")
            #file.writelines(newaccs)
            #file.write(acc)
            #file.close()


        
