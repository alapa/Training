def add_num(book, name, num):
	if name not in book:
		book[name] = num
	else: raise NameError
	
def search_num(book, name):
	if name in book:
		print(book[name])
	else: raise NameError
	
def upd_num(book, name, num):
	if name in book:
		book[name] = num
	else: raise NameError

def del_num(book, name):
	if name in book:
		del book[name]	
	else: raise NameError
	
def show_all(book):
	#if not book:
	for name,num in book:
		print(name + " - " + num)
	#else: raise

book={}

while True:
	action = input("Choose action: add, search, update, delete, all:")
	if action == "add":
		name = input("Enter name:")
		num = input("Enter number:")
		try:
			add_num(book, name, num)
		except NameError:
			print("Name already exist")
	elif action == "search":
		name = input("Enter name:")
		try:
			search_num(book, name)
		except NameError:
			print("No such contact")
	elif action == "update":	
		name = input("Enter name:")
		num = input("Enter number:")
		try:
			upd_num(book, name, num)
		except NameError:
			print("No such contact")
	elif action == "delete":
		name = input("Enter name:")
		try:
			del_num(book, name)
		except NameError:
			print("No such contact")
	elif action == "all":
		#try:
		show_all(book)
		#except:
		#	print("The phonebook is empty")			
	elif action == "q":
		break
	else: 
		print("Wrong action!")	