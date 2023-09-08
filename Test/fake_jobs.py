import pandas as pd
import requests
import pandas as ps
from bs4 import BeautifulSoup

response = requests.get("https://realpython.github.io/fake-jobs/")
print(response.status_code)
#print(response.content)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    lista_divs = soup.find_all("div", attrs={"class" : "card-content"})

    data = {"Puesto":[], "Empresa":[], "Ciudad":[], "Fecha":[]}

    for div in lista_divs:
        puesto = div.find("h2",attrs= {"class":"title is-5"})
        company = div.find("h3",attrs= {"class":"subtitle is-6 company"})
        city = div.find("p",attrs = {"class":"location"})
        date = div.find("time")
        data["Puesto"].append(puesto.text)
        data["Empresa"].append(company.text)
        data["Ciudad"].append(city.text.strip())
        data["Fecha"].append(date.text)

        #print(div.prettify())
        """print(puesto.text)
        print(company.text)
        print(city.text.strip())
        print(date.text)"""
        print("\n")

    df_jobs = pd.DataFrame(data)
    df_jobs.to_csv("Jobs.csv")

    #print(lista_divs[0]).prettify()
    #print(soup.head.title.text)
else:
    print(f"Error {response.status_code} al momento de cargar la página")