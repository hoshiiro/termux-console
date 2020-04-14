import os
import sys
from datetime import datetime
		
fol = os.getcwd()
wf = fol + "/data"

"""
Date var
"""
dt = datetime.now()
year = str(dt.year)
month = str(dt.month)
day = str(dt.day)

"""
end date var
"""


class note():
	
	def write(self):
		
		self.note_list()
		fnme = input("\n\tSelect file name to write > ")
		f = open("data/"+ year +"-"+ month +"-"+ day +"-"+ fnme +".txt", "a")
		while(1):
			text = input("\tWrite >>> ")
			if text == "/end":
				break
			else:
				f.write(text + "\n")
		f.close()
		
	def file_loc(self):
		
		print("\tThe Note File Located In:\n\t"+ wf)
	
	def clear_note(self):
		
		os.system("rm "+ wf)
		
	def read(self):
		
		self.note_list()
		fnme = input("\n\tInsert note file name (not included the file format) > ")
		f = open(wf +"/"+ year +"-"+ month +"-"+ day +"-"+ fnme +".txt", "r")
		print("\t"+ str(f.read()))
		f.close()
			
	def note_list(self):
		
		f = os.listdir(wf)
		fn = 0
		for file in f:
			fn += 1
		print("\n\tYou have",fn,"note and here the list: ")
		n = 0
		for i in f:
			fi = f[n]
			print("\t\t- "+ fi)
			n += 1
		
	def make(self):
		
		print(os.getcwd())
		fnme = input("\tInsert note file name > ")
		os.system("touch "+ wf +"/"+ year +"-"+ month +"-"+ day +"-"+ fnme +".txt")
		
	def delete(self):
		
		self.note_list()
		fnme = input("\tInsert the note title > ")
		os.system("rm "+ wf +"/"+ year +"-"+ month +"-"+ day +"-"+ fnme +".txt")

n = note()		

info = """
	Note Program By Fikricahyon24
	------------------------
	Don't forget your memories.
	
	---[ insert /help to see command list ]---
"""
about_auth = """
	[ Fikricahyon24 ]
	----------
	
	Just 13 y.o boy from Indonesian.
	Like a playing a game and singing a song.
	Dreaming to wanna be programmer.
	
	Found Me On:
		- Github: Fikricahyon24
		- Facebook: Takahashi Haruki
		- Twitter: @siirius431 
"""
cmd_list = """
	[ Command list ]
	
	- /write : Use to change the prompt from 'note >' to 'write >'.
		   With that you can write now. End with /end command.
	- /read  : Read your note without text editor.
	- /make  : Make a blank note.
	- /list  : print list all your note.
	- /clear : Delete all your note.
	- /rm    : remove your selected note.
"""

print(info)
while(1):
	inp = input("Note > ")
	if inp.lower() == "/help":
		print(cmd_list)
	elif inp.lower() == "/write":
		n.write()
	elif inp.lower() == "/read":
		n.read()
	elif inp.lower() == "/make":
		n.make()
	elif inp.lower() == "/list":
		n.note_list()
	elif inp.lower() == "/clear":
		n.clear()
	elif inp.lower() == "/rm":
		n.delete()
	elif inp.lower() == "/about":
		print(about_auth)
	elif inp.lower() == "exit":
		sys.exit()
	else:
		print("Command Not Found")