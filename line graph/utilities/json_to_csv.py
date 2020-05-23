import csv
import json

#f = open("C-B0024-002.json", encoding='utf-8')
#j = json.load(f)
#f.close()

csv_format = ['time', 'pressure', 'temperature', 'humidity', 'wind speed', 'wind direction', 'precipitation']


def ele_to_list(element, order):
    d = element[order]
    dd = element[order]['weatherElement']
    l = [d['obsTime'], dd[0]['elementValue']['value'],dd[1]['elementValue']['value'],dd[2]['elementValue']['value'], \
        dd[3]['elementValue']['value'],dd[4]['elementValue']['value'].split(',')[1],dd[5]['elementValue']['value']]
    #print(l)
    return l


for i in range(len(j["cwbopendata"]["dataset"]["location"])):

    location = j["cwbopendata"]["dataset"]["location"][i]
    name = location['locationName']
    element = location["weatherElement"][0]['time']

    fc = open(f"{name}.csv", "w", newline='')
    writer = csv.writer(fc)
    writer.writerow(csv_format)
    for i in range(len(element)):
        writer.writerow(ele_to_list(element, i))
    fc.close()
