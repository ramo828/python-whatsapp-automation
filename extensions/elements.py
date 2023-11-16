from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def qr_check(wait):
    try:
        # Profil öğesini bul
        element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#app > div > div > div.landing-window > div.landing-main > div > div > div._2I5ox > div > canvas")))
        print("QR kodu daxil edin.")
        return False
    except:
        print("QR kod doğrulaması geçildi")
        # driver.maximize_window()
        return True
        # sleep(1)


def new_message(wait):
    try:
        # Profil öğesini bul
        element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#app > div > div > div._2Ts6i._3RGKj > header > div._604FD > div > span > div:nth-child(5) > div > span")))
        element.click()
        print("Mesaja girdi")
        return False
    except:
        print("Mesaj baglandi")
        return True

def profile(wait):
    try:
        # Profil öğesini bul
        element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#main > header > div._2au8k > div > div")))
        element.click()
        print("Profile girdi")
        return False
    except:
        print("Profil baglandi")
        return True
    

def number(wait):
    try:
        # Profil öğesini bul
        element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#app > div > div > div._2Ts6i._1xFRo > span > div > span > div > div > section > div.gsqs0kct.oauresqk.efgp0a3n.tio0brup.g0rxnol2.tvf2evcx.oq44ahr5.lb5m6g5c.brac1wpa.lkjmyc96.b8cdf3jl.bcymb0na.myel2vfb.e8k79tju > div.tvf2evcx.m0h2a7mj.lb5m6g5c.j7l1k36l.ktfrpxia.nu7pwgvd.p357zi0d.dnb887gk.gjuq5ydh.i2cterl7.fhf7t426.f8m0rgwh.gndfcl4n > div > span > span")))
        if not element.text:
            element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#app > div > div > div._2Ts6i._1xFRo > span > div > span > div > div > section > div:nth-child(6) > div.gx1rr48f._3VUan > div > div > span > span")))

        print("Profile girdi")
        print(element.text)
        return element.text
    except:
        print("Profil baglandi")
        return ""
