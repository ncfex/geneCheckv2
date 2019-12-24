import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_values() -> str:
    unparsed_html = _get_all_response()

    return unparsed_html

def get_response_gnomad(url):
    import requests
    try:
        response = requests.get(url, verify=False)
        return response
    except:
        print("=======================HATA====================")
        raise Exception
        print("===============================================")

def _get_all_response() -> None:

    gnomad_data = '13-32906729-A-C'
    url = 'https://gnomad.broadinstitute.org/variant/'+ gnomad_data +'?dataset=gnomad_r2_1'
    response = get_response_gnomad(url)

    return response.text

if __name__ == "__main__":

    gnomad_data = '13-32906729-A-C'

    gnomad_sonuc = get_values()




