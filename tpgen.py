import requests
import sys
import os
import time
import random
import math
import json
import hashlib
import pyautogui



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
    




while True:
    try:
        response = requests.get("http://accounthaven.net/gsntokens.txt", headers={"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"}, verify=False, timeout=5)
        if "none" not in response.text:
            gsntoken = response.text
            gsntoken = str(gsntoken.strip().replace("\n","").replace("\r",""))
            
            username, password = register(gsntoken)

            if username != None:
                file= open("textplusaccs.txt", "a")
                file.write(str(username+":"+password+"\n"))
                file.close()                
            requests.get("http://accounthaven.net/addgsntoken.php?token=none", headers={"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"}, verify=False, timeout=5)
            print("Reset token")            
    except Exception as EE:
        print("Error: "+str(EE))
    


