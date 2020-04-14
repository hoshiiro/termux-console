import json
import sys

file = open("data_quiz.json")
data = json.loads(file.read())

score = 0

gr = "—–———"

class game:	

	def question(self, tipe, number):
		
		self.tipe =  tipe
		self.number = number
		self.num = str(self.number)
		
	def total_quest(self, tipe):
		
		t_q = 0
		self.tipe = tipe
		
		for question in data['question'][self.tipe]:
			t_q += 1
			
		print("Kamu memilih pertanyaan tipe "+ type +" yang memiliki:", t_q,"pertanyaan")
	
	def checkker(self):
		
		global score
		
		per = input("\n\t - "+ data['question'][self.tipe][self.num]['quest']+ ': ')
		j = data['question'][self.tipe][self.num]['answer']
		if per.lower() == j.lower():
			score += 1
			print("\n\t"+ data['yes'])
		else:
			score -= 1
			print("\n\t"+ data['no'])
		 
# main program
prog = game()

print("Hai! Selamat datang di simple quiz!")		
type = input("Sebelum itu masukan Tipe Pertanyaan [serius/lucu]: ")

nm = 1
tq = 0

prog.total_quest(type)

for question in data['question'][type]:
	tq += 1

def p():
	
	global type, nm, prog, tq, gr
	
	for question in data['question'][type]:
		prog.question(type,nm)
		prog.checkker()
		nm += 1
				
	if score == tq:
		print("\n\t"+ gr)
		print("\tSelamat! Kamu berhasil menjawab semua pertanyaan!")
		print("\t"+ gr)
	elif score >= 0 and score < tq:
		print("\n\t"+ gr)
		print("\t Ayo coba lagi!")
		print("\t"+ gr)
	else:
		print("\n\t"+ gr)
		print("\tWah, kamu masih belum bisa menjawab semua pertanyaan. Tapi tetap semangat!")
		print("\t"+ gr)

def l():
	global score, nm, tq, type
	
	if nm < tq:
		p()
	else: 
		pr = input("\n\tMain Lagi? [y/n]: ")
		if pr.lower() == 'y':
			nm = 1
			score = 0
			p()
		elif pr.lower() == 'n':
			print("\tExit Program / Thanks for playing!")
			sys.exit()
		else:
			print("\tOption not found, please write Y or N")
			
while(1):
	l()