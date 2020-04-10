import json
import os

file_json = open("quiz_data.json")
data = json.loads(file_json.read())

q = 0

score = 0
total_q = 0
cor_q = 0

for question in data['question']:
    total_q += 1

m = score + total_q
mark = 100 / (score + total_q)

y = data['yes']
n = data['no']

def quest():

    global score
    global cor_q
    global q
    global y
    global n

    q += 1 
    l = str(q)

    j = input("\n• "+ data['question'][l]['quest'])
    c = data['question'][l]['answer']
    if j.lower() == c.lower():
        print("\t"+ y)
        score += 1
        cor_q += 1
    else: 
        print("\t"+ n)

os.system("figlet Simple Quiz")
print("\tSelamat Datang di "+ data['metadata']['name'] +" • By: "+ data['metadata']['by'])
print("\t———")
play = input("\tMau Main?? [y/n]: ")     
if play.lower() == 'y':    
    for question in data['question']:
        quest()
else:
    print("abort")

sc = cor_q
ic = total_q - cor_q

print("")
if ic == 0:
    print("\tKamu berhasil menjawab semua pertanyaan dengan benar!")
else:
    print("\tKamu berhasil menjawab", sc, "pertanyaan!")
    print("\tTapi salah menjawab", ic,"pertanyaan!")
    
print("\tDengan ini quiz selesai, thanks for playing!\n")