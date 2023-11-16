from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from extensions import elements, keyboard

# Baslangic addim
counter_step = 0
# Limit
limit = 6
# nomreler toplanacaq
numbers = ""
# Kontaktin adi
contact_name = "Metros"

# ChromeDriver'ın yolu
chrome_driver_path = '/usr/bin/chromedriver'

# ChromeOptions ve ChromeService oluştur
chrome_options = Options()
chrome_service = Service(chrome_driver_path)

# Selenium WebDriver'ı başlat
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# Web sitesine git
driver.get("https://web.whatsapp.com")

# Bekleme süresi
wait = WebDriverWait(driver, 50)

while True:
    if elements.qr_check(wait):
        break
    else:
        sleep(10)
        continue

sleep(20)
driver.maximize_window()

while True:
    if(limit == counter_step):
        break
    
    # elements.new_message(wait)
    keyboard.search()
    sleep(1)
    keyboard.write(contact_name)
    for _ in range(3):
        keyboard.tab()
        sleep(1/3)
    for _ in range(counter_step):
        keyboard.down()
        sleep(1/3)
    sleep(1/8)
    keyboard.enter()
    sleep(2)
    elements.profile(wait)
    sleep(1)
    numbers+=elements.number(wait).replace(" ", "")+"\n"
    counter_step+=1
print("Tapılan nömrə sayı",len(numbers.split("\n"))-1)
with open("numbers.txt","w") as file:
    file.write(numbers)        
# Tarayıcıyı kapat
print(numbers)
driver.quit()
