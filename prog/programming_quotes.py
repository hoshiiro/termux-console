import urllib.request
import json

url = "https://programming-quotes-api.herokuapp.com/quotes/random/lang/en"
result = urllib.request.urlopen(url)
data =  json.loads(result.read())

text = data['en']
author = data['author']

print("\t"+ text +"\n\t— "+ author)