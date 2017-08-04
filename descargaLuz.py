import urllib.request
import urllib.error
import json

year = 2014
month = 4

url_str = "https://api.esios.ree.es/archives/70/download_json?locale=es&date="
line_gen = ""
line_noc = ""

while True:
    for i in range(1, 32):
        if i < 10:
            url_str_tmp = url_str + str(year) + "-" + str(month) + "-" + "0" + str(i)
        else:
            url_str_tmp = url_str + str(year) + "-" + str(month) + "-" + str(i)
        try:
            with urllib.request.urlopen(url_str_tmp) as url:
                data = json.loads(url.read().decode())
                for hour in data["PVPC"]:
                    line_gen += str(float(hour["GEN"].replace(",", ".")) / 1000) + ";"
                    line_noc += str(float(hour["NOC"].replace(",", ".")) / 1000) + ";"
                line_gen += "\n"
                line_noc += "\n"
            print("Readed day " + str(i) + " of month " + str(month) + " of year " + str(year))
        except urllib.error.HTTPError as err:
            continue
    text_file_gen = open(str(year) + "-" + str(month) + "-GEN.csv", "w")
    text_file_gen.write(line_gen)
    text_file_gen.close()
    text_file_noc = open(str(year) + "-" + str(month) + "-NOC.csv", "w")
    text_file_noc.write(line_noc)
    text_file_noc.close()
    line_gen = ""
    line_noc = ""
    month += 1
    if month == 13:
        year += 1
        month = 1
