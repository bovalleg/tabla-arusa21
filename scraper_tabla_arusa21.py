import requests
from bs4 import BeautifulSoup
import json

URL = "https://arusa.cl/es/tournament/1304838/ranking/3595238"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

rows = soup.select(".table-responsive table tbody tr")
data = []

for row in rows:
    cols = row.find_all("td")
    if len(cols) < 11:
        continue

    posicion = cols[1].get_text(strip=True)
    nombre_raw = cols[2].get_text(strip=True)
    escudo = cols[2].find("img")["src"] if cols[2].find("img") else ""

    equipo = {
        "posicion": int(posicion),
        "nombre": nombre_raw,
        "escudo": escudo,
        "puntos": cols[3].get_text(strip=True),
        "pj": cols[4].get_text(strip=True),
        "pg": cols[5].get_text(strip=True),
        "pe": cols[6].get_text(strip=True),
        "pp": cols[7].get_text(strip=True),
        "f": cols[8].get_text(strip=True),
        "c": cols[9].get_text(strip=True),
        "dif": cols[10].get_text(strip=True)
    }
    data.append(equipo)

with open("tabla_arusa.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("Tabla guardada en tabla_arusa.json")
