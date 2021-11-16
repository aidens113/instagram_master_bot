import mss
import mss.tools
import os
import sys
import requests
import random
import time
import pyautogui
from PIL import Image
import cv2
import pyaudio
import wave


def record():

    #while pyautogui.locateCenterOnScreen("bsimg/headphones.PNG", confidence=0.8) != None:
    pyautogui.moveTo(pyautogui.locateCenterOnScreen("bsimg/headphones.PNG", confidence=0.8))
    time.sleep(0.5)
    pyautogui.click()
    time.sleep(1)
        
    time.sleep(5)
    
    CHUNK_SIZE = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    RECORD_SECONDS = 8
    WAVE_OUTPUT_FILENAME = "output.wav"

    p = pyaudio.PyAudio()
    

    stream  = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, output=True,frames_per_buffer=CHUNK_SIZE, input_device_index=1)

    print("* recording")
    time.sleep(1)
    pyautogui.moveTo(pyautogui.locateCenterOnScreen("bsimg/playsound.PNG", confidence=0.8))
    time.sleep(1)
    pyautogui.click()
    time.sleep(0.1)
    pyautogui.click()
    time.sleep(0.1)
    pyautogui.click()
    time.sleep(1)
        
    frames = []

    for i in range(0, int(RATE / CHUNK_SIZE * RECORD_SECONDS) + 1):
        data = stream.read(CHUNK_SIZE)
        frames.append(data)

    print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
       

#submitbuttoncoords = (837, 751)

def screenshot():
    try:
        # The screen part to capture
        region = {'top':133 , 'left':477, 'width': 424, 'height': 571}

        # Grab the data
        img = mss.mss().grab(region)

        # Save to the picture file
        mss.tools.to_png(img.rgb, img.size, output='recaptcha.png')
        time.sleep(0.2)
        picture = Image.save("recaptcha.png")
        picture.save("recaptcha.png", "PNG", optimize = True, quality = 10)
    except:
        print("Error in screenshot")


def sendcaptcha():
    try:

        headers = {'authorization': "498616f599fe4c5897cf13555dadc37d"}
        response = requests.post('https://api.assemblyai.com/v2/upload',headers=headers,data=open("output.wav", 'rb'))
        print(response.json())

        time.sleep(5)
        endpoint = "https://api.assemblyai.com/v2/transcript"

        json = {
          "audio_url": str(response.json()['upload_url'])
        }

        headers = {
            "authorization": "498616f599fe4c5897cf13555dadc37d",
            "content-type": "application/json"
        }

        response = requests.post(endpoint, json=json, headers=headers)

       

        status = ""

        while "completed" not in status:
            time.sleep(5)
            print("ID: "+str(response.json()['id']))
            endpoint = "https://api.assemblyai.com/v2/transcript/"+str(response.json()['id'])

            headers = {
                "authorization": "498616f599fe4c5897cf13555dadc37d",
            }
            
            response = requests.get(endpoint, headers=headers)
            
        
            status = response.json()['status']
            finalresponse = response.json()
            print("Status: "+str(status))


        stringtotype = ""
        for words in finalresponse['words']:
            stringtotype = stringtotype+" "+str(words['text'])
            
        print("Words: "+str(stringtotype))
        pyautogui.moveTo(pyautogui.locateCenterOnScreen("bsimg/enterbar.PNG", confidence=0.8))
        time.sleep(0.5)
        pyautogui.click()
        time.sleep(1)
        pyautogui.write(stringtotype)
        time.sleep(1)
        
        pyautogui.moveTo(pyautogui.locateCenterOnScreen("bsimg/verify.PNG", confidence=0.8))
        time.sleep(0.5)
        pyautogui.click()
        
        #f = open('recaptcha.png', 'rb')
        #imgdata = f.read()
        #f.close()

        #img = base64.b64encode(imgdata)
        #previousid = ''
        #if "None" not in myid:
            #previousid = 'previousID'myid

        #print("PreviousID found. Continuing captcha")
        #postdata = {'key':'3fd94090a145df3bd4889a46ecfebbf6','method':'post','coordinatescaptcha':'1','canvas':'1',previousid,'textinstructions':'Follow captcha instructions.'}
        
        #response = requests.post('http://2captcha.com/in.php', data=postdata, files={'file':open('recaptcha.png','rb')})
        #myid = response.text.strip()
        #print("Myid: "+str(myid))
        #return myid
    except Exception as ee:
        print("Error with sendcaptcha: "+str(ee))
        time.sleep(10)

def completecaptcha():
    while True:
        try:
            postdata = {'key':'3fd94090a145df3bd4889a46ecfebbf6','action':'get','id':myid}
            response.text = requests.post('http://2captcha.com/in.php', data=postdata)
            if "canvas" in response.text:
                coords = response.text.split("canvas")[1].split(",")
                print("Got coords. Clicking")
                #for i in range(len(coords)):
                    #if !(i % 2) == 0:
                        #coordstoclickx = int(coords[int(i)])
                        #coordstoclicky = int(coords[int(i+1)])
                        #print("clicking at "+str(coordstoclickx)+" "+str(coordstoclicky))
                
                print("Finished clicking")
                return
            else:
                time.sleep(5)
        except Exception as ee:
            print("Error with completecaptcha: "+str(ee))
            time.sleep(10)



while True:
    try:
        if pyautogui.locateCenterOnScreen("bsimg/captcha.PNG", confidence=0.8) == None:
            break
    except:
        print('Couldnt find any captcha. Breaking')

    record()
    sendcaptcha()
    
    
