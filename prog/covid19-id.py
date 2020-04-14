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

print("\n\tUpdate Covid-19 di Indonesia")
print("\t———")
print("\tKasus Terkonfirmasi: ",confirmed)
print("\tSembuh: ",recovered)
print("\tMeninggal: ",death)
print("\tDalam Perawatan: ",care)
print("")