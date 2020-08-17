class Library:
   def __init__(self,list,name):
      self.booklist=list
      self.name=name
      self.lendDict={}
   def displayBook(self):
      print("We have following book in our Library : {self.name}")
      for books in self.booklist:
          print(books)
   def LendBook(self,user,book):
       if book not in self.lendDict.keys():
           self.lendDict.update({book:user})
           print("Lender-Book has been updated \n You cantake the book now!")
       else:
           print(f"Book is already been lended to {self.lendDict[book]}")
   def addBook(self,book):
       self.booklist.append(bool)
       print("Book has been added to Library!")
   def returnBook(self,book):
       self.lendDict.pop(book)
FirstLibrary=Library(['Python','JKP','KKMT','Fault in Our Stars','Harry Potter'],'ALibraryBy_NamraAbid')
#print(FirstLibrary.booklist,"\n",FirstLibrary.name)
while(True):
    print(f"Welcome to {FirstLibrary.name} ")
    print("Enter your choice to continue")
    print("1.Display Book")
    print("1.Lend a Book")
    print("1.Add a Book")
    print("1.Return a Book")
    user_choice = int(input())
    if user_choice==1:
        harry.displayBook()
    elif user_choice==2:
        pass
    elif user_choice==3:
        pass
    elif user_choice==4:
        pass
    else:
        print("Not a valid option")
    print("press Q to quit and C to Continue")
    
    user_choice2=input()
    if user_choice2=='q':
        exit()
    if user_choice2=="c"
        continue
