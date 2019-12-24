def get_values(args: tuple) -> str:

    unparsed_html = _get_all_response(args)
    summary_info = _parse_to_summary(unparsed_html)
    
    return summary_info


def get_values_whole(args: tuple) -> str:
    unparsed_html = _get_all_response(args)

    return unparsed_html

def _get_all_response(args: tuple) -> None:

    from DataOps import get_response

    post_values = {"gene": args[0],
                   "transcript_stable_id_text": args[1],
                   "sequence_type": args[2],
                   "sequence_snippet": args[3],
                   "position_be": args[4],
                   "new_base": args[5],
                   "start_insdel": args[6],
                   "end_insdel": args[7],
                   "bases_inserted": args[8]
    }
    

    url = "http://www.mutationtaster.org/cgi-bin/MutationTaster/MutationTaster69.cgi"
    response = get_response.get_response(url, post_values)

    return response.text
    
    #file = get_file("w")
    #file.write(response.text)
    #file.close()

    

def _parse_to_summary(unparsed:str)-> str:
    
    # unparsed_file = get_file("r")
    import bs4

    soup = bs4.BeautifulSoup(unparsed, "html.parser")
    # unparsed_file.close()

    # table = soup.find("table").find_next_sibling()
    # row = table.find("tr").find_next_sibling()
    # summary = row.find("ul")

    summary = soup.find("ul").get_text()
    return summary
    
    
if __name__ == "__main__":
    t = ("", "ENST00000379370", "gDNA", "", "",
         "", "28669", "28672", "")
    print(get_values(t))


    
