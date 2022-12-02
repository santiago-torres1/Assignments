"""
Name: Assignment2.py
Author: Santiago Torres
Date created: 10/08/2022
Date last modified: 11/10/2022
This program is designed to work for Arnold's  restaurant, and the user should be one of the employees. This program will
    ask customer information, then which and how many meals, then apply respective discounts and finally print the receipt.
"""
def checkAddress(address):
    b = address.split()
    return True if b[0].isdigit()==True and b[1].isalpha()==True and b[-1].upper() in streets else False

def checkPostalCode(postalCode):
    try:
        postal = [i for i in postalCode]
        numbers = [postal[1], postal[4], postal[6]]
        letters = [postal[0], postal[2], postal[5]]
    except:
        return False
    else:
        return True if ("".join(numbers).isdigit() == True and "".join(letters).isalpha() == True and postal[3] == " ") else False
    
def discount(subtotal):
    return subtotal*0.05 if subtotal<100 else subtotal*0.10 if subtotal<500 else subtotal*0.15

def tipping(tip):
    return 0.10 if tip=="10%" else 0.15 if tip=="15%" else 0.20

def grandtotal(subtotal, deliveryFee, tip):
    return subtotal*1.13+deliveryFee+(subtotal*0.10 if tip=="10%" else subtotal*0.15 if tip=="15%" else subtotal*0.20 if tip=="20%" else 0)

meals = {"1" : {"Name" : "Poutine", "Price" : 7.99}, "2" : {"Name" : "Grilled Chicken Burrito", "Price" : 12.99},
         "3" : {"Name" : "Double Cheeseburger", "Price" : 9.99}, "4" : {"Name" : "Hot Dog wit Chili", "Price" : 8.99},
         "5" : {"Name" : "Chicken Nuggets", "Price" : 6.99}, "6" : {"Name" : "Nachos", "Price" : 5.99}}
order = {}
customerData = {}
provinces = {"ON" :  "ONTARIO", "QC" : "QUEBEC", "NS" : "NOVA SCOTIA", "NB" : "NEW BRUNSWICK", "MB" : "MANITOBA", 
             "BC" : "BRITISH COLUMBIA", "PE" : "PRINCE EDWARD ISLAND", "SK" : "SASKATCHEWAN", "AB" : "ALBERTA",
             "NL" : "NEWFOUNDLAND AND LABRADOR", "NT" : "NORTHWEST TERRITORIES", "YK" : "YUKON", "NU" : "NUNAVUT"}

streets = ["STREET", "ROAD", "AVENUE", "FREEWAY", "HIGHWAY", "BOULEVARD", "DRIVE", "ST", "DR", "RD", "AVE"]

print("Welcome to Arnold's Amazing Food II!")

while True:
    name = list(map(str, input("Please enter the customer's full name: ").split(" "))) #Input for customer's name, which stores first name and last name in different variables
    customerData["firstName"] = name[0]
    customerData["lastName"] = name[-1]
    customerData["address"] = input("Please enter the customer's full delivery address: ")
    while checkAddress(customerData["address"])==False:
        customerData["address"] = input("Please enter a valid address: ")
    customerData["unitNumber"] = input("Please enter the unit number if aplicable: ")#This and the following inputs are inputs for customer's information
    customerData["city"] = input("Please enter the customer's city: ")
    customerData["province"] = input("Please enter the province: ")
    while customerData["province"].upper() not in provinces.keys() and customerData["province"].upper() not in provinces.values():
        customerData["province"] = input("Please enter the province: ")
    customerData["postalCode"] = input("Please enter the customer's postal code. Use the following format [A1A 1A1]: ")
    while checkPostalCode(customerData["postalCode"]) == False:
        customerData["postalCode"] = input("Please enter the customer's postal code. Use the following format [A1A 1A1]: ")
    customerData["phoneNumber"] = str(input("Please enter the customer's phone number: ")) 
    while customerData["phoneNumber"].isdigit == False or len(customerData["phoneNumber"]) != 10:
        customerData["phoneNumber"] = str(input("Please a valid phone number: ")) 
    
    print("\nTake a look at our menu: ")
    while True:
        while True:
            for k in meals.keys():
                print ("{}. {}: ${}".format(k, meals[k]["Name"], meals[k]["Price"]))
                
            item = input("\nPlease select a meal [1-{}]: ".format(len(meals)))
            
            while item not in meals.keys():
                item = input("\nPlease select a meal [1-{}]: ".format(len(meals)))
            while True:
                try:    
                    amountOrder = int(input("Now, how many of those would you like? "))
                except:
                    print("\nPlease type a valid number.")
                else:
                    break
            if len(order) == 0 or (item not in order):
                order[item] = {"Name" : meals[item]["Name"], "Price" : meals[item]["Price"], "Amount" : amountOrder, "Subtotal" : meals[item]["Price"]*amountOrder}
            elif (item in order):
                order[item]["Amount"] = order[item]["Amount"] + amountOrder
                order[item]["Subtotal"] = order[item]["Subtotal"] + meals[item]["Price"]*amountOrder
            another = input("Do you wish to add another item to your order? [y/n]: ")
            while another.strip().upper() != "Y" and another.strip().upper() != "N":
                another = input("Please select a valid option. [y/n]")
            if another.strip().upper() == "Y":
                continue
            else:
                break
        print("Okay! Please confirm the order: ")
        for k in order.keys():
            print("{} x {} (Price: ${}/each)".format(order[k]["Amount"], order[k]["Name"], order[k]["Price"]))
        confirmation = input("Confirm the order [y/n]: ")
        while confirmation.strip().upper() != "Y" and confirmation.strip().upper() != "N":
            confirmation = input("Confirm the order [y/n]: ")  
        if confirmation.strip().upper() == "N": #first condition, if the user selects No
            print ("\nWhat do you want to do?: ") #this messages displays two options: Start all
            print ("\n1. Start order from beginning")
            print ("2. Modify meals")
            orderAgain = str(input("\nPlease select one [1/2]:"))
            while orderAgain.strip() != "1" and orderAgain.strip() != "2": 
                orderAgain = str(input("Please select one [1/2]:"))  
            if orderAgain.strip().upper() == "1": 
                order.clear()
                break
            elif orderAgain.strip().upper() == "2": 
                order.clear()
                continue
        elif confirmation.strip().upper() == "Y": 
            break
    break
print(("ITEM \t").expandtabs(30) + ("PRICE \t AMOUNT \t SUBTOTAL").expandtabs(10))
print("{0:-^60s}".format('')) 
for k in order.keys():
    print(("{} \t").format(order[k]["Name"]).expandtabs(30), (("${:.2f} \t {} \t ${:.2f} ".format(order[k]["Price"], order[k]["Amount"], order[k]["Subtotal"])).expandtabs(10)))
print("{0:-^60s}".format('')) 
for i, k in enumerate(order):
    total = order[k]["Subtotal"] if i==0 else order[k]["Subtotal"] + total
print("TOTAL: ${:.2f}".format(total))
print(("DISCOUNT (5%):" if total <100 else "DISCOUNT (10%):" if total<500 else "DISCOUNT (15%):"), ("-${:.2f}").format(discount(total)))
print("GRAND TOTAL: ${:.2f}".format(total-discount(total))) 
     
student = input("Now, are you a student? [y/n]: ")
while student.strip().upper() != "Y" and student.strip().upper() != "N":
    student = input("Please enter a valid answer. [y/n]: ")
customerData["isStudent"] = True if student.strip().upper() == "Y" else False

print("\nNow, is this order for:")
print("\n1. Delivery")
print("2. Pick up")

delivery = str(input("\nPlease select an option [1/2]: "))
while delivery.strip() != "1" and delivery.strip() != "2":
    delivery = input("Please enter a valid answer. [1/2]: ")
customerData["isDelivery"] = True if delivery.strip() == "1" else False
if customerData["isDelivery"] == True:
    customerData["deliveryFee"] = 5.00 if total <= 30 else 0
    customerData["instructions"] = input("Please enter any special instructions (i. e. Leave at door): ")
    customerData["tip"] = input("Please select your tip: [10%/15%/20%]: ")
    while customerData["tip"].strip().upper() != "10%" and customerData["tip"].strip().upper() != "15%" and customerData["tip"].strip().upper() != "20%":
        customerData["tip"] = input("Please select your tip: [10%/15%/20%]: ")
else:
   customerData["deliveryFee"] = 0  
   customerData["instructions"] = ""
   
print ("\n{0: ^60s}".format(customerData["firstName"] + " " +(customerData["lastName"] if (customerData["lastName"] != customerData["firstName"]) else "")))
if customerData["isDelivery"] == True: #This information will display the customer address only if they picked delivery
    print ("{0: ^60s}".format(customerData["address"]+customerData["unitNumber"]))   
    print ("{0: ^60s}".format(("{}").format(customerData["city"] +", "+ (provinces[customerData["province"]].capitalize() if customerData["province"] in provinces.keys() else customerData["province"].capitalize()) +" "+ customerData["postalCode"])))
print ("{0: ^60s}".format(customerData["phoneNumber"]))
if customerData["isDelivery"] == True:
    print (("{0: ^60s}").format("Special instructions: " + customerData["instructions"]))
print ("\n{0:-^80s}".format(''))
print(("ORDER \t").expandtabs(40) + ("AMOUNT \t PRICE \t TOTAL").expandtabs(15))
print (("{} \t").format("----------").expandtabs(40) + ("{} \t {} \t {}").format("------", "-----", "-----").expandtabs(15))
for k in order.keys():
    print(("{} \t").format(order[k]["Name"]).expandtabs(40), (("{} \t ${:.2f} \t ${:.2f} ".format(order[k]["Amount"], order[k]["Price"], order[k]["Subtotal"])).expandtabs(15)))
print ((("Discount for big purchase (5%) \t").expandtabs(25) if total <100 else ("Discount for big purchase (10%) \t").expandtabs(25) if total<500 else ("Discount for big purchase (15%) \t").expandtabs(25)), ("\t -${:.2f}").format(discount(total)).expandtabs(20))
if customerData["isStudent"] == True:
    print (("{} \t").format("10% Student Savings").expandtabs(40), ("\t -${:.2f}").format(total*0.1).expandtabs(30))
print(("\t").expandtabs(40), ("Subtotal \t ${:.2f}").expandtabs(30).format(total))
print(("\t").expandtabs(40), ("Tax (13%) \t ${:.2f}").expandtabs(30).format(total*0.13))
if customerData["isDelivery"] == True: 
    print(("\t").expandtabs(40), (("Delivery fee \t {:.2f}").expandtabs(30).format(5) if total<=30 else ("Delivery fee (waived) \t ${:.2f}").expandtabs(10).format(0)))
    print(("\t").expandtabs(40), ("Tip ({}) \t ${:.2f}").expandtabs(30).format(customerData["tip"], total*tipping(customerData["tip"])))
print ("{0:-^80s}".format(''))
print((" \t").expandtabs(40) + ("TOTAL \t ${:.2f}").expandtabs(30).format(grandtotal(total, customerData["deliveryFee"], customerData.get("tip"))))



receipt = open("receipt.txt", "w") 
receipt.write("\n{0: ^60s}".format(customerData["firstName"] + " " +(customerData["lastName"] if (customerData["lastName"] != customerData["firstName"]) else "")))
if customerData["isDelivery"] == True: #This information will display the customer address only if they picked delivery
    receipt.write("\n{0: ^60s}".format(customerData["address"]+customerData["unitNumber"]))
    receipt.write("\n{0: ^60s}".format(("{}").format(customerData["city"] +", "+ (provinces[customerData["province"]].capitalize() if customerData["province"] in provinces.keys() else customerData["province"].capitalize()) +" "+ customerData["postalCode"])))
receipt.write("\n{0: ^60s}".format(customerData["phoneNumber"]))
if customerData["isDelivery"] == True:
    receipt.write(("\n{0: ^60s}").format("Special instructions: " + customerData["instructions"]))
receipt.write ("\n{0:-^80s}".format(''))
receipt.write(("\nORDER \t").expandtabs(40) + ("AMOUNT \t PRICE \t TOTAL").expandtabs(15))
receipt.write(("\n{} \t").format("----------").expandtabs(40) + ("{} \t {} \t {}").format("------", "-----", "-----").expandtabs(15))
for k in order.keys():
    receipt.write(("\n{} \t").format(order[k]["Name"]).expandtabs(40) + (("{} \t ${:.2f} \t ${:.2f} ".format(order[k]["Amount"], order[k]["Price"], order[k]["Subtotal"])).expandtabs(15)))
receipt.write((("\nDiscount for big purchase (5%) \t").expandtabs(25) if total <100 else ("Discount for big purchase (10%) \t").expandtabs(25) if total<500 else ("Discount for big purchase (15%) \t").expandtabs(25)) + ("\t -${:.2f}").format(discount(total)).expandtabs(20))
if customerData["isStudent"] == True:
    receipt.write (("\n{} \t").format("10% Student Savings").expandtabs(40) + ("\t -${:.2f}").format(total*0.1).expandtabs(30))
receipt.write(("\n\t").expandtabs(40) + ("Subtotal \t ${:.2f}").expandtabs(30).format(total))
receipt.write(("\n\t").expandtabs(40) + ("Tax (13%) \t ${:.2f}").expandtabs(30).format(total*0.13))
if customerData["isDelivery"] == True: 
    receipt.write(("\n\t").expandtabs(40) + (("Delivery fee \t {:.2f}").expandtabs(30).format(5) if total<=30 else ("Delivery fee (waived) \t ${:.2f}").expandtabs(10).format(0)))
    receipt.write(("\n\t").expandtabs(40) + ("Tip ({}) \t ${:.2f}").expandtabs(30).format(customerData["tip"], total*tipping(customerData["tip"])))
receipt.write ("\n{0:-^80s}".format(''))
receipt.write(("\n \t").expandtabs(50) + ("TOTAL \t ${:.2f}").expandtabs(20).format(grandtotal(total, customerData["deliveryFee"], customerData.get("tip"))))
receipt.close()


     