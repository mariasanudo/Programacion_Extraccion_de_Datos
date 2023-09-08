import time

import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By # Queda pendiente
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

# Configuraciones
s = Service(ChromeDriverManager().install())
opc = Options()
opc.add_argument("--window-size = 1020, 1200") # los -- son obligatorios, indican una palabra extensa, se utiliza para determinar la terminal

navegador = webdriver.Chrome(service=s, options=opc)
navegador.get("http://www.olympedia.org/statistics/medal/country")

cmbYear = navegador.find_element(By.NAME,"edition_id")
cmbGender = navegador.find_element(By.NAME,"athlete_gender")

genderOptios = cmbGender.find_elements(By.TAG_NAME, "option")
print(genderOptios[0].text)
print(genderOptios[1].text)
print(genderOptios[2].text)

yearGroups = cmbYear.find_elements(By.TAG_NAME, "optgroup")
year_list = yearGroups[0].find_elements(By.TAG_NAME, "option")

datos = {
    "country":[],
    "year":[],
    "gender":[],
    "gold":[],
    "silver":[],
    "bronze":[],
    "total":[],
}

"""
soup = BeautifulSoup(navegador.page_source, "html.parser")
#print(soup)
#print(soup.prettify())
table = soup.find("table", attrs={"class":"table table-striped"})
print(table.prettify)
"""

for gender in genderOptios[1:]:
    gender.click()
for year in year_list:
    year.click()
time.sleep(1)

soup = BeautifulSoup(navegador.page_source, "html.parser")
table = soup.find("table", attrs={"class": "table table-striped"})
list_rows = table.find_all("tr")

for row in list_rows[1:]:
    datos["gender"].append(gender.text)
    datos["year"].append(year.text)
    values = row.find_all("td")
    datos["country"].append(values[0].text)
    datos["gold"].append(values[2].text)
    datos["silver"].append(values[3].text)
    datos["bronze"].append(values[4].text)
    datos["total"].append(values[5].text)

#print(datos)
df_olimpiadas= pd.DataFrame(datos)
df_olimpiadas.to_csv("data_oilimpiadas.csv")
print(df_olimpiadas)
# time.sleep(5) # deja abierta la ventana por el tiempo indicado
navegador.close()
