from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep



driver = webdriver.Chrome()
driver.maximize_window()


driver.get('https://kariyer.baykartech.com/tr/')


lan = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/nav/div/div[2]/div[2]/ul/div/li[2]/a")
lan.click()
sleep(3)
kariyer = driver.find_element(By.XPATH, "/html/body/div[3]/section[1]/div/div/div[1]/div[2]/div/div/div/div[2]/button")
testresult = kariyer.text == "OPEN POSITIONS"
print(f"sonuc : {testresult}")
sleep(5)

lang = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/nav/div/div[2]/div[2]/ul/div/li[2]/a")
lang.click()
sleep(2)
kariyer1 = driver.find_element(By.XPATH,"/html/body/div[3]/section[1]/div/div/div[1]/div[2]/div/div/div/div[2]/button")
testresult1 = kariyer1.text == "AÇIK POZİSYONLAR"
print(f"sonuc1 : {testresult1}")
sleep(10)








