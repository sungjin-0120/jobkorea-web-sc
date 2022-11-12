from requests import get
from bs4 import BeautifulSoup

def get_page_count(term):
  base_url = "https://www.jobkorea.co.kr/Search/?stext="
  response = get(f"{base_url}{term}")
  if response.status_code != 200:
    print("can't request website")
  else: 
    soup=BeautifulSoup(response.text,"html.parser")
    tplPagination=soup.find("div", class_="tplPagination newVer wide")
    ul=tplPagination.find("ul")
    if ul == None:
      return 1
    li=ul.find_all("li", reculsive=False)
    count=len(li)
    if count >= 5:
      return 5
    else:
      return count

    

def extractor_job(term):  
  results=[]
  pages = get_page_count(term)
  print("Found", pages, "pages")
  for page in range(pages):
    base_url = "https://www.jobkorea.co.kr"
    final_url= f"{base_url}/Search/?stext={term}&Page_No={page*1}"
    print("requesting,",final_url)
    response = get(final_url)
    
    soup = BeautifulSoup(response.text,"html.parser")
    jobs = soup.find('div', class_="list-default")
    fuck = jobs.find('ul', class_="clear")
    sibbals = fuck.find_all('li', class_="list-post")
    for sibbal in sibbals:
          sucks = sibbal.find_all('div', class_="post")
          for suck in sucks:
            posts = suck.find('div', class_="post-list-corp")
            link=posts.find('a')
            site=link["href"]
            infos= suck.find('div',class_="post-list-info")
            option=infos.find('p', class_="option")
            exp=option.find('span', class_="exp")
            edu=option.find('span', class_="edu")
            loc_long=option.find('span', class_="loc long")
            job_data={
                'company':link.string,
                'site':f"https://www.jobkorea.co.kr{site}",
                'exp': exp.string.replace(","," "),
                'edu':edu.string.replace(","," "),
                'location':loc_long.string.replace(","," ")
                }
            results.append(job_data)
  return results

