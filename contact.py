contact_dictionary = {}
details = []
print("CONTACT BOOK")
def insert():
    details= input("Enter Name,Contact Number,Email,Address(give space)").split()
    name = details[0]
    contact = details[1]
    email = details[2]
    address = details[3]
    records = {'Name': name,'Contact Number':contact,'Email':email,'Address':address}
    contact_dictionary[name]=records
def search():
    search_for = input("Search:(enter name/contact/email)")
    for x in contact_dictionary:
        if contact_dictionary[x]['Name'] == search_for:
            print("True")
            print(contact_dictionary[x])
        elif contact_dictionary[x]['Contact Number'] == search_for:
            print("True")
            print(contact_dictionary[x])
        if contact_dictionary[x]['Email'] == search_for:
            print("True")
            print(contact_dictionary[x])

def main():
    insert()
    while True:
        user_input = input ("Enter 1 to add more contacts, 2 to search existing contach, 3 to exit")
        if user_input == "1":
            insert()
        elif user_input == "2":
            search()
        elif user_input == "3":
            break

if __name__ =='__main__':
    main()
            
        
         
    
