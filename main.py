from bs4 import BeautifulSoup
import requests
from datetime import date


url = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation='

timestamp = date.today()

main_sauce = requests.get(url).text
sauce = BeautifulSoup(main_sauce, 'lxml')

all_job = sauce.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')

for index, job in enumerate(all_job):
    job_count = sauce.find('header', class_ = 'srp-header clearfix')
    job_found = job_count.h1.span.text
    comp_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ','')
    exp = job.ul.li.text[11:]
    jd = job.find('ul', class_ = 'list-job-dtl clearfix')
    job_desc = jd.li.text
    skills = job.find('span', class_ = 'srp-skills').text.replace(' ','')
    posted_date = job.find('span', class_ = 'sim-posted').span.text
    more_info = job.header.h2.a['href']
    with open(f'Info\InfofileNo{index}_{timestamp}.txt', 'w') as info_file:
        info_file.write(f"Total Job : {job_found} \n")
        info_file.write(f"Company Name : {comp_name.strip()}\n")
        info_file.write(f"Required Experience : {exp}\n")
        info_file.write(f"{job_desc.strip()}\n")
        info_file.write(f"Required Skills : {skills.strip()}\n")
        info_file.write(f"Posted Date : {posted_date.strip()}\n")
        info_file.write(f"More Information : {more_info}\n")

