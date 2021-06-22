from bs4 import BeautifulSoup
from urllib.request import urlopen
from task1 import GetDetails
import csv

url = "https://www.espncricinfo.com/series/ipl-2019-1165643/match-results"
url_contents = urlopen(url).read()
soup = BeautifulSoup(url_contents, "html.parser", )
matches = soup.find_all("a", {"class": "match-info-link-FIXTURES"})

all_rows = []
for match in matches:
    href = match['href']
    match_id = href[-22:-15]
    rows = GetDetails(match_id, False)
    all_rows = all_rows + rows

keys = all_rows[0].keys()


with open(f'matches.csv', 'w', newline="") as file:
    dict_writer = csv.DictWriter(file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(all_rows)
