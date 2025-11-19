#tasks 5 contact book

contacts=[]#list stoge the contacts

def show_menu():
    print("\n ==== CONTACTS BOOKS MENU ====\n")
    print("1.Add contacts\n")
    print("2.View contacts\n")
    print("3.Search contacts\n")
    print("4.Update contacts\n")
    print("5.Delete contacts\n")
    print("6.Exit")

def add_contact():
    print("--Add The New Contacts")
    name=input("Enter name:")
    phone=input("Enter phone number:")
    email=input("Enter the email id:")
    address=input("Enter the adress:")

    con={
        "name":name,
        "phone":phone,
        "email":email,
        "address":address
    }
    contacts.append(con)
    print("Contact is successufully added")

def view_contact():
    print("\n Contacts List")
    if not contacts:
        print("No record is found")
        return
    for i,con in enumerate(contacts,start=1):
        print("\n Contact")
        print("Name",con["name"])
        print("Phone",con["phone"])
        print("email",con["email"])
        print("address",con["address"])

def search_contact():
    print("\n === Search contact==")
    keyword=input("Enter the name or phone number:")
    found=False
    for con in contacts:
        if keyword.lower()in con['name'].lower() or keyword in con['phone']:
            print("Name",con["name"])
            print("Phone",con["phone"])
            print("email",con["email"])
            print("address",con["address"])
            found=True
        if not found:
            print("No matching contact found")

def upadate_contact():
    print("--update  contact")
    search=input("\n Enter name of contact to update")
    for con in contacts:
        if search.lower()==con['name'].lower():
            print("\n Contact found ! Enter the new details")

            con['name']=input('new name:')
            con['phone']=input('new phone:')
            con['email']=input('new eamil:')
            con['address']=input('new address:')

            print("contact update successfully")
            return
    print("contact is not found ")


def delete_contact():
    print("==delete contact")
    search=input("enter the contact to delete ")
    for con in contacts:
        if search.lower()==con['name'].lower():
            contacts.remove(con)
            print("contact deleted  succfully")
            return
    print("contact is not found ")

while True:
    show_menu()
    choice=input("\n Enter the choice 1 to 6:\t")

    if choice=='1':
        add_contact()
    elif choice=='2':
        view_contact()
    elif choice=='3':
        search_contact()
    elif choice=='4':
        upadate_contact()
    elif choice=='5':
        delete_contact()
    elif choice=='6':
        print("Exiting contcat book byeeeeee!!")
        break
    else:
        print("enter the valid choice! please enter the number between 1 to 6")
