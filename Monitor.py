import time
from selenium import webdriver

print("Enter name to search")
name=input()
driver = webdriver.Chrome('D:\chromedriver.exe')
driver.get('https://web.whatsapp.com/');
time.sleep(5) # Let the user actually see something!
chat=driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div/header/div[2]/div/span/div[2]/div")
chat.click()
time.sleep(2)
search_name=driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[1]/span/div/span/div/div[1]/div/label/div/div[2]")
search_name.click()
search_name.send_keys(name)
time.sleep(2)
Person=driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[1]/span/div/span/div/div[2]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div/span/span")
Person.click()
time.sleep(2)
Status=driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/header/div[2]/div[2]/span")
print(Status.get_attribute("title"))
driver.quit()
