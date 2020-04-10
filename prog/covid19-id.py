import urllib.request
import json
import os

url = "https://kawalcovid19.harippe.id/api/summary"
result = urllib.request.urlopen(url)
data = json.loads(result.read())

confirmed = data['confirmed']['value']
recovered = data['recovered']['value']
death = data['deaths']['value']
care = data['activeCare']['value']

os.system("figlet Covid-19")
print("\n\tLokasi: Indonesia")
print("———")
print("Kasus Terkonfirmasi: ",confirmed)
print("Sembuh: ",recovered)
print("Meninggal: ",death)
print("Dalam Perawatan: ",care)
print("")