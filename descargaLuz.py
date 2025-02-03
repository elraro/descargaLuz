import urllib.request
import urllib.error
import json

year = 2024
month = 1

url_str = "https://api.esios.ree.es/archives/70/download_json?locale=es&date="
line_pcb = ""

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
                    line_pcb += str(float(hour["PCB"].replace(",", ".")) / 1000) + ";"
                line_pcb += "\n"
            print("Readed day " + str(i) + " of month " + str(month) + " of year " + str(year))
        except urllib.error.HTTPError as err:
            continue
    text_file_pcb = open(str(year) + "-" + str(month) + "-PCB.csv", "w")
    text_file_pcb.write(line_pcb)
    text_file_pcb.close()
    line_pcb = ""
    month += 1
    if month == 13:
        year += 1
        month = 1
