import pickle
import sys

class PhoneBookError(Exception):
    pass

class Contact():
    def __init__(self, name, number):
        self.name = name
        self.number = number
    def __eq__(self, other):
        return self.name == other.name
    def __hash__(self):
        return hash(self.name)
    """def __setattr__(self, attrname, value):
        if attrname == 'name':
            raise AttributeError("Name can't be changed")"""
    def __repr__(self):
        return "{} - {}".format(self.name,self.number)
    
class PhoneBook():
    def __init__(self):
        self._contacts = set()
        
    def __repr__(self):        
        return '\n'.join(cont.__repr__() for cont in self._contacts)
      
    def load_data(self, file):
        with open(file, 'r+b') as phonebook_file:
            self._contacts = pickle.load(phonebook_file)._contacts            
            
    def enter_contact_info(f):
        def wrapper(self, **kwargs):
            n = input("Enter name:")
            num = input("Enter number:")
            res = f(self, Contact(n,num), **kwargs)
            return res
        return wrapper
    
    def enter_contact_name(f):
        def wrapper(self, **kwargs):
            n = input("Enter name:")           
            res = f(self, Contact(n,0), **kwargs)
            return res
        return wrapper
    
    @enter_contact_info
    def add_con(self,cont):
        if cont in (self._contacts):
            raise PhoneBookError('Contact already exist in phonebook.')
        self._contacts.add(cont)
    
    @enter_contact_name    
    def get_con(self, cont):
        for c in self._contacts:
            if c == cont:
                return c
        raise PhoneBookError('Contact not found.')
    
    @enter_contact_info
    def upd_con(self, cont):
        if cont not in (self._contacts):
            raise PhoneBookError('Contact not found.')
        self._contacts.add(cont)

    @enter_contact_name    
    def del_con(self, cont):
        try:
            self._contacts.remove(cont)
        except KeyError:    
            raise PhoneBookError('Contact not found.')
        
      
def write_change():
    with open(file_name, 'w+b') as phonebook_file:
        pickle.dump(book, phonebook_file)

def autosave(f):
    def wrapper(**kwargs):
        res = f(**kwargs)
        write_change()
        return res
    return wrapper        
        
@autosave        
def add_num():
    book.add_con() 
    
def search_num():
    print(book.get_con())

@autosave 
def upd_num():
    book.upd_con()

@autosave
def del_num():
    book.del_con()
    
def show_all():
    print(book)
        
def exec_action(action):
    actions.get(action, wrong_action)()

def wrong_action():
    print("Incorrect action!")    
    
def quit():
    sys.exit()

def main_func():

    while True:
        action = input("Choose action: a, s, u, d, all, q:")
        try:
            exec_action(action)
        except PhoneBookError as e:
            print(e)
            
actions = {'a': add_num, 's': search_num, 'u': upd_num, 'd': del_num, 'all': show_all, 'q': quit}
file_name = 'phonebook.pickle'
book = PhoneBook()
book.load_data(file_name)
main_func()

