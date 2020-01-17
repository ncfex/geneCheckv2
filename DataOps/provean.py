import time

import urllib3
from bs4 import BeautifulSoup
from DataOps import get_response
import requests

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class Provean:

    provean_input = '17,41249386,T,C'
    provean_response = "none"

    #TO GET JOB ID
    def create_job_id_response(self):
        post_values = {"CHR" : self.provean_input,
                       "table" : "human37_66"
                       }
        url = 'http://provean.jcvi.org/genome_prg_2.php'
        response = get_response.get_response(url, post_values)

        return response.content

    def parse_jobID(self):
        soup = BeautifulSoup(self.create_job_id_response(), 'html.parser')
        interp = soup.find_all('p')
        id_without_split = interp[1].text
        jobid_ver1 = id_without_split.split(": ")
        jobid_ver2 = jobid_ver1[1].split(").")
        jobID = jobid_ver2[0]
        return jobID

    #TO GET ACTUAL DATA
    def get_response_with_jobID(self):
        url = 'http://provean.jcvi.org/genome_view_table_2.php?jobid=' + self.parse_jobID()
        time.sleep(5)
        response = self.request_with_jobID(url)

        return response.content

    def request_with_jobID(self, url):
        try:
            response = requests.post(url)
            return response
        except:
            print("=======================HATA====================")
            raise Exception
            print("===============================================")


    def parse_PROV_Score(self):

        soup = BeautifulSoup(self.get_response_with_jobID(), 'html.parser')
        interp = soup.find_all("td")
        prov_score = interp[34].text

        return prov_score

    def parse_PROV_Predic(self):

        soup = BeautifulSoup(self.get_response_with_jobID(), 'html.parser')
        interp = soup.find_all("td")
        prov_predic = interp[35].text

        return prov_predic

    def parse_SIFT_Score(self):

        soup = BeautifulSoup(self.get_response_with_jobID(), 'html.parser')
        interp = soup.find_all("td")
        sift_score = interp[38].text

        return sift_score

    def parse_SIFT_Predic(self):

        soup = BeautifulSoup(self.get_response_with_jobID(), 'html.parser')
        interp = soup.find_all("td")
        sift_predic = interp[39].text

        return sift_predic


