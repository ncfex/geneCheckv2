def get_response(url, kwords):
    import requests
    try:
        response = requests.post(url, data=kwords, verify=False)
        return response
    except:
        print("=======================HATA====================")
        raise Exception
        print("===============================================")
