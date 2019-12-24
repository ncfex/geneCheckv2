import urllib3
from bs4 import BeautifulSoup

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import requests

class gnomAD:
    gnomad_input = 'rs11571833'

    def request_gnomad(self, url):
        try:
            response = requests.get(url, verify=False)
            return response
        except:
            print("=======================HATA====================")
            raise Exception
            print("===============================================")

    def get_response(self):

        url = 'https://gnomad.broadinstitute.org/variant/'+ self.gnomad_input +'?dataset=gnomad_r2_1'
        response = self.request_gnomad(url)

        return response.content

    def parse_gnomAD(self):
        soup = BeautifulSoup(self.get_response(), 'html.parser')
        print(soup.prettify())
        #prov_score = interp[34].text

g1 = gnomAD()
g1.parse_gnomAD()


