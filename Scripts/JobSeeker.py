from bs4 import BeautifulSoup
import urllib
import re

class JobSeeker:

    #Search filters
    city = None
    province = None
    province_wide_search = False
    keywords = set()
    keywords_list = None

    def __init__(self, city, province, province_wide_search, *search_terms):

        self.city = city
        self.province = province
        self.province_wide_search = province_wide_search
        self.keywords = set(search_terms)
        self.keywords_list = search_terms

    def search(self):

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
               results = str(j).lower().split("<div class=\"notes-container result-tab\">"
                                              "</div>\n</div>\n</td>\n</tr>\n</table>\n</div>]]")
               for r in results:
                   if any(x in r for x in self.keywords):
                       jobs_filtered.append(r)

















































































