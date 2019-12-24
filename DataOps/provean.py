import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def get_values(args: tuple) -> str:
    unparsed_html = _get_all_response(args)

    return unparsed_html


def get_response_withID(url):
    import requests
    try:
        response = requests.post(url)
        return response
    except:
        print("=======================HATA====================")
        raise Exception
        print("===============================================")


#TO GET JOB ID
def _get_all_response(args: tuple) -> None:
    from DataOps import get_response

    post_values = {"CHR" : args[0],
                   "table" : "human37_66"
                   }

    url = 'http://provean.jcvi.org/genome_prg_2.php'


    response = get_response.get_response(url, post_values)

    return response.text


#TO GET ACTUAL DATA
def _get_all_response_jobID():
    jobid = '165053663620446'
    url = 'http://provean.jcvi.org/genome_view_table_2.php?jobid=' + jobid


    response = get_response_withID(url)

    return response.text

if __name__ == "__main__":

    rsNo = '22,30163533,A,C'
    jobid = '1395093392530011'

    #print(get_values(rsNo))
    provean_sonuc = _get_all_response_jobID()

