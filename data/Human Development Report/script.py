import os

FILE = "Indicators.csv"

indicator = {}
ID = []

with open(FILE, 'r') as file:
    for line in file:
        colonne = line.rstrip().split(';')
        if colonne[2] == "oui":
            ID.append((colonne[0], colonne[1]))
print(ID)

for id, name in ID:
    command = f"curl \"http://ec2-54-174-131-205.compute-1.amazonaws.com/API/HDRO_API.php/indicator_id={id}\" -H \"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0\" -H \"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8\" -H \"Accept-Language: en-US,en;q=0.5\" --compressed -H \"Prefer: safe\" -H \"Referer: http://ec2-54-174-131-205.compute-1.amazonaws.com/API/Information.php\" -H \"DNT: 1\" -H \"Connection: keep-alive\" -H \"Cookie: PHPSESSID=q79r1h6hif37jrpjubp6npsbg4\" -H \"Upgrade-Insecure-Requests: 1\" -H \"Cache-Control: max-age=0\" > '{name}'.json"
    os.system(command)

