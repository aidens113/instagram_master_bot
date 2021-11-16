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
from os import listdir
import base64
from os.path import isfile, join
from PIL import Image
import numpy as np 

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


def press_key(key):
    actions = ActionChains(driver)
    actions.send_keys(key)
    actions.perform()

def randkeys(element, keys):
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



def initdriver(profile):
    try:
        chrome_options = webdriver.ChromeOptions()
       #mobile_emulation = {

            #"deviceMetrics": { "width": 360, "height": 640, "pixelRatio": 3.0 },

        #"userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19" }

        #chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        if profile == True:
            chrome_options.add_argument('--user-data-dir=C:\\Users\\aiden\\AppData\\Local\\Google\\Chrome\\User Data\\')
            #chrome_options.add_argument("--load-extension=C:\\Users\\exoti\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Extensions\\hapgiopokcmcnjmakciaeaocceodcjdn\\6.4_0")
            chrome_options.add_argument(str('--profile-directory=Default'))
        #chrome_options.add_argument("--start-maximized")
        #chrome_options.add_argument('--proxy-server=http://163.172.36.181:15001')
        chrome_options.add_argument("--headless")   
        driver = webdriver.Chrome(executable_path='chromedriver.exe',options=chrome_options)
        
        driver.delete_all_cookies()
        return driver
    except Exception as EE:
        print("Error init driver: "+str(EE))

def genface(driver, male):
    while True:
        try:
            driver.get("https://generated.photos/face-generator/new")
            time.sleep(3)
            
            #FEMALE OR MALE
            
            if male == True:
                driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/aside/div[2]/div[3]/div/div[2]/div[1]/div/div[1]/input').click()
            else:
                driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/aside/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/input').click()

            #AGE
            en =  driver.find_element_by_xpath('//*[@id="ageSlider"]/input')
            move = ActionChains(driver)
            move.click_and_hold(en).move_by_offset(random.randint(10, 50), 0).release().perform()
            time.sleep(1)


            #SKIN TONE
            i = random.randint(1, 6)
            xpath = "/html/body/div[1]/div/div/div[1]/aside/div[2]/div[3]/div/div[2]/div[5]/div/div/div["+str(i)+"]/div"
            driver.find_element_by_xpath(xpath).click()
            time.sleep(0.5)
            

            #NO GLASSES
            try:
                driver.find_element_by_xpath('//*[@id="no"]').click()
            except:
                print("Error clicking no glasses")
            time.sleep(3)
            
            #UPDATE FACE
            
            driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/aside/div[3]/div[2]/button').click()

            time.sleep(10)
            src = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/main/div[2]/div[1]/img').get_attribute("src")
            urllib.request.urlretrieve(src, "facegeneration.png")
            return
        except Exception as EE:
            print("Genface error: "+str(EE))


def faceswap(driver, male):
    driver.get("https://reflect.tech/faceswap/my")
    time.sleep(3)
    if male == True:
        dire = ("C:\\Users\\aiden\\coding\\Botting - The New Era\\accounthaven.net\\instagram bot\\profilemaker\\men")
    else:
        dire = ("C:\\Users\\aiden\\coding\\Botting - The New Era\\accounthaven.net\\instagram bot\\profilemaker\\woman")

    files = os.listdir(dire)
    myfilei = files[random.randint(0, (len(files) - 1))]
    myfile = str(dire+"\\"+str(myfilei))
    print("Using base image: "+str(myfile))
    time.sleep(2)
    drag_and_drop_file(driver.find_element_by_xpath('//*[@id="dropzone"]/div/span/div'), myfile, driver)
    time.sleep(3)

    while True:
        if driver.current_url != "https://reflect.tech/faceswap/my":
            break
        time.sleep(1)
    time.sleep(3)
    driver.find_element_by_class_name('face-block').click()
    time.sleep(2)
    drag_and_drop_file(driver.find_element_by_xpath("//*[text()='Add faces to swap to']"), 'C:\\Users\\aiden\\coding\\Botting - The New Era\\accounthaven.net\\instagram bot\\profilemaker\\facegeneration.png', driver)    
    time.sleep(4)
    driver.find_element_by_class_name('imgAvatar').click()
    time.sleep(3)
    while True:
        try:
            if driver.find_element_by_xpath('//*[@id="app"]/div/main/div/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div[1]') != None:
                break
        except:
            print("Looking for download button")
    time.sleep(1)
    src = driver.find_element_by_xpath('//*[@id="app"]/div/main/div/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div[1]').get_attribute("src")
    urllib.request.urlretrieve(src, "person.png")

    img2 = Image.open("person.png")
    w, h = img2.size
    factor = random.randint(1,8)
    #img2 = img.resize((int(w / factor), int(h / factor)))
    
    myrand = random.randint(0,10)
    if myrand >= 5:
        print("flipping img")
        img2 = img2.transpose(Image.FLIP_LEFT_RIGHT)
    else:
        print("not flipping img")
    img2.save(str('person.png'),"PNG")

def genbackground(driver):
    file = open("cap.txt", "r")
    allcaps = file.readlines()
    file.close()

    texttosend = ""
    for _ in range(random.randint(2, 5)):
        texttosend = str(texttosend + " " + allcaps[random.randint(0, (len(allcaps) - 1)  )])

    
    driver.get("https://vision-explorer.allenai.org/text_to_image_generation")
    time.sleep(3)
    press_key(Keys.SPACE)
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="root"]/section/section/section/main/main/form/div[2]/textarea').click
    time.sleep(0.4)
    driver.find_element_by_xpath('//*[@id="root"]/section/section/section/main/main/form/div[2]/textarea').send_keys(texttosend)
    time.sleep(1)
    driver.find_element_by_xpath("//*[text()='Run Model']").click()
    time.sleep(6)
    press_key(Keys.SPACE)
    time.sleep(2)
    canvas = driver.find_element_by_xpath('//*[@id="root"]/section/section/section/main/main/div[6]/div[2]/div/div[2]/div/div/div/canvas')
    canvas_base64 = driver.execute_script("return arguments[0].toDataURL('image/png').substring(21);", canvas)

    # decode
    canvas_png = base64.b64decode(canvas_base64)

    # save to a file
    with open(r"background.png", 'wb') as f:
        f.write(canvas_png)
    #imgb64 = str((src.split(",")[1]).strip().replace("\n","").replace("\r",""))


def changebackground(driver, male):
    driver.get("https://www.slazzer.com/upload")
    time.sleep(5)
    drag_and_drop_file(driver.find_element_by_xpath('//*[@id="drag-drop-more-then-one"]/div[1]/div/div/button'),'C:\\Users\\aiden\\coding\\Botting - The New Era\\accounthaven.net\\instagram bot\\profilemaker\\person.png',driver)
    time.sleep(8)
    src = driver.find_element_by_xpath('/html/body/div[2]/div[7]/div/div/div[1]/div[2]/div[1]/img').get_attribute('src')
    print(src)
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    urllib.request.install_opener(opener)
    
    urllib.request.urlretrieve(src, "persontransparent.png")

    

    img2 = Image.open("persontransparent.png")

    background = Image.open("background.png")
    
    w, h = img2.size
    #w2, h2, = background.size
    background2 = background.resize((w, h), Image.LANCZOS)
    
    
    
    
    #dif = w2 - w

    #if w < w2:
    #    width = (int((dif / 2)))
    #else:
    #    width = (int(-(dif / 2)))
    pos = random.randint(3,7)
    #img2 = img2.convert('RGBA')
    #background = background.convert('RGBA')
    myrand = random.randint(0,11)
    if myrand >= 6:
        background2.paste(img2, (int(w / pos), int(h / pos)), img2)
    else:
        background2.paste(img2, (-int(w / pos), int(h / pos)), img2)
        
    if male == True:
        background2.save(str('profileman/profile'+str(random.randint(99999,9999999999))+'.png'),"PNG")
    else:
        background2.save(str('profilewoman/profile'+str(random.randint(99999,9999999999))+'.png'),"PNG")
    
    #drag_and_drop_file(driver.find_element_by_xpath('//*[@id="background-image"]/div/div/div[2]/div/button[1]/div'),'C:\\Users\\aiden\\coding\\Botting - The New Era\\accounthaven.net\\instagram bot\\profilemaker\\background.png',driver)



    

while True:
    try:
        myrand = random.randint(0,10)
        if myrand >= 5:
            male = True
        else:
            male = False
        driver = initdriver(False)
        genface(driver, male)
        try:
            driver.close()
            driver.quit()
        except:
            print("Error exiting driver")
        driver = initdriver(True)
        faceswap(driver, male)
        try:
            driver.close()
            driver.quit()
        except:
            print("Error exiting driver")
        driver = initdriver(False)
        genbackground(driver)
        changebackground(driver, male)
        try:
            driver.close()
            driver.quit()
        except:
            print("Error exiting driver")
    except Exception as EE:
        print("Error: "+str(EE))
