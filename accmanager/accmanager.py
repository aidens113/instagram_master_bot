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
import selenium
import urllib.request
import urllib
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time,string,zipfile,os
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from subprocess import CREATE_NO_WINDOW
import multiprocessing
from selenium import webdriver
def randkeys(element, keys, driver):
    for myi in keys:
        element.send_keys(myi)
        time.sleep(random.uniform(0.05, 0.25))

def press_key(key, driver):
    actions = ActionChains(driver)
    actions.send_keys(key)
    actions.perform()

def login(user, passw, driver):
    try:

        for _ in range(10):
            try:
                driver.get("https://www.instagram.com/accounts/login/")
                break
            except:
                print("Error getting connection, trying again")
        time.sleep(2)

        for _ in range(5):
            try:
                driver.find_element_by_xpath('/html/body/div[2]/div/div/button[1]').click()        
            except:
                print("Error")

        while True:
            try:
                if driver.find_element_by_xpath('//*[@id="loginForm"]/div[1]/div[3]/div/label/input') != None:
                    randkeys(driver.find_element_by_xpath('//*[@id="loginForm"]/div[1]/div[3]/div/label/input'),user, driver)            
                    break
            except Exception as EE:
                print("Looking for user: "+str(EE))

        while True:
            try:
                if driver.find_element_by_xpath('//*[@id="loginForm"]/div[1]/div[4]/div/label/input') != None:
                    randkeys(driver.find_element_by_xpath('//*[@id="loginForm"]/div[1]/div[4]/div/label/input'),passw , driver)            
                    break
            except:
                print("Looking for pass")

        while True:
            try:
                
                if driver.find_element_by_xpath('//*[@id="loginForm"]/div[1]/div[6]/button') != None:
                    try:
                        driver.find_element_by_xpath('//*[@id="loginForm"]/div[1]/div[6]/button').click()            
                    except:
                        print("Error clicking submit")
                    break
            except Exception as EE:
                print("Looking for submit button: "+str(EE))



        while True:
            try:
                if driver.current_url == "https://www.instagram.com/accounts/onetap/?next=%2F":
                    break
                try:
                    if driver.find_element_by_xpath("/html/body/div[1]/section/main/div[1]/div/div/div/form/div[2]/p") != None:
                        print("Found error")
                        return False  
                except:
                    print("No error msg")
                if "challenge" in driver.current_url:
                    print("Got challenge")
                    file = open("mainaccs.txt", "r")
                    allaccs = file.readlines()
                    file.close()

                    allaccs.remove(allaccs[0])

                    file = open("mainaccs.txt", "w")
                    file.writelines(allaccs)
                    file.close()
                    
                    return False
            except:
                print("Waiting for login")

            time.sleep(1)

    except Exception as EE:
        print("Error: "+str(EE))




def changeprofile(user):
    driver.get(str("https://www.instagram.com/"+str(user)))
    
    

def makepost(caption, driver):

    for i in range(100):
        try:
            driver.find_element_by_xpath('//*[@id="react-root"]/section/nav[2]/div/div/div[2]/div/div/div[3]').click()
            break
        except:
            print('Looking for post button')
        time.sleep(2)

            
    time.sleep(2)
    pyautogui.write(str(str(os.getcwd()).replace("/","\\")+"\\mainpost.png"))
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    

    for i in range(100):
        try:
            driver.find_element_by_xpath('//*[@id="react-root"]/section/div[1]/header/div/div[2]/button').click()
            break
        except:
            print("Looking for next button")
        time.sleep(2)


    for i in range(100):
        try:
            driver.find_element_by_xpath('//*[@id="react-root"]/section/div[2]/section[1]/div[1]/textarea').click()
            break
        except:
            print("Looking for caption area")
        time.sleep(2)

    time.sleep(2)
    for line in caption:
        try:
            newlines = 0
            randkeys(driver.find_element_by_xpath('//*[@id="react-root"]/section/div[2]/section[1]/div[1]/textarea'), line, driver)
            if "@" in line:
                newlines = 3
                time.sleep(1)
            else:
                newlines = 1
            for ii in range(newlines):
                time.sleep(1)
                driver.find_element_by_xpath('//*[@id="react-root"]/section/div[2]/section[1]/div[1]/textarea').send_keys(Keys.ENTER)
                time.sleep(1)
        except:
            print('error writing line')

    time.sleep(2)
    for i in range(100):
        try:
            driver.find_element_by_xpath('//*[@id="react-root"]/section/div[1]/header/div/div[2]/button').click()
            break
        except:
            print("Looking for share button")
        time.sleep(2)

    time.sleep(10)
    
def generatecaption(category, myname, credit):

    randchoice = random.randint(0,10)

    part1 = ""
    
    #if randchoice >= 4:
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    current_time = str(current_time)

    #if int(str(current_time.split(":")[0])) > 12:
        #part1 = "gn"
    #else:
        #part1 = "gm"
        
    #else:
    filename = str("category\\"+category+".txt")
    file = open(filename, "r")
    allcap = file.readlines()
    file.close()

    part1 = allcap[random.randint(0, int(len(allcap) - 1))].strip().replace("\n","")

    for i in range(10):
        try:
            part1t = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[3]/div[1]/div/div[1]/div/span/span[1]').text.strip().replace("\n","")
            if "#" in part1t or "@" in part1t or "explain" in part1t or "Explain" in part1t:
                break
            else:
                part1 = part1t
                break
            print("Found caption part 1: "+str(capig))
        except:
            print("Looking for caption")
    
    
        
    fullcaption = []
    fullcaption.append(part1)
    fullcaption.append(str("Credit: @"+str(credit)))
    fullcaption.append(str("Follow @"+str(myname)))
    fullcaption.append(str("Follow @"+str(myname)))
    fullcaption.append(str("."))
    fullcaption.append(str("."))
    fullcaption.append(str("."))
    fullcaption.append(str("."))
    fullcaption.append(str("."))
    fullcaption.append(str("."))
    fullcaption.append(str("."))
    fullcaption.append(str("."))
    fullcaption.append(str("Tags:"))

    filename = str("hashtags\\"+category+".txt")
    print("Reading "+str(filename))
    file = open(filename, "r")
    alltags = file.readlines()
    file.close()

    thetags = ""
    for i in range(0,random.randint(14, 27)):
        thetags = str(thetags+" #"+str(alltags[i]).strip().replace("\n",""))

    fullcaption.append(str(thetags))
    print("Generated caption: "+str(fullcaption))
    return fullcaption
    
def repost(category, user, driver):


    for myii in range(10):
        driver.get("https://www.instagram.com/explore/tags/"+str(category))
        time.sleep(2)
        myrow = random.randint(1, 3)
        mycol = random.randint(1, 3)

        for i in range(100):
            try:
                driver.find_element_by_xpath('//*[@id="react-root"]/section/div[3]/div/p[2]/div/button/span').click()
            except:
                print("Looking for x button")

            try:
                driver.find_element_by_xpath('//*[@id="react-root"]/section/div[2]/div/div[1]/button').click()
            except:
                print("Looking for second x button")
                
            try:
                if driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[2]/div/div/div[1]') != None:
                    break
            except:
                print("Looking for image")
            try:                                 
                if driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div['+str(myrow)+']/div['+str(mycol)+']/a') != None:
                    print("Found post, trying to click")
                    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div['+str(myrow)+']/div['+str(mycol)+']/a').click()
                    
            except Exception as rr:
                print("Finding post on col: "+str(mycol)+" and row: "+str(myrow))
                print("Error finding it: "+str(rr))
            time.sleep(2)

        breakl = False
        time.sleep(3)
        for i in range(100):
            try:
                if driver.find_element_by_class_name('fXIG0') != None:
                    breakl = True
                    print("Found play button. Restarting")
                    break
            except:
                print("Looking for play button")
            
                        
            try:                                    
                img = driver.find_element_by_class_name('FFVAD')
                break
            except:
                print("Looking for image src")
            time.sleep(2)

        time.sleep(3)
        if breakl == False:
            src = img.get_attribute('src')
            urllib.request.urlretrieve(src, "mainpost.png")
            break

    #driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[3]/div[1]/div/div[1]/div/span/span[2]/button').click()
    time.sleep(2)

    #caption = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[3]/div[1]/div/div[1]/div/span').text
    credit = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[3]/div[1]/div/div[1]/div/a').text

    caption = generatecaption(category,str(user),str(credit).strip())

    print("Caption: "+str(caption))
    print("Credit: "+str(credit))

    print("Posing")
    makepost(caption, driver)    

def genuser(category):
    try:


        username = ""
        file = open(str("username/"+str(category)+".txt"),"r")
        usernames = file.readlines()
        file.close()
        file = open("username/last.txt","r")
        users2 = file.readlines()
        file.close()

        user1 = str(usernames[random.randint(0,int(len(usernames) - 1))]).strip().replace("\n","").replace("\r","")
        user2 = str(users2[random.randint(0,int(len(usernames) - 1))]).strip().replace("\n","").replace("\r","")

        myrand = random.randint(0,10)
        if myrand >= 2:
            username = str(str(user1)+str("_")+str(user2))
        if myrand < 2:
            username = str(str(user1)+str(".")+str(user2))

        username = str(username+str(random.randint(0,99)))           
        
        return username
            
        print("Changing username")
    except Exception as ER:
        print("Error changing user: "+str(ER))


def changeprofilepic(driver, link, category):
    try:
        for myii in range(10):
            driver.get("https://www.instagram.com/explore/tags/"+str(category))
            time.sleep(2)
            myrow = random.randint(1, 3)
            mycol = random.randint(1, 3)

            for i in range(100):
                try:
                    driver.find_element_by_xpath('//*[@id="react-root"]/section/div[3]/div/p[2]/div/button/span').click()
                except:
                    print("Looking for x button")

                try:
                    driver.find_element_by_xpath('//*[@id="react-root"]/section/div[2]/div/div[1]/button').click()
                except:
                    print("Looking for second x button")
                    
                try:
                    if driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[2]/div/div/div[1]') != None:
                        break
                except:
                    print("Looking for image")
                try:                                 
                    if driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div['+str(myrow)+']/div['+str(mycol)+']/a') != None:
                        print("Found post, trying to click")
                        driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div['+str(myrow)+']/div['+str(mycol)+']/a').click()
                        
                except Exception as rr:
                    print("Finding post on col: "+str(mycol)+" and row: "+str(myrow))
                    print("Error finding it: "+str(rr))
                time.sleep(2)

            breakl = False
            time.sleep(3)
            for i in range(100):
                try:
                    if driver.find_element_by_class_name('fXIG0') != None:
                        breakl = True
                        print("Found play button. Restarting")
                        break
                except:
                    print("Looking for play button")
                
                            
                try:                                    
                    img = driver.find_element_by_class_name('FFVAD')
                    break
                except:
                    print("Looking for image src")
                time.sleep(2)

            time.sleep(3)
            if breakl == False:
                src = img.get_attribute('src')
                urllib.request.urlretrieve(src, "profilepic.png")
                break


        driver.get("https://instagram.com/accounts/edit")
        
        while True:
            try:
                if driver.find_element_by_class_name('tb_sK') != None:
                    #driver.find_element_by_xpath("//*[text()='Change Profile Photo']").click()
                    break
            except:
                print("Looking for profile pic button")
            time.sleep(0.5)

        #time.sleep(1)
        #drag_and_drop_file(driver.find_element_by_xpath("//*[text()='Change Profile Photo']"), str(str(os.getcwd()).replace("/","\\")+"\\"+link), driver)

        try:
            time.sleep(2)
            field = driver.find_element_by_class_name('tb_sK')
            driver.execute_script("arguments[0].style.display = 'block';", field)
            field.send_keys(str(str(os.getcwd()).replace("/","\\")+"\\"+link))
            time.sleep(0.5)
            field.submit()
        except Exception as Err:
            print("Error with submitting image: "+str(Err))
                
        #pyautogui.write(str(str(os.getcwd()).replace("/","\\")+"\\"+link))
        #time.sleep(0.3)
        #pyautogui.press('enter')
        time.sleep(3)    

        driver.find_element_by_xpath('//*[@id="react-root"]/section/div[1]/header/div/div[2]/button').click()
        time.sleep(1)
        
        os.remove(link)

        file = open("igaccountsmade.txt", "r")
        allaccs = file.readlines()
        file.close()

        acc = allaccs[0].strip().replace("\r","").replace("\n","")
        acc = str(acc+":yes\n")

        allaccs.remove(allaccs[0])
        allaccs.append(acc)
        
        file = open("igaccountsmade.txt", "w")
        file.writelines(allaccs)
        file.close()
    except Exception as EE:
        print("Error changing profile pic: "+str(EE))
        return


def changeuser(driver, category):
    driver.get("https://instagram.com/accounts/edit/")
    time.sleep(1)
    username = genuser(category)
    while True:
        try:
            if driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/form/div[2]/div/div/input') != None:
                driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/form/div[2]/div/div/input').click()
                time.sleep(random.uniform(0.1, 0.6))
                for myii in range(random.randint(25, 31)):
                    press_key(Keys.BACKSPACE, driver)
                    time.sleep(random.uniform(0.001, 0.01))
                time.sleep(random.uniform(0.1, 0.6))
                randkeys(driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/form/div[2]/div/div/input'),username ,driver)
                break
        except Exception as EE:
            print("Looking for username: "+EE)

    #while True:
        #try:
        #    if driver.find_element_by_class_name('storiesSpriteX__outline__44 u-__7') != None:
        #        driver.find_element_by_class_name('storiesSpriteX__outline__44 u-__7').click()
        #except:
        #    print("Error clicking submit")
        #
        #try:
        #    if driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/form/div[10]/div/div/button') != None:
        #        driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/form/div[10]/div/div/button').click()
        #        break
        #except:
        #    print("Error clicking submit")
    try:
        driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/form/div[2]/div/div/input').submit()
    except:
        print("Error submitting form")
    time.sleep(2)
    return username

def create_proxyauth_extension(proxy_host, proxy_port,proxy_username, proxy_password,
                               scheme='http', plugin_path=None):
    """Proxy Auth Extension
    args:
        proxy_host (str): domain or ip address, ie proxy.domain.com
        proxy_port (int): port
        proxy_username (str): auth username
        proxy_password (str): auth password
    kwargs:
        scheme (str): proxy scheme, default http
        plugin_path (str): absolute path of the extension

    return str -> plugin_path
    """
    if plugin_path is None:
        file='./chrome_proxy_helper'
        if not os.path.exists(file):
            os.mkdir(file)
        plugin_path = file+'/%s_%s@%s_%s.zip'%(proxy_username,proxy_password,proxy_host,proxy_port)

    manifest_json = """
    {
        "version": "1.0.0",
        "manifest_version": 2,
        "name": "Chrome Proxy",
        "permissions": [
            "proxy",
            "tabs",
            "unlimitedStorage",
            "storage",
            "<all_urls>",
            "webRequest",
            "webRequestBlocking"
        ],
        "background": {
            "scripts": ["background.js"]
        },
        "minimum_chrome_version":"22.0.0"
    }
    """
    background_js = string.Template(
    """
    var config = {
            mode: "fixed_servers",
            rules: {
              singleProxy: {
                scheme: "${scheme}",
                host: "${host}",
                port: parseInt(${port})
              },
              bypassList: ["foobar.com"]
            }
          };

    chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

    function callbackFn(details) {
        return {
            authCredentials: {
                username: "${username}",
                password: "${password}"
            }
        };
    }

    chrome.webRequest.onAuthRequired.addListener(
                callbackFn,
                {urls: ["<all_urls>"]},
                ['blocking']
    );
    """
    ).substitute(
        host=proxy_host,
        port=proxy_port,
        username=proxy_username,
        password=proxy_password,
        scheme=scheme,
    )
    with zipfile.ZipFile(plugin_path, 'w') as zp:
        zp.writestr("manifest.json", manifest_json)
        zp.writestr("background.js", background_js)

    return plugin_path




def initdriver(proxy):
    chrome_options = webdriver.ChromeOptions()
    mobile_emulation = {

        "deviceMetrics": { "width": 360, "height": 640, "pixelRatio": 3.0 },

    "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19" }
    
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')

    #chrome_options.add_argument(str('--profile-directory=Default'))
    #chrome_options.add_argument("--start-maximized")
    #chrome_options.add_argument(str('--proxy-server=http://'+str(proxy)))
    proxyauth_plugin_path = create_proxyauth_extension(
    proxy_host=str(str(proxy.split(":")[0]).strip().replace("\n","")), 
    proxy_port=str(str(proxy.split(":")[1]).strip().replace("\n","")),#80,
    proxy_username=str(str(proxy.split(":")[2]).strip().replace("\n","")),#"country-ca",
    proxy_password=str(str(proxy.split(":")[3]).strip().replace("\n","")),
    scheme='http'
    )
    chrome_options.add_extension(proxyauth_plugin_path)
    #chrome_options.add_argument("--headless")   
    driver = webdriver.Chrome(executable_path='chromedriver.exe',options=chrome_options)
    
    driver.delete_all_cookies()
    return driver

    
file = open("mainaccs.txt", "r")
accounts = file.readlines()
file.close()

while True:
    categories = ['meme', 'travel', 'luxury', 'health']
    allproxies = ['listofproxieshere']
    thist = 0
    for acc in accounts:
        driver = initdriver(allproxies[thist])
        thist += 1
        if thist >= len(allproxies):
            thist = 0
            
        user = acc.split(":")[0]
        passw = acc.split(":")[1]

        if login(user, passw, driver) != False:
            
            try:
                category = acc.split(":")[2].strip().replace("\n","").replace("\r","")
                theuser = user
            except:
                print("no category stored. Initiating account")
                category = categories[random.randint(0,int(len(categories) - 1))]

                file = open("mainaccs.txt", "r")
                accstowrite = file.readlines()
                file.close()

                accstowrite.remove(acc)
                newuser = changeuser(driver,category)
                newuser = str(newuser+":"+acc.split(":")[1].strip().replace("\n","").replace("\r",""))
                
                accstowrite.append(str(newuser.strip().replace("\n","").replace("\r","")+":"+category+"\n"))
                
                file = open("mainaccs.txt", "w")
                file.writelines(accstowrite)
                file.close()

                changeprofilepic(driver,"profilepic.png", category)
                theuser = newuser.split(":")[0].strip().replace("\n","").replace("\r","")   
                os.system(str("curl http://accounthaven.net/addaccountstofollow.php?acc="+str(theuser)))
                
            repost(category, theuser, driver)
        try:
            driver.close()
            driver.quit()
        except:
            print("Error closing browser")

