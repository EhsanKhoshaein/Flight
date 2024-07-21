if username == emp_info[0] and password == emp_info[1]:
    print("WELCOME EMPLOYEE !")
    search = [input('\nEnter the Origin: '),input('Enter the Destination: ')]
    #read the flights doc and find it:
    if flag == 1:
        print('''
    1. Show the Remaining Capacity
    2. Create new Ticket
    3. Show all the Tickets
    4. Search a Ticket  #private
    5. exit
    ''')
        emp_choice = ('1','2','3','4','5')
        choice = input("\nEnter your choice: ")
        if choice not in emp_choice:
            print("\nWRONG INPUT !")
        elif choice == emp_choice[0]:
            #show the remaining capacity
        elif choice == emp_choice[1]:
            #create new Ticket
        elif choice == emp_choice[2]:
            #from tickets of this flight, show all infos
        elif choice == emp_choice[3]:  #PRIVATE
            #henqame farakhanie methode private, aval user o pass migirim, agar == manager:
            print('''
            1. Edit the Ticket
            2. Delete the Ticket
            3. Go Back
            ''')
            emp_search_choice = ('1','2','3')
            search = input("\nEnter your choice: ")
            if search not in emp_search_choice:
                print("\nWRONG INPUT")
            elif search == emp_search_choice[0]:
                pass
            elif search == emp_search_choice[1]:
                pass
            elif search == emp_search_choice[2]:
                break
            #agar nabud: print("SORRY .. YOU CAN NOT ACCESS TO THIS PART")
        elif choice == emp_choice[4]:
            break


else:
    print('counterfeit user ..')
