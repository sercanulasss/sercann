from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


driver = webdriver.Chrome()
driver.maximize_window()


driver.get("https://kariyer.baykartech.com/tr/")


Kariyer_link = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/nav/div/div[2]/div[2]/ul/li[1]/a")
Kariyer_link.click()
sleep(5)

yüksekirtifa = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/nav/div/div[2]/div[2]/ul/li[1]/ul/li[1]/a")
yüksekirtifa.click()
sleep(2)

Kariyer1 = driver.find_element(By.XPATH, "/html/body/section/nav/div[2]/ul/li[1]/a/span")
Kariyer1.click()
sleep(2)

yerles = driver.find_element(By.XPATH, "/html/body/section/nav/div[2]/ul/li[1]/ul/li[2]/a")
yerles.click()
sleep(2)

Kariyer2 = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/nav/div/div[2]/div[2]/ul/li[1]/a")
Kariyer2.click()
sleep(2)



sosyal = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/nav/div/div[2]/div[2]/ul/li[1]/ul/li[3]/a")
sosyal.click()
sleep(2)



acikpoz = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/nav/div/div[2]/div[2]/ul/li[3]/a")
acikpoz.click()
sleep(2)

ssh = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/nav/div/div[2]/div[2]/ul/li[7]/a")
ssh.click()
sleep(2)


expected_url1 = "https://kariyer.baykartech.com/tr/sss/"
actual_url1 = driver.current_url

if expected_url1 == actual_url1:
    print("SSH sonrasi sayfa açildi, test başarili.")
else:
    print(f"Hata: Beklenen URL: '{expected_url1}', Açılan URL: '{actual_url1}'")

    

staj = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/nav/div/div[2]/div[2]/ul/li[5]/a")
staj.click()
sleep(1)


expected_url2 = "https://kariyer.baykartech.com/tr/staj/"
actual_url2 = driver.current_url

if expected_url2 == actual_url2:
    print("Staj sonrasi sayfa açildi, test başarili.")
else:
    print(f"Hata: Beklenen URL: '{expected_url2}', Açılan URL: '{actual_url2}'")



baykar = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/nav/div/div[2]/div[2]/ul/li[9]/a")
baykar.click()
sleep(2)

expected_url3 = "https://baykartech.com/tr/"
actual_url3 = driver.current_url

if expected_url3 == actual_url3:
    print("Baykar sonrasi sayfa açildi, test başarili.")
else:
    print(f"Hata: Beklenen URL: '{expected_url3}', Açılan URL: '{actual_url3}'")





