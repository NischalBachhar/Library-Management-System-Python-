#importing date and time
import datetime

#defining function file to open a text file containing books
def file():
    file = open("books.txt","r")
    print("Books present in library are: ")
    print(file.read())
    file.close

#defining function borrow to borrow books from libary.
def borrow(a):

#Construting listbook to store books in bill.    
    listbook = []
    
#Constructing listprice to store prices of different books in bill.    
    listprice = []
    print ("\n"
        "You will now borrow a book.")

    #Constructing loop
    contin = True

    while contin == True:

    #Exception handling incase if inavalid data is entered as book ID
        trbid = False
        while trbid == False:
            try:
                boid = int(input("\n"
                    "Enter the Book ID of the book :"))
                trbid = True
            except:
                print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX \n"
                         "Invalid book id !!! Please enter a valid bookid\n"
                         "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        #while loop incase if user enter value less than 0 or more than the lenght of book id.
        while boid <= 0 or boid>len(dict_):
                print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n"
                      "Invalid book ID !!! Please enter a valid book ID\n"
                        "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
            
            #Exceptional handlig incase if the user entered invalid book ID.
                inv = False
                while inv == False:
                    try:
                    
                        boid = int(input("Enter the book ID of the book: "))
                        inv = True
                    except:
                        print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n"
                          "Invalid book ID !!! Please enter a valid book ID.\n"
                          "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
                    
        #Inspecting if the book is available or not.
        if (int(dict_[boid][2])) == 0:
            
            #Giving output to the user if the book is not available.
            print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n"
                      " \t \t \t Sorry!!! Book is not available!!! \n"
                      "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

        #Giving output to the user if the book is available.
        else :
            
            print ("==========================================================================\n"
                       " \t \t \t Book is available!!! \n"
                       "==========================================================================\n")


                #asking the user to input the name of the borrower
            name = input("\n"
            "Enter the name of the borrower: ")
            listprice.append(dict_[boid][3]) #Appending price of the book to the list
            listbook.append(dict_[boid][0])  #Appending book name to the list
            print ("The price of the book is",("$"+dict_[boid][3])) #Displaying the price of the book from the dictionary
            
            import datetime #importing date and time
            datetime1 = datetime.datetime.now() 
            total = list(map(int,listprice))
            sum_price = sum(total)   #Calculating total price of the book
            print("Date & time of borrow : ", datetime1) #Displaying current time
            dict_[boid][2] = int(dict_[boid][2]) - 1 #Subtracting quantity of book from the dictionary
            dict_w() #Calling dict_w() function
            print("\n"
                    "Library after borrow is: ")
            disp_dict() #calling disp_dict() function
            contin = False

            Cound = True
            while Cound == True:
                
                #Asking the user if they want to borrow more book
                more = input("\n"
                        "Do you want to borrow more book? \n"
                        "If 'Yes' please enter 'Yes' or else enter 'No': ")
                if more == "Yes" or more == "yes" or more == "y":
                    
                #Exceptional handling incase if the user enter invalid book id
                    bot = False
                    while bot == False:
                        try:
                        
                            boid2 = int(input("Enter book ID of the book: "))
                            bot = True
                        except:
                            print("\nInvalid book ID !!! Please enter a valid book ID\n")
                            
                #Constructing While loop if the user enter less than 0 or more than the book id.
                    while boid2 <= 0 or boid2>len(dict_):
                        print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n"
                          "Invalid book ID !!! Please enter a valid book ID\n"
                            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")

                        tob = False
                        while tob == False:
                            try:
                                boid2 = int(input("Enter the book ID of the book: "))
                                tob = True
                            except:
                                print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n"
                                      "Invalid book ID !!! Please enter a valid book ID\n"
                                        "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
                    
                    if (int(dict_[boid2][2])) == 0: #Inspecting if the book is available or not.
                        
                        #Giving output to the user if the book is not available.
                        print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n"
                               " \t \t \t Sorry!!! Book is not available!!! \n"
                               "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
                        boid2 = int(input("Enter the book ID : "))
                        listprice.append(dict_[boid2][3])
                        listbook.append(dict_[boid2][0])
                        total = list(map(int,listprice))
                        sum_price = sum(total)
                        dict_[boid2][2] = int(dict_[boid2][2]) - 1
                        dict_w()
                        print("\n"
                            "Library after borrow is: ")
                        disp_dict()
                        

                    

                    #Giving output to the user if the book is available.
                    else :
                        print("==========================================================================\n"
                           " \t \t \t Book is available!!! \n"
                            "==========================================================================\n")

                    

                        listprice.append(dict_[boid2][3])
                        listbook.append(dict_[boid2][0])
                        total = list(map(int,listprice))
                        sum_price = sum(total)
                        dict_[boid2][2] = int(dict_[boid2][2]) - 1
                        dict_w()
                        print("\n"
                            "Library after borrow is: ")
                        disp_dict()

                
                else:
                    Cound = False
                    print("\n")
                    print ("Name of the borrower : ",name)  #Displaying Name of the borrower
                    print ("Total price : $",sum_price)     #Displaying Total price of the book
                    print ("Date and time of borrow : ", datetime1) #Displaying Date&Time of borrow
                    print ("Books borrowed are : ")     #Displaying Name of the books that are borrowed
                    for i in range(len(listbook)):
                        print(listbook[i])
                    print ("<><><><><><><><><><><><><><><><><><><><><><><><><<><><><><><><><><><><>"
                       "\nThe bill has been generated successfully.\n"
                       "<><><><><><><><><><><><><><><><><><><><><><><><><<><><><><><><><><><><>\n")
                    
                    import datetime #importing date and time
                    sec = str(datetime.datetime.now().second)
                    microsec = str(datetime.datetime.now().microsecond)
                    mix = sec+microsec

                    #Creating a text file (Billing) of borrow
                    file = open("borrow_"+name+mix+".txt","w")
                    file.write("\n Name of the person :"+name)
                    file.write("\n Total price : $"+str(sum_price))
                    file.write("\n Date & time of borrow :"+str(datetime1))
                    file.write("\n Books borrowed are : "+" \n ")
                    for i in range(len(listbook)):
                        file.write(listbook[i]+" \n ")
                    file.close()

    
    lib() #Calling lib() function

#Defining a function datadisplay to display name, price, books borrowed, date & time
def datadisplay():
 
    print("\n")
    print ("Name of the person : ",name)
    print ("Total price : $",sum_price)
    print ("Date and time of borrow : ", datetime1)
    print ("Books borrowed are : ")
    for i in range(len(listbook)):
        print(listbook[i])

#Defining a function dict_w to write in books.txt file 
def dict_w():
    file = open("books.txt","w")
    for values in dict_.values():
        file.write(str(values[0]) + ","+ str(values[1])+ ","+str(values[2])+","+ str(values[3]))
        file.write("\n")
    file.close()

#Defining retrn function to return the books to the libary    
def retrn(a):

    returnlist=[] #Creating returnlist to store books name in bill.
    print ("\n"
        "You will now return the book that you have borrowed. \n")

    #Exception handling incase if the user input invalid book id.
    trrtn = False
    while trrtn == False:
        try:
            retbook = int(input("Enter the book id of the book you want to return: "))
            trrtn = True
        except:
            print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n"
                  "Invalid book ID !!! Please enter a valid book ID"
                  "\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")

    #While loop incase if the user enter book id less than 0 or more than the books id.
    while retbook <= 0 or retbook>len(dict_):
        print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n"
              "Invalid book ID !!! Please enter a valid book ID\n"
              "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
        tre = False
        while tre == False:
            try:
                
                
                retbook = int(input("Enter the book id of the book you want to return: "))
                tre = True
            except:
                print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n"
                      "Invalid book ID !!! Please enter a valid book ID\n"
                      "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
            
    dict_[retbook][2] = int(dict_[retbook][2]) + 1 #Adding quantity of book in dictionary
    returnlist.append(dict_[retbook][0]) #adding book to the returnlist for bill of return.
    dict_w() #calling dict_w() function

    name = input("Enter the name of the returner: ")
    import datetime
    dateNtimeRetrn = datetime.datetime.now() #Displaying current time.
    print("\n"
    "Library after return is: ")
    disp_dict() #calling disp_dict() function

   
        #Exceptional handling
    trda = False
    while trda == False:
        
        try:
                #Asking the no. of borrow days from the user
            days = int(input("\n Enter the No. of borrow days: "))
            trda = True
                
        except:
            print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n"
                      "Invalid value!!! Please enter a valid value."
                      "\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
                

        #Constructing finelist to add fine in the list
        finelist = []
        #Calculating the fine amount if the borrow days is more than 10
        if days>10:
            fineamount = 0.24
            fine = (days - 10) * fineamount
            finelist.append(fine)
            totalf = sum(finelist)
            print("\n Due to the fact you have return this book after", days ,"days, you have been penalized $0.24 each day as per the guideline. \n This fine must be paid right away.")
            print("\n Total Fine amount is $", totalf)

        else:
            totalf = 0

        Cound = True
        while Cound == True:
        #Asking the user if they want to return another book too
            more = input("\n"
                "Do you wish to return another book too? \n"
                        "If 'Yes' please enter 'Yes' or else enter 'No': ")
            if more == "Yes" or more == "yes" or more == "y":

                #Exception handlng for invalid book id
                rtn = False
                while rtn == False:
                    try:
                        retbo = int(input("Enter the book ID: "))
                        rtn = True
                    except:
                        print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n"
                          "Invalid value!!! Please enter a valid book ID"
                          "\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
                    
                
                #Updating the quantity of book after return       
                dict_[retbo][2] = int(dict_[retbo][2]) + 1
                #Adding the updated quantity in the dictionary
                returnlist.append(dict_[retbo][0])
                dict_w()
                print("\n"
                "Library after return is: ")
                disp_dict()
                days_ = int(input("\nEnter the no. of borrow days:"))
                if days_>10:
                    fineamount = 0.24
                    fine1 = (days_ - 10) * fineamount
                    finelist.append(fine1)
                    totalf = sum(finelist)
                    print("\n Due to the fact you have return this book after", days ,"days, you have been penalized $0.24 each day as per the guideline. \n This fine must be paid right away.")
                    print("\n Total Fine amount is $", totalf)
            
     

            else:
                Cound = False
                print("\n")
                print ("Name of the person : ",name) #Displaying Name of returner
                print ("Date and time of return : ",dateNtimeRetrn) #Displaying Date & time of return
                print ("Total fine amount is : $",totalf) #Displaying total fine amount
                print ("Books returned are : ")     #Displaying books that are returned
                for i in range(len(returnlist)):
                    print(returnlist[i])
                print ("<><><><><><><><><><><><><><><><><><><><><><><><><<><><><><><><><><><><>"
                       "\nThe bill has been generated succesfully.\n"
                       "<><><><><><><><><><><><><><><><><><><><><><><><><<><><><><><><><><><><>\n")
                
        #importing date and time
        import datetime
        sec = str(datetime.datetime.now().second)
        microsec = str(datetime.datetime.now().microsecond)
        mix = sec+microsec

        #Constructingg a text file (Billing) for return
        file = open("return_"+name+mix+".txt","w")
        file.write("\n Name of the person :"+name)
        file.write("\n Date & time of return :"+str(dateNtimeRetrn))
        file.write("\n Total fine amount is : $"+str(totalf))
        file.write("\n Books returned are : "+" \n ")
        for i in range(len(returnlist)):
            file.write(returnlist[i]+" \n ")
        file.close()


#Defining a function exit to show the message if the user exit the program
def exit(a):
    print ("\n============================================================================\n"
           "\t \t Thank you for using our library management system.\n"
           "============================================================================\n")


#Defining a function lib to show the welcome message when the user open the program
def lib():
    print("\n==========================================================================\n"
          "\t \t Hello and Welcome to our library management system\n"
          "==========================================================================\n")


    disp_dict() #Calling disp_dict function
    usdata()    #Calling usdata function

#Defining a function disp_dict to display the details about the book
def disp_dict():
    print("\n"
        "___________________________________________________________________________")
    print("Book ID " + " Book Name \t"  + " Author      " + "Quantity " + "  Price" )
    print("___________________________________________________________________________")
    dictionary ={} #Creating dictionary
    file = open("books.txt","r") #Opening books.txt from txt file
    n = 0
    for line in file:
        n = n + 1
        line = line.replace("\n","")
        dictionary [n] = line.split(',')
        line = line.replace(",", " \t")
        
        print(n, "\t", line) 
    print("_______________________________________________________________________________\n")
    file.close()

#Defining a function bookdic to open the books.txt file    
def bookdic():
    dictionary ={} #Creating dictionary
    file = open("books.txt","r") #Opening books.txt file
    n = 0
    for line in file:
        n = n + 1
        line = line.replace("\n","")
        dictionary [n] = line.split(',')
        line = line.replace(",", " \t")

    file.close()
    return dictionary #Making dictionary accesible globally.

dict_ = bookdic() #Assigning value of bookdic() function to dict_.



#Defining a function usdata to ask the user if they want to borrow, return or exit the program.
def usdata():
    #Exceptional Handling if incase user enter invalid value.
    corvalue = False
    while corvalue == False:

        try:
            
            usdataInput = int(input("\n"
                "Enter '1' to borrow a book\n"
                            "Enter '2' to return a book\n"
                            "Enter '3' to exit\n"
                            "Please enter a value: "))
            corvalue = True
            
        except:
            print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n"
                  "Invalid Value !!! Please enter '1' or '2' or '3'. \n"
                    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
            disp_dict()


    if usdataInput == 1: 
        
        borrow(usdataInput)

    elif usdataInput == 2:
            
        retrn(usdataInput)
        lib()

    elif usdataInput == 3:
            exit(usdataInput)

    #Giving output to the user if incase user enter value other than 1 or 2 or 3.
    else:
        print ("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n"
                    "Invalid value. Please enter '1' or '2' or '3'."
               "\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
        
        #Calling the disp_dict() and usdata() function
        disp_dict()
        usdata()
            
        
    
    return usdataInput #Making usdataInput accessible globally
          
            
     
        


