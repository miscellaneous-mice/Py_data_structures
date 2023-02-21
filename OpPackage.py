class PythonOp:
    
    def lib_ref(self, lib):

        #default = "incorrect 
              
        print("\nIt's a Operation\n")
                
        return getattr(self, lib.upper(), None)()
           
    def BYTEARRAY(self):
        
        print("this operation is :",'\033[1m' +                                 'bytearray\n' + '\033[0m' )
        
        # Creating bytearray

        a = bytearray((12, 8, 25, 2))

        print("Creating Bytearray:")

        print(a)
 
        # accessing elements

        print("\nAccessing Elements:", a[1])
 
        # modifying elements 

        a[1] = 3

        print("\nAfter Modifying:")

        print(a)
 
        # Appending elements

        a.append(30)

        print("\nAfter Adding Elements:")

        print(a)
        
    def DEQUE(self):
        
        print("this operation is :",'\033[1m' +                                 'Deque\n' + '\033[0m' )
        
        import collections
 
        # initializing deque
        de = collections.deque([1,2,3])
 
        # using append() to insert element at right               end
        # inserts 4 at the end of deque
        de.append(4)
 
        # printing modified deque
        print("The deque after appending at right is :           ")
        print(de)
 
        # using appendleft() to insert element at left           end
        # inserts 6 at the beginning of deque
        de.appendleft(6)
 
        # printing modified deque
        print("The deque after appending at left is : ")
        print(de)
 
        # using pop() to delete element from right               end
        # deletes 4 from the right end of deque
        de.pop()
 
        # printing modified deque
        print("The deque after deleting from right is :           ")
        print(de)
 
        # using popleft() to delete element from left             end
        # deletes 6 from the left end of deque
        de.popleft()
 
        # printing modified deque
        print("The deque after deleting from left is : ")
        print(de)

