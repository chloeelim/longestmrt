import requests
import json
import csv
from bs4 import BeautifulSoup


def scrape_data():
    data = []

    for i in range(1, 97):
        response = requests.get(
            f"https://developers.onemap.sg/commonapi/search?searchVal=mrt%20station&returnGeom=Y&getAddrDetails=Y&pageNum={i}")
        data += response.json()['results']

    with open("mrt.json", 'w') as f:
        json.dump(data, f, indent=4)


def clean_data():
    inside = set()
    data = []
    with open("mrt.json") as f:
        file_data = json.load(f)
        for stuff in file_data:
            if stuff['BUILDING'] not in inside:
                inside.add(stuff['BUILDING'])
                data.append(stuff)
    with open("unique_mrt.json", 'w') as f:
        json.dump(data, f, indent=4)


def parse_table():
    data = []
    with open("table.html") as f:
        soup = BeautifulSoup(f)
        for tr in soup.find_all("tr"):
            values = [td.string for td in tr.find_all("td")]
            data.append(values)
    with open("data.csv", 'w') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerows(data)


def craft_adj_list():
    stations = {}
    with open("data.csv") as f:
        data = list(csv.reader(f))
        for code, name, _, _ in data[1:]:
            stations[code] = {"name": name, "edges": []}

        station_codes = list(stations.keys())
        temp = []
        for codes in station_codes:
            for code in codes.split():
                temp.append(code)

        station_codes_flattened = temp
        for codes, station_data in stations.items():
            try:
                for code in codes.split(" "):
                    line = code[:2]
                    number = int(code[2:])
                    prev = [int(c[2:]) if c[2:] else 0
                            for c in station_codes_flattened if line in c and int(c[2:]) < number]
                    if prev:
                        target = f"{line}{max(prev)}"
                        station_data['edges'].append(
                            [code for code in station_codes if target in code][0] if max(prev) else [code for code in station_codes if line in code][0])

                    next = [int(c[2:]) if c[2:] else 0 for c in station_codes_flattened if c.startswith(
                        line) and int(c[2:]) > number]
                    if next:
                        target = f"{line}{min(next)}"
                        station_data['edges'].append(
                            [code for code in station_codes if target in code][0])
            except:
                print("stupid mrt:", code)

        with open("adj.json", 'w') as f:
            json.dump(stations, f, indent=4)


# scrape_data()
# clean_data()
# parse_table()
craft_adj_list()
