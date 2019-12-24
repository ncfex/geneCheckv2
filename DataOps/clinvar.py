import time

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import requests
from bs4 import BeautifulSoup

class Clinvar:
    def get_response_clinvar(self, url):
        try:
            response = requests.post(url, verify=False)
            return response
        except:
            print("=======================HATA====================")
            raise Exception
            print("===============================================")


    def _get_all_response(self) -> None:
        rsNo1 = 'rs11571833'
        url = 'https://www.ncbi.nlm.nih.gov/clinvar/?term=' + rsNo1
        time.sleep(0.5)
        response = self.get_response_clinvar(url)

        return response.content

    def parse_clinvar(self):

        soup = BeautifulSoup(self._get_all_response(), 'html.parser')
        interp = soup.findChildren('dd', class_='bold margin-bottom')
        clinvar_predict = interp[0].text

        return clinvar_predict



