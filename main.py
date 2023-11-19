from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from extensions import elements, keyboard, time_settings

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
wait = WebDriverWait(driver, time_settings.timeout)

while True:
    if elements.qr_check(wait):
        break
    else:
        sleep(time_settings.access_loop)
        continue

sleep(time_settings.start_time)
driver.maximize_window()

while True:
    if(limit == counter_step):
        break
    # elements.new_message(wait)
    keyboard.search()
    sleep(time_settings.search_bf)
    keyboard.write(contact_name,time_settings.write_speed)
    for _ in range(3):
        keyboard.tab()
        sleep(time_settings.tab_time)
    for _ in range(counter_step):
        keyboard.down()
        sleep(time_settings.step_time)
    sleep(time_settings.contact_select_time)
    keyboard.enter()
    sleep(time_settings.profile_load_time)
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
