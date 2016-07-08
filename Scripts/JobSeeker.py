from bs4 import BeautifulSoup
import urllib
import re
from Job import Job

class JobSeeker:

    #Search filters
    city = None
    province = None
    province_wide_search = False
    keywords = set()
    keywords_list = None

    #Jobs found
    job_listings = list()

    def __init__(self, city, province, province_wide_search, *search_terms):

        self.city = city
        self.province = province
        self.province_wide_search = province_wide_search
        self.keywords = set(search_terms)
        self.keywords_list = search_terms

    def extract_job_information(self, jobs):

        for j in jobs:
            re_title = re.compile('rel="nofollow" target="_blank" title=.*">')
            re_url = re.compile('href="/.*/.*amp;fccid=\S*')

            job_title_matches = re_title.findall(j)
            job_url_matches = re_url.findall(j)

            if len(job_title_matches) > 0 and len(job_url_matches) > 0:
                job_title_unfiltered = job_title_matches[0]
                job_url_unfiltered = job_url_matches[0]

                job_title = job_title_unfiltered[38:].replace('"', "").replace('>', "").replace('-', '')
                job_url = "ca.indeed.com" + job_url_unfiltered[5:].replace('"', '')
                job_listing = [job_title, job_url]
                self.job_listings.append(job_listing)
        







    def search(self):

       if len(self.keywords_list) < 1:
           return

       job_titles = self.keywords_list
       indeed_base_url = "http://www.indeed.ca/"
       jobs_found = list()

       #Jobs containing keywords the user inputted
       jobs_filtered = list()

       for job in job_titles:

           search_term = str(job).replace(' ', '-')


           if self.province_wide_search:
               search_term += "-jobs-" + self.province
           else:
               search_term += "-jobs-" + self.city + "," + self.province


           query_url = indeed_base_url + search_term
           search_result_contents = urllib.urlopen(query_url).read()
           bs4 = BeautifulSoup(search_result_contents, "html.parser")

           jobs_found.append(bs4.find_all('div', id=re.compile('p_\w+')))

       #get all the jobs containing the key words
       for job in jobs_found:
           for j in job:
               results = str(j).lower().split("div class=\" row result")
               for r in results:
                   if any(x in r for x in self.keywords):
                       jobs_filtered.append(r)
       self.extract_job_information(jobs_filtered)



























































































