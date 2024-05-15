from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


driver = webdriver.Chrome()
driver.maximize_window()


driver.get("https://kariyer.baykartech.com/tr/")


#captche sebebiyle bu kısım çalışamıyor.
loginbutton = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/nav/div/div[2]/div[2]/ul/div/li[1]/a")
loginbutton.click()
sleep(3)


username = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/form/div[2]/input")
username.send_keys("asdasda")
sleep(2)

password = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/form/div[3]/input")
password.send_keys("12345")
sleep(2)

login = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/form/div[5]/button")
login.click()


acikpoz = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/nav/div/div[2]/div[2]/ul/div/li[1]/a")
acikpoz.click()
sleep(2)

# Ana sayfaya giriş yaptığı senaryoda

closeBttn = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[6]/button[3]")
closeBttn.click()


acikpoz1 = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[4]/div/div/div[1]/div/div/div/a")
acikpoz1.click()
sleep(2)

checkbox = driver.find_element(By.XPATH, "/html/body/section[2]/div/div/div[2]/div/div[2]/ul/div[2]/li/div/input")
checkbox.click()
sleep(2)


input = driver.find_element(By.XPATH, "/html/body/section[2]/div/div/div[3]/div[1]/input")
input.send_keys("otopilot")
input.send_keys(Keys.ENTER)



##açık pozisyonlar tıklanamadığı için dashboard üzerinden gittim ama kod çalıştırıldığında,
##login isteyecek ve captcha sebebiyle o kısma giriş yapamayacak.
##ma yine de bu şekilde yazmak istedim belirtmek isterim teşekkürler.


dogrulama = driver.find_element(By.XPATH, "/html/body/section[2]/div/div/div[3]/div[2]/div/div/h3")
testresult = dogrulama.text == "Otopilot"
print(f"test sonuç : {testresult} ")
