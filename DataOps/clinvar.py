import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_response_clinvar(url):
    import requests
    try:
        response = requests.post(url, verify=False)
        return response
    except:
        print("=======================HATA====================")
        raise Exception
        print("===============================================")


def get_values() -> str:
    unparsed_html = _get_all_response()

    return unparsed_html


def _get_all_response() -> None:
    rsNo1 = 'rs11571833'
    url = 'https://www.ncbi.nlm.nih.gov/clinvar/?term=' + rsNo1

    response = get_response_clinvar(url)

    return response.text



if __name__ == "__main__":

    rsNo = 'rs80357919'
    rsNo1 = 'rs11571833'
    rsNo2 = 'rs1135401872'
    rsNo3 = 'rs398122618'

    clinvar_sonuc = get_values()

