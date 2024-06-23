#entering contact name
n=int(input("Enter number of contacts to enter\n"))
list_name=[]
list_phone=[]
for x in range(1,n+1):
    name=input("Enter name \n")
    list_name.append(name)
    num=input("Enter number \n")
    list_phone.append(num)
while True:
    user=int(input("Enter 1 to add, 2 to search, 3 to delete, 4 to view, 5 to exit \n"))
    if user==1:
        name=input("Enter name \n")
        list_name.append(name)
        num=input("Enter number \n")
        list_phone.append(num)
        print("NUMBER ADDED SUCCESSFULLY\n")
    elif user==2:
        search=input("Enter name to be searched \n")
        if search in list_name:
            search_name=list_name.index(search)
            print("Contact number- ")
            print(list_phone[search_name])
        else:
            print("Contact not available \n")
    elif user==3:
        delete=input("Enter contact to be deleted\n")
        if delete in list_name:
            delete_name=list_name.index(delete)
            del list_name[delete_name]
            print("NUMBER DELETED SUCCESSFULLY\n")
        else:
            print("Contact not available\n")
    elif user==4:
        for x in range (1,n+1):
            for x in list_name:
                print("Contact name- ")
                print(x)
                num_ind=list_name.index(x)
                print("Contact number- ")
                print(list_phone[num_ind])
            print("\n")
    elif user==5:
        print("TERMINATED SUCCESSFULLY\n")
        exit
    else:
        print("Invalid input \n")