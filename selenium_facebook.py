import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By # Queda pendiente
from webdriver_manager.chrome import ChromeDriverManager

# Configuraciones
s = Service(ChromeDriverManager().install())
opc = Options()
opc.add_argument("--window-size = 1020, 1200") # los -- son obligatorios, indican una palabra extensa, se utiliza para determinar la terminal

navegador = webdriver.Chrome(service=s, options=opc)
navegador.get("https://es-la.facebook.com/")

txt_email = navegador.find_element(By.ID, "email")
txt_email.send_keys("usuario@gmail.com")
time.sleep(2)

txt_password = navegador.find_element(By.ID, "pass")
txt_password.send_keys("*****************")
time.sleep(2)

navegador.save_screenshot("img_test.png")

btnlogin = navegador.find_element(By.NAME, "login")
btnlogin.click()

print(navegador.title)

time.sleep(5) # deja abierta la ventana por el tiempo indicado