import urllib.request
import json
from datetime import datetime

url = "https://api.covid19api.com/summary"
result = urllib.request.urlopen(url)
data = json.loads(result.read())

country_nm = []
l = 0
for countries in data['Countries']:
	country_nm.append(data['Countries'][l]['Country'])
	l += 1

class cov19:
	
	def cn_ls():
		
		cn = 0
		print("")
		for country in country_nm:
			print("\t",cn,": "+ country_nm[cn])
			cn += 1
		print("")
			
	def cn_dtl():
		
		tc = data['Countries'][cn_iln]['TotalConfirmed']
		nc = data['Countries'][cn_iln]['NewConfirmed']
		tr = data['Countries'][cn_iln]['TotalRecovered']
		nr = data['Countries'][cn_iln]['NewRecovered']
		td = data['Countries'][cn_iln]['TotalDeaths']
		nd = data['Countries'][cn_iln]['NewDeaths']
		
		d = data['Countries'][cn_iln]['Date']
		dttm = d.split("T")
		dttm_dt = dttm[0].split("-")
		dttm_tm = dttm[1].split(":")
		
		dt_year = dttm_dt[0]
		dt_month = dttm_dt[1]
		dt_day = dttm_dt[2]
		
		tm_hour = dttm_tm[0]
		tm_min = dttm_tm[1]
		tm_sec = dttm_tm[2]
		
		date = dt_day +"-"+ dt_month +"-"+ dt_year
		time = tm_hour +":"+ tm_min +":"+ tm_sec
		
		print("\n\t "+ country_nm[cn_iln])
		print("\t ----------------")
		print("\t Total Confirmed : ", tc)
		print("\t Total Recovered : ", tr)
		print("\t Total Deaths    : ", td)
		print("\t -[ New ]--------")
		print("\t New Confirmed   : ", nc)
		print("\t New Recovered   : ", nr)
		print("\t New Deaths      : ", nd)
		print("\t ----------------")
		print("\t Last Updated    : ",date, time.replace('Z', ''))
		
	def glo_dtl():
		
		tc = data['Global']['TotalConfirmed']
		nc = data['Global']['NewConfirmed']
		tr = data['Global']['TotalRecovered']
		nr = data['Global']['NewRecovered']
		td = data['Global']['TotalDeaths']
		nd = data['Global']['NewDeaths']
		
		print("\n\t Global")
		print("\t ----------------")
		print("\t Total Confirmed : ", tc)
		print("\t Total Recovered : ", tr)
		print("\t Total Deaths    : ", td)
		print("\t -[ New ]--------")
		print("\t New Confirmed   : ", nc)
		print("\t New Recovered   : ", nr)
		print("\t New Deaths      : ", nd)
		print("\t ----------------")
		
	def help():
		
		help = """
\t How to use
\t ----------
		
\t Insert country name to prompt to see total cases,
\t death and recovered.
\t Use capitalize in first country character name.
		
\t Command Available
\t -----------------
		
\t help          - Print this text.
\t country list  - Print all infected Covid-19 country name.
\t global        - Print global cases, death and recovered.
		
\t By Fikricahyon24
\t ----------------
\t Found me on:
\t \tFacebook  : Takahashi Haruki
\t \tGithub    : Fikricahyon24
\t \tTwitter   : @siirius431
		"""
		
		print(help)
		
text = """
\t Covid-19 Info | Countries And Global
\t -------------- ---------------------
			
\t Use API From https://api.covid19api.com
\t Repository:
\t https://github.io/Fikricahyon24/termux-console/prog/covid-19_tracking.py	
"""
		
print(text)
while(1):
	i = input("\t Covid-19@Info: ")
	if i.lower() == "country list":
		cov19.cn_ls()
	elif i.lower() == "global":
		cov19.glo_dtl()
		print("")
	elif i in country_nm:
		index = country_nm.index(str(i))
		cn_iln = int(index)
		cov19.cn_dtl()
		print("")
	elif i.lower() == "help":
		cov19.help()
	else:
		print("\n\t Oops, command not found.")
		print("\t Try to use help command to print help text\n")