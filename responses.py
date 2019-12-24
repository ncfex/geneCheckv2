import os
import webbrowser
from DataOps import MuTasterValues, PolyPhenValues

'''from DataOps import MuTasterValues, PolyPhenValues
from DataOps.fileOps import read_input

muta = ("", "ENST00000379370", "gDNA", "", "",
         "", "28669", "28672", "")

poly = ("P41567", '', '59', 'L', 'P', '')


name_deneme = "Genesis"


res_mut = MuTasterValues.get_values(muta)
res_poly = PolyPhenValues.get_values(poly)

html = res_mut + "\n\n\n\n" + res_poly

def output_file(html):
    fileName = "Result_all.html"
    f = open(fileName, "a")
    f.write(html)
    f.close()
    return fileName

unparsed_muta = MuTasterValues.get_values_whole(muta)
unparsed_poly = PolyPhenValues.get_values_whole(poly)

unparsed_all = unparsed_muta + unparsed_poly

web_result_page_html = output_file(unparsed_all)'''