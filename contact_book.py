import re
import json

#CONTACT DICTIONARY
full_contact = {
        "Name": "",
        "Civic Number": "",
        "Street Name": "",
        "Appartment Number": "",
        "City": "",
        "Province": "",
        "Postal Code": "",
        "Phone number": "",
        "Email": "",
}

#ALL REGEX PATTERNS
pattern_name = "^([a-zA-Z']){2,20}(\s|-?)[a-zA-Z?]{0,20}\s[a-zA-Z]{2,20}$"
pattern_civic_number = "^\d{1,5}$"
pattern_street_name = "^[a-zA-Z]|[0-9]|(-'.)$"
pattern_appartment_number = "[a-zA-Z]|[0-9]?"
pattern_city = "^[a-zA-Z]|[0-9]|(-'.)$"
pattern_province = "[a-zA-Z]{2}"
pattern_postal_code =  "^[a-zA-z]{1}\d{1}[a-zA-z]{1}\s{1}\d{1}[a-zA-Z]{1}\d{1}$"
pattern_phone_number = "\d\d\d(-|\s)?\d\d\d(-|\s)?\d\d\d\d"
email_pattern = "[a-zA-Z0-9]+@[a-zA-Z0-9]+\.(com|ca|fr|edu|net|org)"

#CHECKING USER INPUT FUNCTIONS
def checkName():
    check_name_pattern = 0
    contact_name = input("First and last name: ")
    while check_name_pattern != 1:
      if (re.search(pattern_name, contact_name)):
          full_contact["Name"] = contact_name
          check_name_pattern +=1
      else:
          print("Hmm that doesn\'t seem right, please try again.")
          contact_name = input("First and last name: ")

def checkAddress():
    civic_number = input("Civic number: ")
    check_pattern_civic = 0
    while check_pattern_civic != 1:
        if (re.search(pattern_civic_number, civic_number)):
            full_contact["Civic Number"] = civic_number
            check_pattern_civic += 1
        else:
            print("Hmm that doesn\'t seem right, please try again.")
            civic_number = input("Civic number: ")

    street_name = input("Street name: ")
    check_pattern_street = 0
    while check_pattern_street != 1:
        if (re.search(pattern_street_name, street_name)):
            full_contact["Street Name"] = street_name
            check_pattern_street += 1
        else:
            print("Hmm that doesn\'t seem right, please try again.")
            street_name = input("Street name: ")

    appartment_number = input("Appartment number(Optional): ")
    check_pattern_appartment = 0
    while check_pattern_appartment != 1:
        if (re.search(pattern_appartment_number, appartment_number)):
            full_contact["Appartment Number"] = appartment_number
            check_pattern_appartment += 1
        else:
            print("Hmm that doesn\'t seem right, please try again.")
            appartment_number = input("Appartment number(Optional): ")

    city = input("City: ")
    check_pattern_city = 0
    while check_pattern_city != 1:
        if (re.search(pattern_city, city)):
            full_contact["City"] = city
            check_pattern_city += 1
        else:
            print("Hmm that doesn\'t seem right, please try again.")
            city = input("City: ")

    province = input("Province: ")
    check_pattern_province = 0
    while check_pattern_province != 1:
        if (re.search(pattern_province, province)):
            full_contact["Province"] = province
            check_pattern_province += 1
        else:
            print("Hmm that doesn\'t seem right, please try again.")
            province = input("Province: ")

    postal_code = input("Postal code: ")
    check_pattern_postal = 0
    while check_pattern_postal != 1:
        if (re.search(pattern_postal_code, postal_code)):
            full_contact["Postal Code"] = postal_code
            check_pattern_postal += 1
        else:
            print("Hmm that doesn\'t seem right, please try again.")
            postal_code = input("Postal code: ")

def checkPhone():
    phone_number = input("Phone number: ")
    check_phone_pattern = 0
    while check_phone_pattern != 1:
        if (re.search(pattern_phone_number, phone_number)):
            full_contact["Phone number"] = phone_number
            check_phone_pattern += 1
        else:
            print("Hmm that doesn\'t seem right, please try again.")
            phone_number = input("Phone number: ")

def checkEmail():
    contact_email = input("Email:  ")
    check_email_pattern = 0
    while check_email_pattern != 1:
        if(re.search(email_pattern, contact_email)):
          full_contact["Email"] = contact_email
          check_email_pattern += 1

        else:
          print("Hmm that doesn\'t seem right, please try again.")
          contact_email = input("Email:  ")


def addContact():
    checkName()
    checkAddress()
    checkPhone()
    checkEmail()
    s = json.dumps(full_contact)
    a = json.loads(s)
    f = open("my_contact_book.txt" ,"a")
    f.write(s + '\n')
    f.close()

def searchContact():
    f = open("my_contact_book.txt", "r")
    print("Searching for a contact.")
    contact_search = input("Search: ")
    for line in f:
        if not line.__contains__(contact_search): continue
        else:
            print(line)

def viewAll():
    lines = []
    with open("my_contact_book.txt") as f:
        lines = f.readlines()
    for i in range(len(lines)):
        print(i, end = " ")
        print(lines[i])

def deleteContact():
    item_deleted = False
    lines = []
    with open("my_contact_book.txt") as f:
        lines = f.readlines()
    for i in range(len(lines)):
        print(i, end = " ")
        print(lines[i])
    item_deleted = False
    while item_deleted == False:
        delete_contact = int(input("Type the ID of the contact to be deleted: "))
        if (delete_contact <= (len(lines))):
            del lines[delete_contact]
            with open("my_contact_book.txt", "w") as f:
                for line in lines:
                    f.write(line)
                    print("Contact deleted.")
                    item_delete = True
    else:
            print("The ID entered does not exist in the contact book.")
