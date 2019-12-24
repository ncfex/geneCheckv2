import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_values(args: tuple) -> str:

    unparsed_html = _get_all_response(args)

    return unparsed_html

def get_response(url, kwords):
    import requests
    try:
        response = requests.post(url, data=kwords, verify=False)
        return response
    except:
        print("=======================HATA====================")
        raise Exception
        print("===============================================")



def get_values_whole(args: tuple) -> str:
    unparsed_html = _get_all_response(args)

    return unparsed_html


def _get_all_response(args: tuple) -> None:

    post_values = {"username": args[0],
                   "password": args[1],
                   "csrfmiddlewaretoken" : args[2]
                   }

    rsno = "rs80357919"

    url = "https://varsome.com/sign-in/?ssologin=1&next=https://varsome.com/"
    response = get_response(url, post_values)

    return response.text


if __name__ == "__main__":

    veri = ('oguzhanguldibi@gmail.com','1597qqqq', 'aOYywXwW4W657XphdObMaGEe42Oc0tv8')

    print(get_values(veri))



