def get_values(args: tuple) -> str:

    resp = _get_all_response(args)
    summary_info = _parse_to_summary(resp)
    
    return summary_info

def get_values_whole(args: tuple) -> str:
    unparsed_html = _get_all_response(args)

    return unparsed_html

def get_file(mode: str):
    f = open("ppresponse.html", mode)
    return f
        
def _get_all_response(args: tuple) -> None:

    import bs4, requests
    from DataOps import get_response

    url = "http://genetics.bwh.harvard.edu/cgi-bin/ggi/ggi2.cgi"

    post_values = {
        "_ggi_project" : "PPHWeb2", 
        "_ggi_origin": "query",
        "_ggi_target_submit": "submit",
        "accid" : args[0],
        "seqres": args[1],
        "seqpos" : args[2],
        "seqvar1" : args[3],
        "seqvar2" : args[4],
    }

    response = get_response.get_response(url, post_values)

    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    sid = soup.find("input").get("value")

    link = _get_link(sid)

    s  = requests.session()
    response = s.post(link)

    
    """file = get_file("w")
    file.write(response.text)
    file.close()"""
    
    return response.text

def _refresh(sid: str):
    import requests

    url = "http://genetics.bwh.harvard.edu/cgi-bin/ggi/ggi2.cgi"
    data = {"sid" : sid,
        "sidreset" : "1",
        "delpend" : "4948667",
        "_ggi_project" : "PPHWeb2",
        "_ggi_origin" : "manage",
        "_ggi_target_manage" : "Refresh"
    }


    session = requests.session()
    r = session.post(url, verify=0, data = data)

    return r

def _get_link(sid: str):
    import bs4, time

    response = _refresh(sid)
    i = 0
    
    while (i < 5):
        link = bs4.BeautifulSoup(response.text, 'html.parser').find_all("a")[-2].get("href")
        if  link[0] == '/':
            return "http://genetics.bwh.harvard.edu" + link
        else :
            response = _refresh(sid)
            time.sleep(1)
        i += 1

def _parse_to_summary(unparsed)-> str:

    #unparsed_file = get_file("r")
    import bs4

    soup = bs4.BeautifulSoup(unparsed, "html.parser")
    #unparsed_file.close()

    # table = soup.find("table").find_next_sibling()
    # row = table.find("tr").find_next_sibling()
    # summary = row.find("ul")

    summary = soup.find("table")
    summary = summary.find("tr").find_next_sibling()
    summary = summary.find_all("td")[-1].get_text()
    return summary
    
    
if __name__ == "__main__":
    t = ("P41567", '', '59', 'L', 'P', '')
    print(get_values(t))
