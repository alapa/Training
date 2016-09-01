def exec_action (action, **kwargs):
    actions.get(action,wrong_action)(**kwargs)
    
def add_num(name):
    if name not in book:        
        book[name] = enter_number()
    else: raise NameError
    
def search_num(name):
    if name in book:
        print(book[name])
    else: raise NameError
    
def upd_num(name):
    if name in book:        
        book[name] = enter_number()
    else: raise NameError

def del_num(name):
    if name in book:
        del book[name]    
    else: raise NameError
    
def show_all():
    if book:
        for name,num in book.items():
            print(name + " - " + num)
    else: raise
    
def enter_number():
    return input("Enter number:")
    
def wrong_action():
    print("Incorrect action!")
    
book={}
actions={'a':add_num,'s':search_num,'u':upd_num,'d':del_num, 'all':show_all}

while True:
    action = input("Choose action: a, s, u, d, all:")
    if action == "all":
        exec_action(action)            
    elif action == "q":
        break
    elif action in actions:
        n = input("Enter name:")
        exec_action(action,name=n)
    else: exec_action(action)
  