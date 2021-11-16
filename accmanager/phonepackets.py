import requests
import sys
import os
import time
import random
import math
import json
import hashlib
import pyautogui
#header1 = {
#    'Host':'xmpp.prd.gii.me:443',
#    'Sec-WebSocket-Protocol':'xmpp',
#    'Sec-WebSocket-Key':'I/2Slym3PZm3ObNznO3dBQ==',
#    'Sec-WebSocket-Version':'13',
#    'Upgrade':'websocket',
#    'Origin':'https://xmpp.prd.gii.me',
#    'Authorization':'Basic KG51bGwpOihudWxsKQ==',
#    'Connection':'Upgrade'
#}

#response = requests.get('https://xmpp.prd.gii.me/', headers=header1)


#print(response)
#print(response.text)

mac = str(str(random.randint(0,9))+'BD87DF'+str(random.randint(0,9))+'-'+str(random.randint(1111,9999))+'-'+str(random.randint(1111,9999))+'-2D2G-7A0FA9E0BE29')

#user ="Hewef"+str(random.randint(1111,9999))+"onlololol"
#passw = str("Jim"+str(random.randint(1111,9999))+"fl$$!!$!$!$2323")

user = "xnfnlll2-1"
passw = "bjoyyejbhj7$!!"

print("mac: "+mac)
#1

def getticket(user, passw):
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
    
    print(response)
    print(response.json())
    print(response.text)

    ticket = response.json()['ticket']
    print("Temp ticket: "+str(ticket))



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
    
    
    print(response)
    print(response.json())

    ticket = "CASST "+str(response.json()['ticket'])
    print("Perm ticket: "+str(ticket))

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
    
    print("User path: "+str(path))
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
    print(response.text)
    #print(response.text)
    #print(response.headers)
    path = ""
    #try:
    #str("https://ums.prd.gii.me/users/")
    path = response.json()['primaryPersona']['user']['id']
    print("User path: "+str(path))
    #except:
        #print("Error getting location")
        #print("Response headers: "+str(response.headers))
    return path



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

    response = requests.get("https://ums.prd.gii.me/me?projection=inline", headers=header1)
    print(response.text)
    #print(response.text)
    #print(response.headers)
    num = ""
    #try:
    #str("https://ums.prd.gii.me/users/")
    try:
        num = response.json()['primaryPersona']['tptns'][0]['phoneNumber']
        print("My number: "+str(num))
    except:
        print("NO NUMBER ASSIGNED")
        

    #except:
        #print("Error getting location")
        #print("Response headers: "+str(response.headers))
    return str(str(num).strip().replace("+",""))


def recaptcha():
    
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

    
    response = requests.get('http://2captcha.com/in.php?key=3fd94090a145df3bd4889a46ecfebbf6&method=userrecaptcha&googlekey=6Lf9nMEUAAAAAHAX2fJIJiQJkXp7IwjUiJsnrvWw&pageurl=http://events.nextplus.me/recaptcha/humantn.html')
    print(response.text)
    myid =str(response.text.split("|")[1])


    while True:
        response = requests.get(str('http://2captcha.com/res.php?key=3fd94090a145df3bd4889a46ecfebbf6&action=get&id='+str(myid)+'&json=1'))
        if "READY" not in response.text:
            break
        
    captchatoken = response.json()['request']
    
    print("Captchatoken: "+str(captchatoken))
        
    return captchatoken


def getnumbers(token):
    
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

    response = requests.get("https://ums.prd.gii.me/tptnLocales?country=CA", headers=header1)
    print(response.text)
    

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
    print("JID: "+str(jid))

    
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
        print(mymsg)
        try:
            igmsg = str(mymsg.split("<#>")[1].split(" is")[0].strip()).replace(" ","")
            igmsgs.append(igmsg)
        except:
            print("No ig message here. Checking next")
    
    print("message: "+str(igmsgs))
    return igmsgs

def changenumber(profile, token):    
    while True:
        try:
            f = open("localeid.txt","r")
            alllocals = f.readlines()
            f.close()

            local = str(alllocals[random.randint(0, 40)].strip().replace("\n","").replace("\r",""))
            print(local)
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
            print("URL: "+str(url))
            response = requests.post(url, headers=header1, json=jsondata)
            print(response)
            print(response.text)
            #try:

            phonenum = response.json()['phoneNumber']
            print("New phone number: "+str(phonenum))
            break
        except:
            print("ERROR getting phone num allocated. Trying again in 2 seconds")
            time.sleep(2)
    #except:
        #print("Error getting location")
        #print("Response headers: "+str(response.headers))
    return phonenum


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


def xregandroid(username, udid):
    
    platformos = "7.1.2"
    appversion = "7.7.4"
    appname = "textplus"
   
    xregtokenbefore = str(username)+str(platformos)+str(appversion)+str(udid)+str(appname)+str("rZdC!UX+2VJu+p*A-ENZpmbyFJ+SYK52$gkVWWWzwxIv7ks=rJITpKHqJu5HQkF8F") 
    #print("BEFORE X REG: "+str(xregtokenbefore))
    myhash = hashlib.sha512( str( xregtokenbefore ).encode("utf-8") ).hexdigest()
    print("xregtoken: "+str(myhash))
    return myhash

def register(gsntoken):    
    
    try:
        username = gentpuser()
        password = gentppass()
        
        udid = str("8"+str(random.randint(111111, 999999))+"g"+str(random.randint(0,9))+"a4a8d8a")

        #udid = "c0575264c704f9c6"
        
        xregtoken = xregandroid(username, udid)
        
        header1 = {
            "x-gsn-token":gsntoken,
            "x-reg-token":xregtoken,
            "platform":"android",
            "market":"GooglePlay",
            "appversion":"7.7.4.01197",
            "udid":udid,
            "device":"ASUS_Z01QD",
            "sku":"com.gogii.textplus",
            "network":"nextplus",
            "carrier":"Bell",
            "content-type":"application/json; charset=utf-8",
            "content-length":"374",
            "accept-encoding":"gzip",
            "user-agent":"okhttp/3.14.9",
        }
        jsondata = {
            
            "avatarUrl": "",
            "country": "CA",
            "device": {
                "appName": "textplus",
                "appVersion": "7.7.4",
                "deviceUDID": udid,
                "model": "ASUS_Z01QD",
                "platform": "google",
                "platformOSVersion": "7.1.2",
                "pushEnabled": True,
                "pushTokenType": "ANDROID_GCM",
                "pushType": 2
            },
            "locale": "en_US",
            "network": "nextplus",
            "optin": 1,
            "password": password,
            "tos": 1,
            "username":username 
        }
        
        url = str("https://ums.prd.gii.me/registration/mobile")
        
        print("My headers: "+str(header1))
        print("My Json data: "+str(jsondata))

        #ff808181791d08160179340df2813631 # one used
        print("URL: "+str(url))
        proxies =   {
            'https' : 'http://country-ca:ead2795d-a80d-4ea0-b686-c08f23894210@51.161.115.64:80',
            'http' : 'http://country-ca:ead2795d-a80d-4ea0-b686-c08f23894210@51.161.115.64:80'
                    } 
        response = requests.post(url, headers=header1, json=jsondata, proxies=proxies)
        print(response)
        if "201" in str(response):
            print("Account made successfully: "+str(username)+":"+str(password))
            username = str(username+"-1")
            return username,password
        else:
            print("Bad response making account")
            return None,None
    except Exception as eee:
        print("ERROR making account: "+ str(eee))
        return None,None
    #except:
        #print("Error getting location")
        #print("Response headers: "+str(response.headers))
    



    

user = "lyvhuep9-1"
passw = "bqyefayakb9$!!"


#username, password = register()
#print("Got account: "+str(username)+":"+str(password))
#print(xregandroid("sdlkfjkfjklsdfklj","8618241f4a4a8d8a"))
token = getticket(user,passw)
userpath = getpersonafornumber(token)
#getnumbers(token)

#getuser(token)

#changenumber(userpath, token)
#time.sleep(2)
getmynumber(token)
getigmessages(token)

#info = getnamegen()
