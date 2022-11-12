from requests import get
from bs4 import BeautifulSoup
from extracy.jobb import extractor_job

keyword = input("what do you want to search for?")
job= extractor_job(keyword)
jobs = job

file = open(f"{keyword}.csv", "w")
file.write("Company, Location, Exp, Edu, URL\n")

for job in jobs:
  file.write(f"{job['company']},{job['location']},{job['exp']},{job['edu']},{job['site']}\n ")
file.close()