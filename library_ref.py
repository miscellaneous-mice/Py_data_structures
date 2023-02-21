from LibPackage import PythonLib
from OpPackage import PythonOp
import inspect
import difflib
           
def has_method(o, name):
    return callable(getattr(o, name, None))
    
def remove(string):

    return string.replace(" ", "")

def strn(str1, str2):

    similarity = difflib.SequenceMatcher(None, str1, str2).ratio()

    str_op =  similarity*100
    return str_op

def expected(d):
  return max(d, key = d.get)

#Go = "test"
max_dict = {}
my_library = PythonLib()
my_operation = PythonOp()

bool_var = True

Libraries = inspect.getmembers(PythonLib, predicate=inspect.isfunction)

print(f"Libraries are \n{Libraries}\n")

Operations = inspect.getmembers(PythonOp, predicate=inspect.isfunction)

print(f"Operations are \n{Operations}\n")

while(bool_var):
    
    choose = input("\nOperation or Library you wanna access : ")
    choose = choose.upper()
    
    Go = remove(choose)

    for Lib,address in Libraries:
        similar = strn(Lib, Go)
        max_dict[Lib] = similar
    
    for Oper,address in Operations:
        similar = strn(Oper, Go)
        max_dict[Oper] = similar

    Go = expected(max_dict)

    if(has_method(my_library, Go.upper())):
        
        bool_var = False

        print (my_library.lib_ref(Go))
        
    elif(has_method(my_operation,Go.upper())):
        
        bool_var = False

        print (my_operation.lib_ref(Go))
        
    else:
        
        print("\nLibrary/Operation not found")

        
