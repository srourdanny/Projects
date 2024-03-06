import json
import os
import shutil
import time

def addData(my_db):
    """Add a new first name to the database"""
    isValidFName = False
    while not isValidFName:
        fName = input("Enter the first name: ").strip()
        isValidFName = existenceCheck(fName) and isNameValid(fName)
        fName = sanitizeInput(fName)

    """Add a new last name to the database"""
    isValidLName = False
    while not isValidLName:
        lName = input("Enter the last name: ").strip()
        isValidLName = existenceCheck(lName) and isNameValid(lName)
        lName = sanitizeInput(lName)
    
    """Add an address to the database"""
    isValidAddress = False
    while not isValidAddress:
        address = input("Enter the address: ").strip()      
        isValidAddress = existenceCheck(address) and isAddressValid(address)
        address = sanitizeInput(address)
    
    """Add a city to the database"""
    isValidCity = False
    while not isValidCity:
        city = input("Enter the city: ").strip()
        isValidCity = existenceCheck(city) and isCityValid(city)
        city = sanitizeInput(city)
    
    """Add a state to the database"""
    isValidState = False
    while not isValidState:
        state = input("Enter the state: ").strip()
        isValidState = existenceCheck(state) and isStateValid(state)
        state = sanitizeInput(state)
    
    """Add a zip code to the database"""
    isValidZip = False
    while not isValidZip:
        zip = input("Enter the zip code: ").strip()
        isValidZip = existenceCheck(zip) and isZipCodeValid(zip)
        zip = sanitizeInput(zip)
    
    """Add a company to the database"""
    isValidCompany = False
    while not isValidCompany:
        company = input("Enter the company: ").strip()
        isValidCompany = isCompanyValid(company)
        company = sanitizeInput(company)

    """Add a primary phone to the database"""
    isValidPrimaryPhone = False
    while not isValidPrimaryPhone:
        primaryPhone = input("Enter the primary phone number: ").strip()
        isValidPrimaryPhone = existenceCheck(primaryPhone) and isPhoneValid(primaryPhone)
        primaryPhone = sanitizeInput(primaryPhone)

    """Add a secondary phone to the database"""
    isValidSecondaryPhone = False
    while not isValidSecondaryPhone:
        secondaryPhone = input("Enter the secondary phone number").strip()
        isValidSecondaryPhone = isPhoneValid(secondaryPhone)
        secondaryPhone = sanitizeInput(secondaryPhone)

    
    """Add an email to the database"""
    isValidEmail = False
    while not isValidEmail:
        email = input("Enter the email: ").strip()
        isValidEmail = isEmailValid(email)
        email = sanitizeInput(email)

    """Insert the new data into the crm_data table."""
    query = f"INSERT INTO crm_data (f_name, l_name, address, city, state, zip, company, primary_phone, secondary_phone, email_address)  VALUES ('{fName}', '{lName}', '{address}', '{city}', '{state}', {zip}, '{company}', '{primaryPhone}', '{secondaryPhone}', '{email}')"
    my_db.executeQuery(query)
    my_db.conn.commit()
    
    query2 = f"INSERT INTO mailings (name, company, address)  VALUES ('{fName} {lName}', '{company}', '{address}')"
    my_db.executeQuery(query2)
    my_db.conn.commit()

def choosingDatabase():
    """Initialize a flag to check for table validity."""

    isTableValid = False

    while not isTableValid:
        """Prompt the user to choose between two tables: crm_data or mailings."""

        whichTable = input("Which table would you like to select? 1. crm_data or 2. mailings: ")
    
        if whichTable == "1":
            """Return '1' if the user chooses crm_data."""
            return "1"
    
        elif whichTable == "2":
            """Return '2' if the user chooses mailings."""
            return "2"
    
        else:
            """Print an error message if the user chooses an invalid option."""
            print("You may only choose 1 or 2.")

def crmDataDelete(my_db, userChoice):
    """Deletes data from the table chosen"""
    while True:
        """Ask the user to confirm if they really want to remove the data."""
        confirmation = input(f"Are you sure you want to remove the data with ID {userChoice}? Type Y/N: ").lower()
        
        """Execute the removal if the user confirms."""
        if confirmation == 'y':
            query = 'DELETE FROM crm_data WHERE crm_id = ' + str(userChoice)
            my_db.executeQuery(query)
            my_db.conn.commit()
            print("\Data has been removed.")
            break
        elif confirmation == 'n':
            """Cancel the removal if the user declines."""
            print("\Data removal cancelled.")
            break
        else:
            """Ask for a valid confirmation input if the user types an invalid character."""
            print("\nInvalid input. Please type Y or N.")

def crmDataEdit(my_db, userChoice):
    """Edits a specific record in the 'crm_data' table based on user input."""
    
    chooseOption = True

    while chooseOption:
        """Display available options to edit."""
        print("What would you like to edit? (Choose option 1-10)")
        print("\n1.First Name")
        print("2.Last Name")
        print("3.Address")
        print("4.City")
        print("5.State")
        print("6.Zip Code")
        print("7.Company")
        print("8.Primary Phone")
        print("9.Secondary Phone")
        print("10.Email")

        """Get user input for the option to edit."""
        option = input("\nChoose option: ")

        """Validate if the input is a number and within the range 1-10."""
        if isNumberValid(option):
            if int(option) >= 1 or int(option) <= 10:
                chooseOption = False
            else:
                print("Error. You may only choose a number between 1 and 10.")

    isValidValue = False

    while not isValidValue:
        """Loop to get the new value for the selected field."""
        
        if option == "1":
            columnName = "f_name"
            newValue = input("Enter the new first name: ").strip()
            isValidValue = existenceCheck(newValue) and isNameValid(newValue)
        elif option == "2":
            columnName = "l_name"
            newValue = input("Enter the new last name: ").strip()
            isValidValue = existenceCheck(newValue) and isNameValid(newValue)
        elif option == "3":
            columnName = "address"
            newValue = input("Enter the new address: ").strip()
            isValidValue = existenceCheck(newValue) and isAddressValid(newValue)
        elif option == "4":
            columnName = "city"
            newValue = input("Enter the new city: ").strip()
            isValidValue = existenceCheck(newValue) and isCityValid(newValue)
        elif option == "5":
            columnName = "state"
            newValue = input("Enter the new state: ").strip()
            isValidValue = existenceCheck(newValue) and isStateValid(newValue)
        elif option == "6":
            columnName = "zip"
            newValue = input("Enter the new zip code: ").strip()
            isValidValue = existenceCheck(newValue) and isZipCodeValid(newValue)
        elif option == "7":
            columnName = "company"
            newValue = input("Enter the new company name: ").strip()
            isValidValue = isCompanyValid(newValue)
        elif option == "8":
            columnName = "primary_phone"
            newValue = input("Enter the new primary phone number: ").strip()
            isValidValue = existenceCheck(newValue) and isPhoneValid(newValue)
        elif option == "9":
            columnName = "secondary_phone"
            newValue = input("Enter the new secondary phone number: ").strip()
            isValidValue = isPhoneValid(newValue)
        elif option == "10":
            columnName = "email_address"
            newValue = input("Enter the new email address: ").strip()
            isValidValue = isEmailValid(newValue)

    newValue = sanitizeInput(newValue)

    """Update the selected field in the database."""
    my_db.executeQuery("UPDATE crm_data SET " + columnName + " = \"" + newValue + "\" WHERE crm_id = " + str(userChoice))
    my_db.conn.commit()


def deleteData(my_db):
    """Deletes data in either the 'crm_data' or 'mailings' table based on user input."""
    
    """Prompt the user to choose which database table to delete from."""
    whichTable = choosingDatabase()
    
    isValid = False
    
    while not isValid:
        """Loop until a valid delete operation is performed."""
        
        """Delete data in the 'crm_data' table."""
        if whichTable == "1":
            """Get the crm_id of the record to delete."""
            userChoice = input("What is the crm_id of the line you want to delete: ").strip()
            
            """Check if the entered ID is valid."""
            if isNumberValid(userChoice):
                """Query to check if the ID exists in the database."""
                result = my_db.executeSelectQuery(f"SELECT * FROM crm_data WHERE crm_id = {userChoice}")
                
                """If the ID does not exist, inform the user."""
                if len(result) == 0:
                    print("This ID does not exist.")
                else:
                    """Call the function to delete the data in the 'crm_data' table."""
                    crmDataDelete(my_db, userChoice)
                    isValid = True

            """Delete data in the 'mailings' table."""
        elif whichTable == "2":
            """Get the mail_id of the record to delete."""
            userChoice = input("What is the mail_id of the line you want to delete: ").strip()
            
            """Check if the entered ID is valid."""
            if isNumberValid(userChoice):
                """Query to check if the ID exists in the database."""
                result = my_db.executeSelectQuery(f"SELECT * FROM mailings WHERE mail_id = {userChoice}")
                
                """If the ID does not exist, inform the user."""
                if len(result) == 0:
                    print("This ID does not exist.")
                else:
                    """Call the function to delete the data in the 'mailings' table."""
                    mailingsDelete(my_db, userChoice)
                    isValid = True


def editData(my_db):
    """Edits data in either the 'crm_data' or 'mailings' table based on user input."""
    
    """Prompt the user to choose which database table to edit."""
    whichTable = choosingDatabase()
    
    isValid = False
    
    while not isValid:
        """Loop until a valid edit operation is performed."""
        
        """Edit data in the 'crm_data' table."""
        if whichTable == "1":
            """Get the crm_id of the record to edit."""
            userChoice = input("What is the crm_id of the line you want to edit: ").strip()
            
            """Check if the entered ID is valid."""
            if isNumberValid(userChoice):
                """Query to check if the ID exists in the database."""
                result = my_db.executeSelectQuery(f"SELECT * FROM crm_data WHERE crm_id = {userChoice}")
                
                """If the ID does not exist, inform the user."""
                if len(result) == 0:
                    print("This ID does not exist.")
                else:
                    """Call the function to edit the data in the 'crm_data' table."""
                    crmDataEdit(my_db, userChoice)
                    isValid = True

            """Edit data in the 'mailings' table."""
        elif whichTable == "2":           
            """Get the mail_id of the record to edit."""
            userChoice = input("What is the mail_id of the line you want to edit: ").strip()
            
            """Check if the entered ID is valid."""
            if isNumberValid(userChoice):
                """Query to check if the ID exists in the database."""
                result = my_db.executeSelectQuery(f"SELECT * FROM mailings WHERE mail_id = {userChoice}")
                
                """If the ID does not exist, inform the user."""
                if len(result) == 0:
                    print("This ID does not exist.")
                else:
                    """Call the function to edit the data in the 'mailings' table."""
                    mailingsEdit(my_db, userChoice)
                    isValid = True           

def existenceCheck(title):
    """Checks if the input is blank or not."""
    if title == "":
        print("Input cannot be left blank. Please try again.")
        return False
    else:
        return True  

def exportCSV(dataList):
    """Open a CSV file for writing."""

    if os.path.isfile("text_files\customer_location.csv"):
        shutil.copy2("text_files\customer_location.csv", "text_files\customer_location.csv.backup" + str(time.time()))

    with open("text_files/customer_location.csv", "w") as csv_obj:

        """Iterate through each dictionary in the dataList."""
        for dictionary in dataList:
            """Write the relevant fields to the CSV file, separated by commas."""
            csv_obj.write(f"{dictionary['First Name']}, {dictionary['Last Name']}, {dictionary['County']}, {dictionary['State']}\n")
 

def exportJSON(dataList):
    """Open a JSON file for writing."""

    if os.path.isfile("text_files\customer_phone.json"):
        shutil.copy2("text_files\customer_phone.json", "text_files\customer_phone.json.backup" + str(time.time()))

    with open("text_files/customer_phone.json", 'w') as json_obj:
        """Dump the dataList into the JSON file."""
        json.dump(dataList, json_obj)

    
             

def importingData(my_db):
    """Prompt user for the location of the data import file."""
    fileLocation = input("Enter the location of the data import: ")
    
    try:
        """Open the file for reading."""
        with open(fileLocation) as readData:
            
            """Initialize empty lists for storing data and email addresses."""
            dataList = []
            emailList = []

            my_db.executeQuery("TRUNCATE TABLE mailings")
            my_db.executeQuery("TRUNCATE TABLE crm_data")
            my_db.conn.commit()
            """Iterate through each line in the file."""
            for data in readData:
                
                """Remove any '##' characters and split the line by '\\\\'."""
                data = data.replace("##", "")
                data = data.split("\\\\") 
                
                """Skip duplicate email addresses."""
                if data[10] in emailList:
                    continue
                
                """Add the email to the emailList."""
                emailList.append(data[10])

                """Skip the header line."""
                if data[0] != "first_name":
                    
                    """Create a dictionary from the line's data."""
                    dataDictionary = {"First Name": data[0], "Last Name": data[1], "Company Name": data[2], "Address": data[3], "City": data[4], "County": data[5], "State": data[6], "Zip": data[7], "Phone1": data[8], "Phone2": data[9], "Email": data[10]}
                    
                    """Append the dictionary to the dataList."""
                    dataList.append(dataDictionary)
                    
                    """Prepare SQL queries for inserting data into databases."""
                    query = f'INSERT INTO crm_data (f_name, l_name, address, city, state, zip, company, primary_phone, secondary_phone, email_address)  VALUES ("{dataDictionary["First Name"]}", "{dataDictionary["Last Name"]}", "{dataDictionary["Address"]}", "{dataDictionary["City"]}", "{dataDictionary["State"]}", {dataDictionary["Zip"]}, "{dataDictionary["Company Name"]}", "{dataDictionary["Phone1"]}", "{dataDictionary["Phone2"]}", "{dataDictionary["Email"]}")'
                    query2 = f'INSERT INTO mailings (name, company, address)  VALUES ("{dataDictionary["First Name"]} {dataDictionary["Last Name"]}", "{dataDictionary["Company Name"]}", "{dataDictionary["Address"]} {dataDictionary["City"]} {dataDictionary["State"]} {dataDictionary["Zip"]}")'
                    
                    """Execute the SQL queries."""
                    my_db.executeQuery(query)
                    my_db.executeQuery(query2)
                    
                    """Commit the changes to the database."""
                    my_db.conn.commit()
            
            """Filter and export the dataList to JSON and CSV formats."""
            filteredDataList = jsonFilter(dataList)
            exportJSON(filteredDataList)
            exportCSV(dataList)
            
    except:
        """Print an error message if the file is not found."""
        print("Error, not found.")


def isAddressValid(address):
    """Iterate through each character in the address string."""
    
    for character in address:
        
        """Check if the character is not in the allowed list and is not alphanumeric."""
        if character not in ["#", ",", ".", "-", "&", "(", ")", "\\", " "] and not character.isalnum():
            
            """Print an error message and return False if an invalid character is found."""
            print("\nUser typed invalid character. You cannot use these characters:  # , . - & ( ) \\")
            return False
    
    """Return True if all characters are valid."""
    return True



def isCityValid(city):
    """Iterate through each character in the city string."""
    
    for character in city:
        
        """Check if the character is not in the allowed list and is not alphabetic."""
        if character in ["!", '"', "@", "$", "%", "^", "&", "*", "_", "=", "+", "<", ">", "?", ";", "[", "]", "{", "}", "~", "`"]:

            """Print an error message and return False if an invalid character is found."""
            print("\nUser typed invalid character. You cannot use these characters:  ! \" @ $ % ^ & * _  = + < >  ? ; [ ] { } ~ `")
            return False
    
    """Return True if all characters are valid."""
    return True


def isCompanyValid(company):
    """Iterate through each character in the company string."""
    
    for character in company:
        
        """Check if the character is in the list of disallowed characters."""
        if character in ["~", "`", "^", "{", "}", "|", "<", ">"]:
            
            """Print an error message and return False if an invalid character is found."""
            print("\nUser typed invalid character. You cannot use these characters: ~ ` ^ { } | < >")
            return False
    
    """Return True if all characters are valid."""
    return True


def isEmailValid(email):
    """Iterate through each character in the email string."""
    
    for character in email:
        
        """Check if the character is in the list of allowed special characters or is alphanumeric."""
        if character.lower() not in ['.', '-', '_', '@', '+', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
            
            """Print an error message and return False if an invalid character is found."""
            print("\nUser typed invalid character. User can only use alphanumeric characters along with these characters:  . - _  @ +")
            return False
    
    """Return True if all characters are valid."""
    return True


def isNameValid(name):
    """Iterate through each character in the name string."""
    
    for character in name:
        
        """Check if the character is in the list of allowed special characters or is alphabetic."""
        if character not in ["'", "-", " "] and not character.isalpha():
            
            """Print an error message and return False if an invalid character is found."""
            print("\nUser typed invalid character. You can only use letters, spaces, and the following characters( , . ' and -) Please try again.")
            return False
    
    """Return True if all characters are valid."""
    return True


def isNumberValid(number):
    """Check if the input string is an integer"""
    if number.isdigit():
        """Return True if the input is a digit."""
        return True
    else:
        """Return False if the input is not a digit."""
        print("You may only use digits.")
        return False 

def isPhoneValid(phone):
    """Check if the phone number is empty."""
    if len(phone) == 0:
        return True
    
    """Check if the phone number has 10 digits and is numeric."""
    if len(phone) == 10:
        return phone.isdigit()
 
    elif len(phone) == 12:
        """Check if the phone number has 12 characters and follows a specific format."""
        return phone[0:3].isdigit() and phone[4:7].isdigit() and phone[8:12].isdigit() and phone[3] in ['.', '-'] and phone[7] in ['.', '-']

    else:
        """Return False if the phone number doesn't match any of the above conditions."""
        return False   

def isStateValid(state):
    """Check if the entered state abbreviation is valid by converting it to uppercase and comparing it to a list of valid state abbreviations."""
    
    if state.upper() not in ["AL", "AK", "AZ", "AR", "CA", 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']:
        """Print an error message if the entered state abbreviation is not valid."""
        print("\nUser typed invalid characters. User can only use these characters: AL, AK, AZ, AR, CA, CO, CT, DE, FL, GA, HI, ID, IL, IN, IA, KS, KY, LA, ME, MD, MA, MI, MN, MS, MO, MT, NE, NV, NH, NJ, NM, NY, NC, ND, OH, OK, OR, PA, RI, SC, SD, TN, TX, UT, VT, VA, WA, WV, WI, WY")
        return False
    else:
        """Return True if the entered state abbreviation is valid."""
        return True  
    

def isZipCodeValid(zip):
    """Check if the entered zip code is valid by checking if it is a digit and its length."""

    if zip.isdigit():
        """Check if the length of the zip code is between 4 and 5 digits."""
        if len(zip) >= 4 or len(zip) <= 5:
            return True
        else:
            """Print an error message if the length of the zip code is not between 4 and 5 digits."""
            print("Zip code can only be between 4 and 5 digits.")
            return False
    else:
        """Print an error message if the zip code contains non-numeric characters."""
        print("Zip code can only be numbers.")
        return False

    
def jsonFilter(dataList):
    """Initialize an empty list to store the filtered data."""

    filteredDataList = []

    """Iterate through each dictionary in the dataList."""
    for dictionary in dataList:
        """Create a new dictionary containing only the desired fields."""
        filteredData = {"First Name": dictionary["First Name"], "Phone1": dictionary["Phone1"], "Phone2": dictionary["Phone2"]}

        """Append the new filtered dictionary to the filteredDataList."""
        filteredDataList.append(filteredData)

    """Return the list of filtered dictionaries."""
    return filteredDataList

def mailingsDelete(my_db, userChoice):
    """Deletes data from the table chosen"""
    while True:
        """Ask the user to confirm if they really want to remove the data."""
        confirmation = input(f"Are you sure you want to remove the data with ID {userChoice}? Type Y/N: ").lower()
        
        """Execute the removal if the user confirms."""
        if confirmation == 'y':
            query = 'DELETE FROM mailings WHERE mail_id = ' + str(userChoice)
            my_db.executeQuery(query)
            my_db.conn.commit()
            print("\Data has been removed.")
            break
        elif confirmation == 'n':
            """Cancel the removal if the user declines."""
            print("\Data removal cancelled.")
            break
        else:
            """Ask for a valid confirmation input if the user types an invalid character."""
            print("\nInvalid input. Please type Y or N.")

def mailingsEdit(my_db, userChoice):
    """Edits a specific record in the 'mailings' table based on user input."""
    
    chooseOption = True

    while chooseOption:
        """Display available options to edit."""
        print("What would you like to edit? (Choose option 1-3)")
        print("\n1.Name")
        print("2.Company")
        print("3.Address")

        """Get user input for the option to edit."""
        option = input("\nChoose option: ")

        """Validate if the input is a number and within the range 1-3."""
        if isNumberValid(option):
            if int(option) >= 1 or int(option) <= 3:
                chooseOption = False
            else:
                print("Error. You may only choose a number between 1 and 3.")

    isValidValue = False

    while not isValidValue:
        """Loop to get the new value for the selected field."""
        
        """Each case corresponds to a different field in the database."""
        if option == "1":
            columnName = "name"
            newValue = input("Enter the new name: ").strip()
            isValidValue = existenceCheck(newValue) and isNameValid(newValue)
        elif option == "2":
            columnName = "company"
            newValue = input("Enter the new company name: ").strip()
            isValidValue = isCompanyValid(newValue)
        elif option == "3":
            columnName = "address"
            newValue = input("Enter the new address: ").strip()
            isValidValue = existenceCheck(newValue) and isAddressValid(newValue)

    newValue = sanitizeInput(newValue)        

    """Update the selected field in the database."""
    my_db.executeQuery("UPDATE mailings SET " + columnName + " = \"" + newValue + "\" WHERE mail_id = " + str(userChoice))
    my_db.conn.commit()

def sanitizeInput(input):
    """Sanitizes user input to escape special characters for SQL queries."""
    input = input.replace("'", "\\'")
    input = input.replace("\\", "\\\\")
    input = input.replace('"', '\\"')

    return input

def showData(my_db):
    """Initialize a flag for valid database option selection."""
    isValidOption = False

    """Loop until a valid database option is selected."""
    while not isValidOption:
        databaseOption = input("Which database would you like shown to you? crm_data (press 1) or mailings (press 2): ")
        if databaseOption == "1" or databaseOption == "2":
            isValidOption = True
        else:
            print("You can only choose number 1 or 2.")

    """Convert the database option to an integer."""
    databaseOption = int(databaseOption)

    """Display data from the crm_data table if option 1 is selected."""
    if databaseOption == 1:
        my_result = my_db.executeSelectQuery("SELECT * FROM crm_data")

        """Iterate through each record in the crm_data table."""
        for data in my_result:
            print("\ncrm ID: " + str(data[0]))
            print("First name: " + data[1])
            print("Last name: " + data[2])
            print("Address: " + str(data[3]))
            print("City: " + data[4])
            print("State: " + data[5])
            print("Zip: " + str(data[6]))
            print("Company: " + data[7])
            print("Primary Phone: " + str(data[8]))
            print("Secondary Phone: " + str(data[9]))
            print("Email: " + str(data[10]))

        """Display data from the mailings table if option 2 is selected."""
    else:
        result = my_db.executeSelectQuery("SELECT * FROM mailings")

        """Iterate through each record in the mailings table."""
        for data in result:
            print("\nMail ID: " + str(data[0]))
            print("Name: " + data[1])
            print("Company: " + data[2])
            print("Address: " + str(data[3]))
