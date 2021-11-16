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
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from subprocess import CREATE_NO_WINDOW


##########################
#TEXTPLUS API


mac = str(str(random.randint(0,9))+'BD87DF'+str(random.randint(0,9))+'-'+str(random.randint(1111,9999))+'-'+str(random.randint(1111,9999))+'-2D2G-7A0FA9E0BE29')
user = ""
passw = ""

def getticket(user, passw):
    for _ in range(5):
        try:
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
                print("Error code on making ticket. Account was not made. Trying again. ARE YOU USING VPN??")
            
            #print(response)
            #print(response.json())
            #print(response.text)

            ticket = response.json()['ticket']
            #print("Temp ticket: "+str(ticket))



            #gets perm ticket

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
                "service": "nextplus",
                "ticketGrantingTicket":ticket
            }

            response = requests.post("https://cas.prd.gii.me/v2/ticket/service", headers=header1, json=jsondata)
            
            
            #print(response)
            #print(response.json())

            ticket = "CASST "+str(response.json()['ticket'])
            #print("Perm ticket: "+str(ticket))

        except:
            print("Error getting token. Trying again")
            

    return ticket


def getpersonafornumber(token):
    #gets perm ticket
    header1 = {
        'content-type':'application/json',
        'authorization':token,
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
   # jsondata = {
        #"service": "nextplus",
        #"ticketGrantingTicket":ticket
    #}

    response = requests.get("https://ums.prd.gii.me/me?projection=inline", headers=header1)
    #print(response.text)
    #print(response.headers)
    
    #try:
    #str("https://ums.prd.gii.me/users/")
                            
    path = response.json()['personas'][0]['id']
    
    #print("User path: "+str(path))
    #except:
        #print("Error getting location")
        #print("Response headers: "+str(response.headers))
    return path



def getuser(token):
    #gets perm ticket

    header1 = {
        'content-type':'application/json',
        'authorization':token,
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
   # jsondata = {
        #"service": "nextplus",
        #"ticketGrantingTicket":ticket
    #}

    response = requests.get("https://ums.prd.gii.me/me?projection=inline", headers=header1)
    #print(response.text)
    #print(response.text)
    #print(response.headers)
    path = ""
    #try:
    #str("https://ums.prd.gii.me/users/")
    path = response.json()['primaryPersona']['user']['id']
    #print("User path: "+str(path))
    #except:
        #print("Error getting location")
        #print("Response headers: "+str(response.headers))
    return path


def changenumber(profile, token):
    phonenum = "ERROR"
    for myii in range(5):
        try:
            f = open("localeid.txt","r")
            alllocals = f.readlines()
            f.close()

            local = str(alllocals[random.randint(0, 40)].strip().replace("\n","").replace("\r",""))
            #print(local)
            header1 = {
                'host':'ums.prd.gii.me',
                'content-type':'application/json',
                'authorization':token,
                'accept':'*/*',
                'appversion':'7.9.0.00396',
                'sku':'com.gogii.textplus',
                #'if-none-match':donotmatch,
                'accept-encoding':'gzip, deflate',
                'accept-language':'en-US;q=1',
                'platform':'iOS',
                'user-agent':'textPlus/7.9.0 (iPhone; iOS 13.7; Scale/2.00)',#'textPlus/7.9.0 (iPhone; iOS 13.7; Scale/2.00)',
                'network':'nextplus',
                'device':'iPhone8,1',
                'carrier':'Telus',
                'udid':mac
            }
            jsondata = {
                "deviceUdid": mac,#mac,
                "localeId": local,
                "platform": "iOS",
                "recaptchaCode": 'gJUT7-9LACI3hf91rP5QtxuBw1-3Ee6gbZs1kKCXTxPXAEtn43Hjn5MXl9xOyGvqh54cA50kS7ysQphlrc1SuQoYQ9MUEW4VghbZHXkRIdekXhj_tP7VoRgfqAsKryQH9jjVeUwDv8guxB4UApisJNMCFylfhCHQhLa-S8pq9ORZ2OgqtMRKLvEXxi_iQy2KUS1u-wHHnQ3LTGl7WGCJb82EUS732D-LyP-s2s3z000KtYbhcBIK_a3O-tRahgcyvkedtXtfl35MkLRqTbcIYSSBizssoBqRiZjaXvMPCnJSRFJqYzXt0CcIgtXEJy4-xjv66rb79osHtA7VyxRhLsAfz_KOxg3UHEXKjg-aU0OuDGjx4po725AmS9aGWd7csduaxp6Qj_OzeHDA-VhMGsRH1R3PMFsNVp7bOhr00DGBMHYlHbOf2HHR0bhXnh6mNCXqLPSbeE5r9I6Db-uuQEUkODhRR9C8U39i1LdSfL7ZFPWrQ'#str(recaptcha())
            }
            
            url = str("https://ums.prd.gii.me/personas/"+str(profile)+"/tptn/allocate")
                                                       #ff808181791d08160179340df2813631 # one used
            #print("URL: "+str(url))
            response = requests.post(url, headers=header1, json=jsondata)
            #print(response)
           # print(response.text)
            #try:

            phonenum = response.json()['phoneNumber']
            print("New phone number: "+str(phonenum))
            break
        except:
            print("ERROR getting phone num allocated. Trying again")
    #except:
        #print("Error getting location")
        #print("Response headers: "+str(response.headers))
    return phonenum


def getmynumber(token):
    #gets perm ticket

    header1 = {
        'content-type':'application/json',
        'authorization':token,
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
   # jsondata = {
        #"service": "nextplus",
        #"ticketGrantingTicket":ticket
    #}
    while True:
        response = requests.get("https://ums.prd.gii.me/me?projection=inline", headers=header1)
        #print(response.text)
        #print(response.text)
        #print(response.headers)
        num = ""
        #try:
        #str("https://ums.prd.gii.me/users/")
        try:
            num = response.json()['primaryPersona']['tptns'][0]['phoneNumber']
            print("My number: "+str(num))
            break
        except:
            print("NO NUMBER ASSIGNED.")
            return "ERROR"
        
    #except:
        #print("Error getting location")
        #print("Response headers: "+str(response.headers))
    return str(str(num).strip().replace("+",""))


def recaptcha():
    key = "3fd94090a145df3bd4889a46ecfebbf6"
    #header1 = {
        #'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        #'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 13_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko)',
        #'Accept-Language':'en-ca',
        #'Accept-Encoding':'gzip, deflate, br',
        #'referer':'http://events.nextplus.me/recaptcha/humantn.html'
    #}
    
    #url = str("https://www.google.com/recaptcha/api2/anchor?ar=1&k=6Lf9nMEUAAAAAHAX2fJIJiQJkXp7IwjUiJsnrvWw&co=aHR0cDovL2V2ZW50cy5uZXh0cGx1cy5tZTo4MA..&hl=en&v=9qx0v7NiOAe_XnW_ULNZm9e3&size=normal&cb=37cgcvmhbo69")
   ## print("URL: "+str(url))
    #response = requests.get(url, headers=header1)
    #print(response)

    #captchatoken = response.text.split('recaptcha-token" value="')[1]
    #captchatoken = captchatoken.split('">')[0]
    #captchatoken = captchatoken.strip()
    #print("Captcha token for 2captcha: "+str(captchatoken))

    
    response = requests.get(str('http://2captcha.com/in.php?key='+str(key)+'&method=userrecaptcha&googlekey=6Lf9nMEUAAAAAHAX2fJIJiQJkXp7IwjUiJsnrvWw&pageurl=http://events.nextplus.me/recaptcha/humantn.html'))
    print(response.text)
    myid =str(response.text.split("|")[1])


    while True:
        response = requests.get(str('http://2captcha.com/res.php?key='+str(key)+'&action=get&id='+str(myid)+'&json=1'))
        if "READY" not in response.text:
            break
        
    captchatoken = response.json()['request']
    
    print("Captchatoken: "+str(captchatoken))
        
    return captchatoken



def getigmessages(token):

    header1 = {
        'content-type':'application/json',
        'authorization':token,
        'accept':'*/*',
        'appversion':'7.9.0.00396',
        'sku':'com.gogii.textplus',
        #'if-none-match':donotmatch,
        'accept-encoding':'gzip, deflate',
        'platform':'iOS',
        'accept-language':'en-US;q=1',
        'user-agent':'textPlus/7.9.0 (iPhone; iOS 13.7; Scale/2.00)',#'textPlus/7.9.0 (iPhone; iOS 13.7; Scale/2.00)',
        'network':'nextplus',
        'device':'iPhone8,1',
        'carrier':'Telus',
        'udid':mac
    }
   # jsondata = {
        #"service": "nextplus",
        #"ticketGrantingTicket":ticket
    #}

    response = requests.get("https://ums.prd.gii.me/me?projection=inline", headers=header1)
    #print(response.text)
    #print(response.text)
    #print(response.headers)
    jid = ""
    #try:
    #str("https://ums.prd.gii.me/users/")
    jid = response.json()['primaryPersona']['jid']
    #print("JID: "+str(jid))

    
    header1 = {
        'content-type':'application/json',
        'authorization':token,
        'accept':'*/*',
        'appversion':'7.9.0.00396',
        'sku':'com.gogii.textplus',
        #'if-none-match':donotmatch,
        'accept-encoding':'gzip, deflate',
        'platform':'iOS',
        'accept-language':'en-US;q=1',
        'user-agent':'textPlus/7.9.0 (iPhone; iOS 13.7; Scale/2.00)',#'textPlus/7.9.0 (iPhone; iOS 13.7; Scale/2.00)',
        'network':'nextplus',
        'device':'iPhone8,1',
        'carrier':'Telus',
        'udid':mac
    }
   # jsondata = {
        #"service": "nextplus",
        #"ticketGrantingTicket":ticket
    #}
    igmsg = "None"
    response = requests.get("https://mhs.prd.gii.me/messages/search/fetchByMessagePartyJidAndUpdatedGreaterThanEqual?jid="+str(jid)+"&since=2021-05-05T13%3A45%3A41.000-0700&projection=inline&size=500", headers=header1)
    #print(response.text)
    messages = response.json()["_embedded"]["messages"]
    #print(messages)
    igmsgs = []
    for message in messages:
        #print(message["body"])
        try:
            mymsg = message["body"].split('Message":"')[1].split('","')[0]
        except:
            print("Error getting message Printing normal body")
        mymsg = message["body"]
       #print(mymsg)
        try:
            igmsg = str(mymsg.split("F-")[1].split(" is")[0].strip()).replace(" ","")
            igmsgs.append(igmsg)
        except:
            try:
                igmsg = str(mymsg.split("Use ")[1].split(" to")[0].strip()).replace(" ","")
                igmsgs.append(igmsg)    
            except:
                print("No ig message here. Checking next")
    
    print("message: "+str(igmsgs))
    return igmsgs



def getphonenum():
    global user
    global passw
    usenewacc = False
    replaceacc = False
    if user == "":
        usenewacc = True
    while True:
        if usenewacc == True:
            file = open("textplusaccs.txt","r")
            allaccs = file.readlines()
            file.close()
            if len(allaccs) <= 1:
                return "out"
            myacc = str(allaccs[0]).replace("\n","").replace("\r","").strip()
            #print("TESTING: "+str(myacc))

            user = myacc.split(":")[0]
            passw = myacc.split(":")[1]

            
            #token = getticket(user,passw)
            #userpath = getpersonafornumber(token)
            oldacc = allaccs[0]
            allaccs.remove(allaccs[0])

            if replaceacc == True:
                file = open("textplusaccs.txt","w")
                file.writelines(allaccs)
                file.close()

                file = open("oldtextplusaccs.txt","a")
                file.write(str(oldacc))
                file.close()
                
            usenewacc = False
        
        try:
            token = getticket(user,passw)
            userpath = getpersonafornumber(token)
            mynum = getmynumber(token)
            status = ""
            if mynum != "ERROR":
                print("Got valid phone number. Returning")
                file = open("usedphone.txt","r")
                usedphones = file.readlines()
                file.close()

                if mynum.strip() not in str(usedphones):
                    print("Phone number is original")
                    file = open("usedphone.txt","a")
                    file.write(str(mynum.strip()+"\n"))
                    file.close()
                    break
                else:
                    print("Phone number is not original. Assigning new")
                    
                    for _ in range(5):
                        token = getticket(user,passw)
                        userpath = getpersonafornumber(token)
                        status = changenumber(userpath, token)
                        if status != "ERROR":
                            break
                        
                    
                    if status != "ERROR":
                        print("Changed number. Getting current number")
                        mynum = getmynumber(token)
                        file = open("usedphone.txt","a")
                        file.write(str(mynum.strip()+"\n"))
                        file.close()
                        break
                    else:
                        print("Couldn't get number on this account. Using new account")
                        time.sleep(10)
                        usenewacc = True
                        replaceacc = True
        
            else:
                for _ in range(5):
                    token = getticket(user,passw)
                    userpath = getpersonafornumber(token)
                    status = changenumber(userpath, token)
                    if status != "ERROR":
                        break
                
                if status != "ERROR":
                    print("Changed number. Getting current number")
                    file = open("usedphone.txt","a")
                    file.write(str(mynum.strip()+"\n"))
                    file.close()
                    mynum = getmynumber(token)
                    break
                else:
                    print("Couldn't get number on this account. Using new account")
                    time.sleep(10)
                    usenewacc = True
                    replaceacc = True
        except:
            print("Error getting token. Getting new tp account")
            usenewacc = True
            replaceacc = True
                        
    
    return mynum


def getallmsgs():
    global user
    global passw
    token = getticket(user,passw)
    userpath = getpersonafornumber(token)
    msgs = getigmessages(token)
        
    return msgs

def getsmscode(allmsgs):
    global user
    global passw
    token = getticket(user,passw)
    userpath = getpersonafornumber(token)
    code = ""
    for i in range(200):
        msgs = getigmessages(token)
        for msg in msgs:
            if msg.strip().replace("\n","").replace("\r","") not in str(allmsgs):
                code = msg
                return code
            
        time.sleep(1)
    return "none"

###################################
#SELENIUM FUNCTIONS

def randkeys(element, keys):
    try:
        for i in keys:
            time.sleep(random.uniform(0.09, 0.3))
            driver.find_element_by_xpath(element).send_keys(i)
    except:
        print("Error typing")
        
        
def passgenerator():
    
    passw = namegenerator().replace(" ","")
        
    randprefix = random.randint(0,10)
    if randprefix >= 5:
        print("Adding prefix to pass")
        passw = str("pass"+passw)

    randsuffix = random.randint(0,10)
    if randsuffix >= 5:
        print("Adding suffix to pass")
        passw = str(passw+str(random.randint(0,999)))

    randsuffix = random.randint(0,10)
    if randsuffix >= 5:
        print("Adding suffix2 to pass")
        randsuffixex = random.randint(0,10)
        if randsuffixex >= 2:
            passw = str(passw+"$")
        if randsuffixex >= 5:
            passw = str(passw+"!")
        if randsuffixex >= 7:
            passw = str(passw+"&")

    return passw

                
def namegenerator():
    gender = random.randint(0,10)
    if gender >= 5:
        genderfile = "names/malegen.txt"
    else:
        genderfile = "names/femalegen.txt"

        
    file = open(genderfile, "r")
    firstnames = file.readlines()
    file.close()

    file = open("names/lastnames.txt", "r")
    lastnames = file.readlines()
    file.close()
    
    fullname = str(firstnames[random.randint(0, (len(firstnames) - 1))].strip().replace("\n","").replace("\r","")+" "+lastnames[random.randint(0, (len(lastnames) - 1))].strip().replace("\n","").replace("\r",""))
    print("Generated name: "+str(fullname))

    return fullname


def usernamegenerator():
    username = namegenerator()
    username = str(username.replace(" ","")+str(random.randint(99,9999)))
    
    return username

            
def initdriver(proxy):
    try:
        global driver
        chrome_options = webdriver.ChromeOptions() 
        chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        #chrome_options.add_argument('--user-data-dir=C:\\Users\\exoti\\AppData\\Local\\Google\\Chrome\\User Data\\')
        #chrome_options.add_argument('--profile-directory=Default')
        #chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument('--proxy-server='+str(proxy))
        #service = Service('chromedriver.exe')
        #service.creationflags = CREATE_NO_WINDOW
        driver = webdriver.Chrome(options=chrome_options)
        driver.delete_all_cookies()    
        #driver.set_window_position(0, -2000, windowHandle='current')
        time.sleep(0.5)
        pyautogui.click(702, 10)
    except Exception as EE:
        print("Error opening: "+str(EE))


def waitforelement(element):
    global driver
    for i in range(30):
        time.sleep(1)
        try:
            if driver.find_element_by_xpath(element) != None:
                return driver.find_element_by_xpath(element)
        except Exception as EE:
            print("Looking for element"+str(EE))

    return None

def waitforclick(element):
    global driver
    obj = waitforelement(element)
    if obj != None:
        myx = 0
        myy = 0
        w,h = obj.size['width'],obj.size['height']
        print(str(w)+str(h))
        randxmax = (w/2) - 5
        randymax = (h/2) - 5

        myrand = random.randint(0,10)
        myrand2 = random.randint(0,10)
        try:
            if myrand >= 5:
                myx += random.randint(0,int(randxmax))
            else:
                myx += random.randint(0,int(randxmax))
            if myrand2 >= 5:
                myy += random.randint(0,int(randymax))
            else:
                myy += random.randint(0,int(randymax))
        except:
            myx = 0
            myy = 0

        try:
            ed = ActionChains(driver)
            ed.move_to_element(obj).move_by_offset(myx, myy).click().perform()
        except:
            print("Error clicking with offset. Clicking normally")
            try:
                obj.click()
            except:
                print("Error clicking normally")

def createig(proxy):
    number = getphonenum()
    for bigloopi in range(2):
        try:
            initdriver(proxy)  
            global driver
            global user
            global passw
            file = open("textplusaccs.txt","r")
            numaccs = file.readlines()
            file.close()

            #phoneacc = numaccs[0].replace("\n","").replace("\r","")
            #user = phoneacc.split(":")[0].strip()
            #passw = phoneacc.split(":")[1].strip()
            #print(str(user)+str(passw))
            #phonenum = getphonenum()
             
            #goes to FB
            driver.get('https://www.instagram.com/accounts/emailsignup/')
            time.sleep(1)
            #waitforclick("//button[contains(text(),'Accept All')]")
            print("DONE LOADING")

            #CREATE ACCOUNT
            #waitforclick('//*[@id="u_0_2_4Y"]')    

            #MOBILE NUM
            waitforclick('//*[@id="react-root"]/section/main/div/div/div[1]/div/form/div[3]/div/label/input')
            if "out" in str(number):
                return
            randkeys('//*[@id="react-root"]/section/main/div/div/div[1]/div/form/div[3]/div/label/input',str(number))
            

            time.sleep(random.uniform(0.1, 1))
            #FULL NAME
            waitforclick('//*[@id="react-root"]/section/main/div/div/div[1]/div/form/div[4]/div/label/input')
            time.sleep(random.uniform(0.1, 1))
            fullname = namegenerator()
            randkeys('//*[@id="react-root"]/section/main/div/div/div[1]/div/form/div[4]/div/label/input',str(fullname))

            
            #USERNAME
            waitforclick('//*[@id="react-root"]/section/main/div/div/div[1]/div/form/div[5]/div/label/input')
            time.sleep(random.uniform(0.1, 1))
            username = usernamegenerator()
            randkeys('//*[@id="react-root"]/section/main/div/div/div[1]/div/form/div[5]/div/label/input',str(username))

            #NEW PASSWORD
            waitforclick('//*[@id="react-root"]/section/main/div/div/div[1]/div/form/div[6]/div/label/input')
            time.sleep(random.uniform(0.1, 1))
            password = passgenerator()
            randkeys('//*[@id="react-root"]/section/main/div/div/div[1]/div/form/div[6]/div/label/input',str(password))
            
            
            allmsgs = getallmsgs()

            #SIGN UP
            waitforclick('//*[@id="react-root"]/section/main/div/div/div[1]/div/form/div[7]/div/button')

            
            #BIRTHDAY
            time.sleep(random.uniform(0.1, 1))
            #MONTH
            waitforclick('//*[@id="react-root"]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[1]/select')
            time.sleep(random.uniform(1.0,2.0))
            waitforclick('//*[@id="react-root"]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[1]/select/option['+str(random.randint(1, 12))+']')
            time.sleep(random.uniform(0.1, 0.3))             
            #DAY
            waitforclick('//*[@id="react-root"]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[2]/select')
            time.sleep(random.uniform(1.0,2.0))
            waitforclick('//*[@id="react-root"]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[2]/select/option['+str(random.randint(1,28))+']')
            time.sleep(random.uniform(0.1, 0.3))
            #YEAR
            
            waitforclick('//*[@id="react-root"]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[3]/select')
            time.sleep(random.uniform(1.0,2.0))
            waitforclick('//*[@id="react-root"]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[3]/select/option['+str(random.randint(18, 65))+']')
            time.sleep(random.uniform(0.1, 0.3))
            #SUBMIT
            waitforclick('//*[@id="react-root"]/section/main/div/div/div[1]/div/div[6]/button')
            time.sleep(random.uniform(1.0,2.0))
            time.sleep(random.uniform(0.1, 1))
            #CONFIRMATION CODE:
            waitforclick('//*[@id="react-root"]/section/main/div/div/div[1]/div/div/div/form/div[1]/div/label/input')
            smscode = getsmscode(allmsgs)
            if smscode == "none":
                print("Error getting code. Returning")
                return
            randkeys('//*[@id="react-root"]/section/main/div/div/div[1]/div/div/div/form/div[1]/div/label/input',str(smscode))
            

            time.sleep(random.uniform(0.1, 1))
            #CONFIRM
            waitforclick('//*[@id="react-root"]/section/main/div/div/div[1]/div/div/div/form/div[2]/button')
            
            breakl = False
            for i in range(20):
                time.sleep(1)
                try:
                    if "challenge" in driver.current_url:
                        print("GOT CHALLENGE ): Breaking")
                        return
                except:
                    print("Looking for url challenge")

            

            print("SUCCESSFUL ACCOUNT! ADDING TO LIST OF MADE ACCS")
            file = open("igaccountsmade.txt","a")
            file.write(str(username+":"+password+"\n"))
            file.close()
            try:
                driver.close()
                driver.quit()
            except:
                print("Error closing driver")
        except Exception as Bige:
            print("Error creating acc. Trying again: "+str(Bige))
            try:
                driver.close()
                driver.quit()
            except:
                print("Error closing driver")

file = open("igproxies.txt","r")
proxies = file.readlines()
file.close()
proxy = proxies[0]
while True:
    file = open("textplusaccs.txt","r")
    alltpaccs = file.readlines()
    file.close()
    
    if len(alltpaccs) > 1:
        createig(proxy)
        try:
            driver.close()
            driver.quit()
        except:
            print("Error closing driver")
        
    time.sleep(1)
