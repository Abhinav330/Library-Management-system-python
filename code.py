class Library :

    lender = {}
    
    def __init__(self, bokk ,nm) :     # Constructor 
        self.books = []
        self.books = bokk
        self.name = nm
    
    def disp(self):                                                             #This Method will print all the books Available.
        '''This Method will print all the books Available. '''
        
        print("\nwe have following Books \n")
        for x in self.books :
            print(x)
    
    def lend (self):                                                            #This Method is used for issuing a book to a user
        ''''This Method is used for issuing a book to a user'''
        a = input("Enter your Name\t")
        b = input("Enter Book Name\t")
        if b in self.books :
            print("Book is available . so  issued to you")
            self.lender.update({b:a})
            self.books.remove(b)
           # print(self.lender)
        else :
            print(f"Book is not available . {self.lender.get(b)} is having this book")
        
            
    def Return_Book (self):                                                    #This Method is used for Returning a book
        ''''This Method is used for Returning a book'''
        a = input("Enter your Name\t")
        b = input("Enter Book Name\t")
        if self.lender.get(b) != None:
            print("Found your record and Now resetting your book count\n")
            self.books.append(b)
            self.lender.pop(b)
        else :
            print("Error in your Entered Data")      

    def addbook(self):                                                         #This Method is used for adding a book to this system
        ''''This Method is used for adding a book to this system'''
        a = input("Enter your Name\t")
        b = input("Enter Book Name\t")
        print("\n")
        self.books.append(b)
        if (b in self.books):
            print(f"Thank you {a} For Donating This book :)\n")

        else :
            print(f"Sorry!! {a} we cannot add {b} to our library \n") 

        


    



cs = "y"                                                                       # Case used to break the loop
bok = ["ds" , "c++" ,"c" , "python" ,"java" , "php", "swift"]                  # Books available in Library 

abhinav = Library(bok , "Abhinav")

while cs == "y":                                                              # Menu Loop 
    print(f"welcome to  {abhinav.name} Library \n")
    print('''               Press 1 to display All the Books available.  
               Press 2 to Lend a Book From this Library.
               Press 3 to Return Back a Book .
               Press 4 to Donate a Book. \n\n
    ''')

    x = int(input("Enteer your choice :\t"))
    print("\n")
    if x == 1 :
        abhinav.disp()
    elif x == 2 :
        abhinav.lend()
    elif x == 3 :
        abhinav.Return_Book()
    elif x == 4 :
        abhinav.addbook()
    
    else :
        print("\n Invalid Input \n")
    
    cs = input("\nWant to continue?? [y/n]")






