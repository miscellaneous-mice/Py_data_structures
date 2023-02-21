class PythonLib:
    
    #@classmethod
    
    def lib_ref(self, lib):

        #default = "incorrect library"
                
        print("\nIt's a Library\n")
        
        #return getattr(self, lib.upper(), lambda: default)()
                
        return getattr(self, lib.upper(), None)()
 

    def COUNTER(self):
        
        print("this library is :",'\033[1m' + 'Counter\n' +            '\033[0m' )
        
        from collections import Counter 

    
# With sequence of items  

        print(Counter(['B','B','A','B','C','A','B','B','A','C'])) 

    
# with dictionary 

        count = Counter({'A':3, 'B':5, 'C':2}) 

        print(count) 
        
        print(list(count.elements()))

        count = Counter(A = 2, B = 4, C = 10)
        

        for _ in range (0,20):
            if ( count.get('A')  < 10):

                count.update(['B', 'D', 'A'])
            else:
                 if(count.get('B') < 1):
                    count.update(['B', 'D']) 
                 else:
                     count.update(['D'])

        return count

 

    def ORDEREDDICT(self):
        
        print("this library is :",'\033[1m' + 'Ordered Dict\n' + '\033[0m' )
        
        from collections import OrderedDict 

        print("Before deleting:\n") 

        od = OrderedDict() 

        od['a'] = 1

        od['b'] = 2

        od['c'] = 4

        od['d'] = 3

  

        for key, value in od.items(): 

            print(key, value) 

  

        print("\nAfter deleting:\n") 

        od.pop('c') 

        for key, value in od.items(): 

            print(key, value) 

  

        print("\nAfter re-inserting:\n") 

        od['c'] = 3

        for key, value in od.items(): 

            print(key, value) 

    
        return od


    def DEFAULTDICT(self):
        
        print("this library is :",'\033[1m' + 'defaultdict\n' + '\033[0m' )
        
        from collections import defaultdict 
  
# Defining the dict 

        d = defaultdict(int)       

        L = [1, 1,4,2,3,3,4] 

      
# Iterate through the list 
# for keeping the count 
        d[0] = 14

        for i in L:           

    # The default value is 0 

    # so there is no need to 

    # enter the key first 

            d[i] += 1

          
        return d


    def CHAINMAP(self):
        
        print("this library is :",'\033[1m' + 'ChainMap\n' + '\033[0m' )
        
        from collections import ChainMap


        d1 = {'a': 1, 'b': 2}

        d2 = {'c': 3, 'd': 4}

        d3 = {'e': 5, 'f': 6}
        
        d4 = { 'a': 3, 'g': 5}

     
        # Defining the chainmap

        c = ChainMap(d1, d2, d3, d4)

        print(c)
 

        print(c['a'])

        #print(c['j'])    if you want keyerror
    
    def NAMEDTUPLE(self):
        
        print("this library is :",'\033[1m' +                                 'NamedTuple\n' + '\033[0m' )
         
        from collections import namedtuple
     
        # Declaring namedtuple()
        Student = namedtuple('Student',['name','age',           'DOB'])
     
        # Adding values
        S = Student('Nandini','19','2541997')
     
        # Access using index
        print ("The Student age using index is : ",end            ="")
        print (S[1])
     
        # Access using name
        print ("The Student name using keyname is : ",        end ="")
        print (S.name)
        
        #access using getattr
        print("The Student DOB using getattr() is : ",             end="")

        print(getattr(S, 'DOB'))
        
        print("All the fields of students are : ")

        print(S._fields)
 
# ._replace returns a new namedtuple, it does not modify the original

        print("returns a new namedtuple : ")

        print(S._replace(name='Manjeet'))
# original namedtuple

        print(S)  
    

    def USERDICT(self):
        
        print("this Library is :",'\033[1m' +                                 'UserDict\n' + '\033[0m' )
        
        from collections import UserDict
 
        # Creating a Dictionary where
        # deletion is not allowed

        class MyDict(UserDict):

        # Function to stop deletion

        # from dictionary

            def __del__(self):

                raise RuntimeError("Deletion not allowed")

            # Function to stop pop from

            # dictionary

            def pop(self, s = None):

                raise RuntimeError("Deletion not allowed")         

            # Function to stop popitem

            # from Dictionary

            def popitem(self, s = None):

                raise RuntimeError("Deletion not allowed")
                
            def update(self, kwargs ):
                
                raise RuntimeError("Append not allowed")
                
            def add(self, **kwargs):
                
                raise RuntimeError("multiple appends not allowed")

     
        # Driver's code

        d = MyDict({'a':1,

            'b': 2,

            'c': 3})
 

        print("Original Dictionary")

        print(d)
        
        d.add(e = 5, f = 6)
        
        #d.update({"e":5})
        
        #d.pop(1)
