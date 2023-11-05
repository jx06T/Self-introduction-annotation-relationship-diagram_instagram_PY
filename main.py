from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import keyboard
from draw import PeopleGraph
import threading
import time

import HTML_JS
import reptile

def ShowGUI(driver):
    global crawler
    driver.switch_to.window(driver.window_handles[-1])
    if crawler.state == 0:
        print("ss")
        try:
            alert = driver.switch_to.alert
        except:
            current_url = driver.current_url
        if "https://www.instagram.com/" in current_url:
            CreatNewButton(driver)
        t = None
        try:
            t = WebDriverWait(driver, timeout=30, poll_frequency=0.5).until(EC.alert_is_present())
        except:
            pass
        
        if not t == None:
            start(driver)
            return
            
        try:
            alert = driver.switch_to.alert
            alert.dismiss()
        except:
            pass

        DeleteGUI(driver)

def Stoppp():
    print("!!!!!!!!!!")
    global crawler
    driver.switch_to.window(driver.window_handles[-1])
    driver.execute_script(HTML_JS.injection_button2)
    try:
        t = WebDriverWait(driver, timeout=30, poll_frequency=0.5).until(EC.alert_is_present())
    except:
        pass
    
    if not t == None:
        crawler.Play()
        return
        
    try:
        alert = driver.switch_to.alert
        alert.dismiss()
    except:
        pass
    driver.execute_script(HTML_JS.remove_button2)


def DeleteGUI(driver):
    driver.execute_script(HTML_JS.remove_button)

def CreatNewButton(driver):
    driver.execute_script(HTML_JS.injection_button)

def start(driver):
    try:
        MaxLevel = driver.find_element(By.ID, 'jx06I2').get_attribute("value")
        MaxStep = driver.find_element(By.ID, 'jx06I1').get_attribute("value")
        me = driver.find_element(By.CSS_SELECTOR,'h2.x1lliihq.x1plvlek.xryxfnj.x1n2onr6.x193iq5w.xeuugli.x1fj9vlw.x13faqbe.x1vvkbs.x1s928wv.xhkezso.x1gmr53x.x1cpjm7i.x1fgarty.x1943h6x.x1i0vuye.x1ms8i2q.xo1l8bm.x5n08af.x10wh9bi.x1wdrske.x8viiok.x18hxmgj')
        me = me.text
    except:
        me = ""
        print("33")
        MaxLevel = ""
        MaxStep = ""

    print(me,MaxLevel,MaxStep)
    MaxLevel = int(MaxLevel) if not MaxLevel == "" else 4
    MaxStep = int(MaxStep) if not MaxStep == "" else 300
    print("start")
    global crawler
    crawler = reptile.InstagramCrawler(driver, MaxLevel, MaxStep,Stoppp)
    people = crawler.crawl()
    print(people)
    if not people:
        return
    graph = PeopleGraph(people)
    graph.show_graph(me,driver)

# %%
driver = webdriver.Chrome()
driver.get("https://www.instagram.com/")
time.sleep(1)
driver.execute_script(HTML_JS.note)
crawler = reptile.InstagramCrawler(driver,1,1,Stoppp)
keyboard.add_hotkey('ctrl+alt+g',lambda: ShowGUI(driver) )
keyboard.wait()

input()
driver.quit()