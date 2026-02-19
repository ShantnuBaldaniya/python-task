import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv
api_key = "3eef399b"

genres=input("Enter the genre like (comedy , action, drama) :-").lower()

print(" ")
industries=input("-----choose the industry type----- \n 1.Hollywood \n 2.Bollywood \n Enter 1/2 :")


if industries=="1":
    company='US'
    print('-U select Hollywood- ')   
else:
    company='IN '
    print('-U select Bollywood- ')
    
    
print(" ")   
title=input('-----enter the content type----- \n choose the \n 1.Movie \n 2.tv-series \n Enter 1/2 :')

if title=="1":
    title_type='feature'
    print('-U select Movie-')
else:
    title_type='tv_series'
    print(' -U select web series-')

print("loading...")
driver = webdriver.Chrome()
url=f"https://www.imdb.com/search/title/?title_type={title_type}&genres={genres}&countries={company}"
driver.get(url)

#esponse=requests.get(driver)
#soup=BeautifulSoup(response.text,"html.parser")
from selenium.webdriver.common.by import By
time.sleep(10)
for i in range(2):
    button = driver.find_element(By.CSS_SELECTOR, "button.ipc-see-more__button")
    driver.execute_script("arguments[0].scrollIntoView();", button)
    driver.execute_script("arguments[0].click();", button)
    time.sleep(2)
    
movies = driver.find_elements(By.CLASS_NAME, "ipc-title__text")

if title=="1":
    duration=driver.find_elements(By.CSS_SELECTOR,"span.dli-title-metadata-item ")
    
   
    durations=[]   
    for item in duration:
        d=item.text
        
        if "h" in d and "m" in d:
            durations.append(item.text)
            
    data=[]
    for i in range(len(durations)):
            data.append(["movie name :"+ movies[i].text + "\n duration:"+ durations[i] +"\n    "])


else :
    data=[]
    for i in range(len(movies)):
        se_name=movies[i].text
        s_name=''
        
        for ch in se_name:
            if ch=="." or ch.isdigit() :
                continue
            else:
                s_name+=ch
                
        s_name = s_name.strip()
            
        api = f"http://www.omdbapi.com/?t={s_name}&type=series&apikey={api_key}"
        res = requests.get(api)
        series = res.json() 
       
        seasons = series.get("totalSeasons", "N/A")
       
        runtime = series.get("Runtime", "N/A")

        data.append(["series: " + s_name +"\n  no of seasons: " + seasons +"\n episode: " + runtime + "\n   "])          

with open("movie.csv", "w",newline="", encoding="utf-8") as file:
    write=csv.writer(file)
    write.writerows(data)
driver.close()



