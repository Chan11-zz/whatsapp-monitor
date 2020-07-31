import time
from datetime import datetime as dt
from selenium import webdriver
from Person import Person
print("Enter number of persons to track")
n=int(input())
People=[]
while n:
    People.append(Person())
    n=n-1
print("Enter name")
for p in People:
    p.add_name(input())
    print(p.name)

start_time=None
end_time=None

driver = webdriver.Chrome('D:\chromedriver.exe')
driver.get('https://web.whatsapp.com/');
time.sleep(5) # Let the user actually see something!
while(True):
    chat=driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div/header/div[2]/div/span/div[2]/div")
    chat.click()
    time.sleep(2)
    for p in People:
        search_name=driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[1]/span/div/span/div/div[1]/div/label/div/div[2]")
        search_name.click()
        search_name.send_keys(p.name)
        time.sleep(2)
        user=driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[1]/span/div/span/div/div[2]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div/span/span")
        user.click()
        time.sleep(2)
        status=driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/header/div[2]/div[2]/span")
        status=status.get_attribute("title")
        if(len(status)==6):
            print("now online",status,len(status))
            p.online(dt.now())
        else:
            print("offline",status,len(status))
            t=dt.now()
            #dt.strptime(status,'last seen today at %H:%M')
            print(t,p.lastseen)
            p.lastseen(t)
    
        

driver.quit()
