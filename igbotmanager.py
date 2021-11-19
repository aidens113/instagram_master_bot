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


def press_key(key, driver):
    actions = ActionChains(driver)
    actions.send_keys(key)
    actions.perform()

def randkeys(element, keys, driver):
    for myi in keys:
        element.send_keys(myi)
        time.sleep(random.uniform(0.05, 0.25))


def drag_and_drop_file(drop_target, path, driver):
    JS_DROP_FILE = """
    var target = arguments[0],
        offsetX = arguments[1],
        offsetY = arguments[2],
        document = target.ownerDocument || document,
        window = document.defaultView || window;

    var input = document.createElement('INPUT');
    input.type = 'file';
    input.onchange = function () {
      var rect = target.getBoundingClientRect(),
          x = rect.left + (offsetX || (rect.width >> 1)),
          y = rect.top + (offsetY || (rect.height >> 1)),
          dataTransfer = { files: this.files };

      ['dragenter', 'dragover', 'drop'].forEach(function (name) {
        var evt = document.createEvent('MouseEvent');
        evt.initMouseEvent(name, !0, !0, window, 0, 0, 0, x, y, !1, !1, !1, !1, 0, null);
        evt.dataTransfer = dataTransfer;
        target.dispatchEvent(evt);
      });

      setTimeout(function () { document.body.removeChild(input); }, 25);
    };
    document.body.appendChild(input);
    return input;
    """
   
    file_input = driver.execute_script(JS_DROP_FILE, drop_target, 0, 0)
    file_input.send_keys(path)

def changeprofilepic(driver, link):
    try: 
        driver.get("https://instagram.com/accounts/edit")
        
        for _ in range(15):
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
        
        acc = allaccs[0]
        username = newuser(driver)
        allaccs.remove(allaccs[0])
        allaccs.append(str(username.strip().replace("\n","").replace("\r","") +":"+ acc.split(":")[1].strip().replace("\n","").replace("\r","") +":yes\n"))
        
        file = open("igaccountsmade.txt", "w")
        file.writelines(allaccs)
        file.close()
    except Exception as EE:
        print("Error changing profile pic: "+str(EE))
        return

def newuser(driver):
    try:
        driver.get("https://www.instagram.com/accounts/edit/")
        time.sleep(1)
        name = ""
        username = ""
        
        for _ in range(50):
            
            try:
                name = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/form/div[1]/div/div/input').get_attribute("value")
            except Exception as EE:
                print("Error finding value: "+str(EE))
            try:                              
                driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/form/div[2]/div/div/input').click()
                time.sleep(random.uniform(0.5, 1.4))
                for myii in range(random.randint(25, 31)):
                    press_key(Keys.BACKSPACE, driver)
                    time.sleep(random.uniform(0.001, 0.01))
                time.sleep(random.uniform(0.1, 0.6))
                username = name
                myrand = random.randint(0,10)
                if myrand >= 5:
                    username = str(username.strip().replace(" ","_"))
                else:
                    username = str(username.strip().replace(" ","."))

                myrand = random.randint(0,10)
                if myrand >= 5:
                    username = str(username+str(random.randint(0,99)))
                else:
                    username = str(str(random.randint(0,99))+username)
                
                    
                randkeys(driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/form/div[2]/div/div/input'), username, driver)
                breaks
            except:
                print("Looking for name")

        try:
            driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/form/div[2]/div/div/input').submit()
        except Exception as EE:
            print("Error submitting: "+str(EE))
      
        return username            

        
    except Exception as EE:
        print("Error with new username "+str(EE))

  
def login(driver, user, passw):
    for _ in range(5):
        try:
            
            driver.get("https://www.instagram.com/accounts/login/")

            time.sleep(2)

            for _ in range(5):
                try:
                    if driver.find_element_by_xpath('/html/body/div[2]/div/div/button[1]') != None:
                        driver.find_element_by_xpath('/html/body/div[2]/div/div/button[1]').click()
                        
                        time.sleep(1)
                        for _ in range(15):
                            try:
                                if driver.find_element_by_xpath('/html/body/div[2]/div/div/button[1]') != None:
                                    print("accept button still visible")
                            except Exception as EEE:
                                print("accept button no longer visible: "+str(EEE))
                                break
                            time.sleep(1)
                except:
                    print("Error")
                time.sleep(1)

            for _ in range(5):
                try:
                    if driver.find_element_by_xpath('//*[@id="loginForm"]/div[1]/div[3]/div/label/input') != None:
                        randkeys(driver.find_element_by_xpath('//*[@id="loginForm"]/div[1]/div[3]/div/label/input'),user, driver)            
                        break
                except:
                    print("Looking for user")
                time.sleep(1)
            for _ in range(5):
                try:
                    if driver.find_element_by_xpath('//*[@id="loginForm"]/div[1]/div[4]/div/label/input') != None:
                        randkeys(driver.find_element_by_xpath('//*[@id="loginForm"]/div[1]/div[4]/div/label/input'),passw , driver)            
                        break
                except:
                    print("Looking for pass")
                time.sleep(1)

            for _ in range(5):
                try:
                    
                    if driver.find_element_by_xpath('//*[@id="loginForm"]/div[1]/div[6]/button') != None:
                        driver.find_element_by_xpath('//*[@id="loginForm"]/div[1]/div[6]/button').click()            
                        break
                except:
                    print("Looking for submit button")
                time.sleep(1)


            time.sleep(2)
            for _ in range(40):
                try:
                    if driver.current_url == "https://www.instagram.com/accounts/login/":
                        print("Mistake with login. Trying again")
                        break
                    if driver.current_url == "https://www.instagram.com/accounts/onetap/?next=%2F":
                        return
                    try:
                        if driver.find_element_by_xpath("/html/body/div[1]/section/main/div[1]/div/div/div/form/div[2]/p") != None:
                            print("Found error")
                            return False  
                    except:
                        print("No error msg")
                    if "challenge" in driver.current_url:
                        print("Got challenge")
                        file = open("igaccountsmade.txt", "r")
                        allaccs = file.readlines()
                        file.close()

                        allaccs.remove(allaccs[0])

                        file = open("igaccountsmade.txt", "w")
                        file.writelines(allaccs)
                        file.close()
                        
                        return False
                except:
                    print("Waiting for login")

                time.sleep(1)

        except Exception as EE:
            print("Error: "+str(EE))



def follow(driver, user):

    try:
        driver.get(str("https://instagram.com/"+str(user)))
        time.sleep(random.uniform(0.8, 1.3))
        for _ in range(5):
            
            try:
                #if driver.find_element_by_xpath("//*[text()='Follow']") != None:
                  
                if driver.find_element_by_xpath("//*[text()='Follow']") != None:
                    driver.find_element_by_xpath("//*[text()='Follow']").click()
                    time.sleep(2)
                    try:
                        if driver.find_element_by_xpath('/html/body/div/div[1]/div/div/h2') != None:
                            print("Content missing. Removing from list")
                            return 'missing'
                            
                    except Exception as EEE:
                        print("No content missing message: "+str(EEE))
                        
                    for _ in range(5):
                        try:
                            if driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[1]/div') != None:
                                print("Found try again message")
                                return False
                        except:
                            print("No try again message")
                        try:
                            time.sleep(0.4)
                            if driver.find_element_by_xpath("//*[text()='Follow']") != None:
                                like3posts(driver,user)
                                return     
                        except:
                            print("Checking follow text")
                    return False
                    
                
            except:
                print("Looking for follow button")

            try:
                if driver.find_element_by_xpath("//*[text()='Message']") != None:          
                    return
                
            except:
                print("Looking for follow button")
            time.sleep(0.5)
    except:
        print("Error with follow")

    
def like(driver,postid):
    driver.get("https://instagram.com/p/"+str(postid))

    for _ in range(6):
        press_key(Keys.SPACE, driver)
        time.sleep(random.uniform(0.8, 1.3))
        try:
            driver.find_element_by_class_name('storiesSpriteX__outline__44 u-__7').click()
        except:
            print("Clicking x button on popup")

        try:
            driver.find_element_by_class_name('glyphsSpriteGrey_Close u-__7').click()
        except:
            print("Clicking x button on popup")

            
        try:                                 
            if driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[3]/section[1]/span[1]/button') != None:
                try:
                    #fill = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[3]/section[1]/span[1]/button/div/span/svg').get_attribute("fill")
                    #if str(fill) == str("#ed4956"):
                        #print("Already liked")
                        #break
                    #else:
                    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[3]/section[1]/span[1]/button').click()
                    break
                except Exception as ee:
                    print("Error getting liked/unliked status: "+str(ee))
                    break
            
        except:
            print("Looking for like button")
        time.sleep(0.5)


def like3posts(driver, user):
    driver.get(str("https://instagram.com/"+str(user)))
    time.sleep(1)
    links = []
    for _ in range(5):
        try:
            for i in range(1,4):
                try:
                    element = str('/html/body/div[1]/section/main/div/div[3]/article/div/div/div[1]/div['+str(i)+']/a')
                                   
                    print(element)
                    src = driver.find_element_by_xpath(element).get_attribute('href')
                    print(src)
                    link = src.split("p/")[1].strip()
                    print(link)
                    links.append(link)
                except:
                    print("Error adding link to likeable posts. Most likely not enough posts yet")
            for i in range(3):
                try:
                    like(driver, links[i])
                except:
                    print("Error liking post. Most likely not enough posts yet")
            return
        except Exception as EE:
            print("Error: "+str(EE))
            time.sleep(3)

def changeprofilepic1(driver, link, category):
    try:
        for myii in range(10):
            try:
                try:
                    driver.get("https://www.instagram.com/explore/tags/"+str(category))
                except Exception as EEEE:
                    print("Error getting url. trying anyways: "+str(EEEE))
                time.sleep(2)
                myrow = 1
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
            except Exception as ERRR:
                print("error: "+str(ERRR))

            
        for _ in range(10):
            try:
                driver.get("https://instagram.com/accounts/edit")
                
                for _ in range(5):
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
                try:
                    time.sleep(2)    
                    try:
                        driver.find_element_by_xpath('//*[@id="react-root"]/section/div[1]/header/div/div[2]/button').click()
                    except Exception as EEE:
                        print("Error clicking button: "+str(EEE))
                    time.sleep(1)
                    
                    #os.remove(link)

                    file = open("igaccountsmade.txt", "r")
                    allaccs = file.readlines()
                    file.close()
                    
                    acc = str(allaccs[0])
                    #username = newuser(driver)
                    allaccs.remove(allaccs[0])
                    allaccs.append(str(acc.split(":")[0].strip().replace("\n","").replace("\r","") +":"+ acc.split(":")[1].strip().replace("\n","").replace("\r","") +":yes\n"))
                    
                    file = open("igaccountsmade.txt", "w")
                    file.writelines(allaccs)
                    file.close()
                    return
                except Exception as EEE:
                    print("Error: "+str(EEE))
                
            except Exception as ERrr:
                print("error: "+str(ERrr))
    except Exception as EE:
        print("Error changing profile pic: "+str(EE))
        return


        
def initdriver(proxy):
    chrome_options = webdriver.ChromeOptions()
    mobile_emulation = {

        "deviceMetrics": { "width": 360, "height": 640, "pixelRatio": 3.0 },

    "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19" }

    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    #prefs = {"profile.managed_default_content_settings.images": 2}
    #chrome_options.add_experimental_option("prefs", prefs)
    # chrome_options.add_argument('--user-data-dir=C:\\Users\\exoti\\AppData\\Local\\Google\\Chrome\\User Data\\')
    #chrome_options.add_argument("--load-extension=C:\\Users\\exoti\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Extensions\\hapgiopokcmcnjmakciaeaocceodcjdn\\6.4_0")
    #chrome_options.add_argument(str('--profile-directory=Default'))
    #chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument(str('--proxy-server=http://'+str(proxy)))
    #chrome_options.add_argument("--headless")   
    driver = webdriver.Chrome(executable_path='chromedriver.exe',options=chrome_options)
    driver.set_page_load_timeout(45)
    #driver.set_window_position(0, -2000, windowHandle='current')
    driver.delete_all_cookies()
    return driver


def fullprocess(proxy, index, threadnum):
    file = open("igaccountsmade.txt", "r")
    allaccounts = file.readlines()
    file.close()

    print("STARTING THREAD NUMBER "+str(index)+" WITH PROXY "+str(proxy))
    for mainloop in range(int(len(allaccounts) - index)):
        try:
           
            acc = allaccounts[int(index + int(threadnum * mainloop))]
            driver = initdriver(proxy)

            acc2 = acc.strip().replace("\n","").replace("\r","")
            if login(driver, acc2.split(":")[0],acc2.split(":")[1]) != False:
                #profile
                try:
                    hasprofile = acc2.split(":")[2]
                except:
                    print("No Profile Picture Data. Making one")
                    
                    male = False

                    file = open("profilemaker\\name\\femalegen.txt", "r")
                    femalenames = file.readlines()
                    file.close()

                    for line in femalenames:
                        if line.strip().replace("\r","").replace("\n","").lower() in acc2.split(":")[0].strip():
                            male = False
                            break
                        
                    file = open("profilemaker\\name\\malegen.txt", "r")
                    malenames = file.readlines()
                    file.close()

                    for line in malenames:
                        if line.strip().replace("\r","").replace("\n","").lower() in acc2.split(":")[0].strip():
                            male = True
                            break
                         
                    
                    if male == True:
                        #files = os.listdir("profilemaker\\profileman\\")
                        categories = ['art','painting','men','man','gym','photography','photos', 'photo','anime','cartoon','drone', 'dronephotography','house','mansion','car','supercar','dronestagram']
                        category = categories[random.randint(0,int(len(categories) - 1))]
                        changeprofilepic1(driver,"profilepic.png", category)
                    else: 
                        #files = os.listdir("profilemaker\\profileman\\")
                        categories = ['art','painting','woman','women','gym','photography','fitness','photos', 'photo','anime','cartoon','drone', 'dronephotography','house','mansion','car','supercar','dronestagram']
                        category = categories[random.randint(0,int(len(categories) - 1))]
                        changeprofilepic1(driver,"profilepic.png", category)
                file = open("accstofollow.txt", "r")
                accstofollow = file.readlines()
                file.close()

                #Follow loop
                for t in range(len(accstofollow)):
                    status = follow(driver,accstofollow[t].strip().replace("\n","").replace("\r",""))
                    if status == False:
                        break
                    if status == 'missing':
                        accstofollow.remove(accstofollow[t])

                file = open("accstofollow.txt", "w")
                file.writelines(accstofollow)
                file.close()
                
            try:
                driver.close()
                driver.quit()
            except:
                print("Error with driver")      
                
        except Exception as Err:
            print("Big error: "+str(Err))
        


def startallthreads(threadnum):
    threads = []
    thist = 0
    for i in range(threadnum):
        
        if thist >= int(len(allproxies) - 1):
            thist = 0
        else:
            thist += 1
        thread = threading.Thread(target=fullprocess, args=(allproxies[thist],i,threadnum,))
        threads.append(thread)
    for thread in threads:
        thread.start()
        time.sleep(0.5)
    for thread in threads:
        thread.join()

while True:
    startallthreads(18)
    
            
        
    


