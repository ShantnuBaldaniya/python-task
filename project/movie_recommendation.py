import requests
from bs4 import BeautifulSoup

#genre = input("Enter genre: ").lower()
url="https://www.merriam-webster.com/dictionary/page"
res=requests.get(url)
print(res.content)
soup=BeautifulSoup(res.text,"html.parser")
m=soup.find_all('span')
print(soup.prettify)
tag = soup.find_all("span", class_="dtText")
t=soup.find_all("div" ,class_="sb-1 sb-entry")
for i in t:
    
    print(i.text)
    
    <button class="ipc-btn ipc-btn--single-padding ipc-btn--center-align-content ipc-btn--default-height ipc-btn--core-base ipc-btn--theme-base ipc-btn--button-radius ipc-btn--on-accent2 ipc-text-button ipc-see-more__button" tabindex="0" aria-disabled="false"><span class="ipc-btn__text"><span class="ipc-see-more__text">50 more</span>
    </span><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" class="ipc-icon ipc-icon--expand-more ipc-btn__icon ipc-btn__icon--post" viewBox="0 0 24 24" fill="currentColor" role="presentation">
    <path opacity=".87" fill="none" d="M24 24H0V0h24v24z"></path><path d="M15.88 9.29L12 13.17 8.12 9.29a.996.996 0 1 0-1.41 1.41l4.59 4.59c.39.39 1.02.39 1.41 0l4.59-4.59a.996.996 0 0 0 0-1.41c-.39-.38-1.03-.39-1.42 0z"></path></svg></button>