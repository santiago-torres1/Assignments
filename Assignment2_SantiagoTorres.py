# -*- coding: utf-8 -*-
"""
Name: Assignment2.py
Author: Santiago Torres
Date created: 10/08/2022
Date last modified: 11/10/2022
This program is designed to work for Arnold's  restaurant, and the user should be one of the employees. This program will
    ask customer information, then which and how many meals, then apply respective discounts and finally print the receipt.
"""
customerData = { #This dictionary will store customer data, it will get it from the inputs
    "firstName" : "",
    "lastName" : "",
    "address" : "",
    "city" : "",
    "province" : "",
    "postalCode" : "",
    "instructions" : "",
    "phoneNumber" : "",
        } 
   
meals = { #This dictionary is a nested dictionary that contains information of all the available meals in menu
    "1" : {
        "Name" : "Poutine",
        "Price" : 7.99,
        },
    "2" : {
        "Name" : "Grilled Chicken Burrito",
        "Price" : 12.99,
        },
    "3" : {
        "Name" : "Double Cheeseburger",
        "Price" : 9.99,
        },
    "4" : {
        "Name" : "Hot Dog wit Chili",
        "Price" : 8.99,
        },
    "5" : {
        "Name" : "Chicken Nuggets",
        "Price" : 6.99,
        },
    "6" : {
        "Name" : "Nachos",
        "Price" : 5.99,
        }
    }

orderData = { #This dictionary will store the order data
    "mealNumber" : "",
    "mealName" : "",
    "mealPrice" : "",
    "mealQuantity" : "",
    "discount" : False,
    "HST" : "",
    "isStudent" : False,
    "delivery" : False,
    "deliveryFee" : "",
    "Tip" : 0.00,
    "Tip%" : "",
    "total" : "",
        }    

def subtotalWithDiscount(a): #Defining subtotalWithDiscount function which will calculate the discount depending on how much the final price is

    if a < 100:  #First condition of this funcion, if the subtotal is less than $100, then the discount is 5%
        total = a*0.95
        return total

    elif a >= 100 and a < 500: #Second condition of this funcion, if the subtotal is less than $500 but more than $100, then the discount is 10%
        total = a*0.9
        return total

    else: #last condition of this funcion, if the subtotal is greater than $500, then the discount is 15%
        total = a*0.85
        return total
    
def discountPercentage(a):
    if a < 100:  #First condition of this funcion, if the subtotal is less than $100, then the discount is 5%
        percentage = "5%"
        discount = a*0.05
        return percentage, discount

    elif a >= 100 and a < 500: #Second condition of this funcion, if the subtotal is less than $500 but more than $100, then the discount is 10%
        percentage = "10%"
        discount = a*0.10
        return percentage, discount

    else: #last condition of this funcion, if the subtotal is greater than $500, then the discount is 15%
        percentage = "15%"
        discount = a*0.15
        return percentage, discount
    
def discountStudent(a, b, c): #this function will calculate the student discount, the taxes and the delivery fees and tips (if aplicable).
    if a == True : # if the customer is a student, 10% will apply
            discountStudent = 0.9
    else: #If the customer is not a student, no discount will apply
            discountStudent = 1    
    total = subtotalWithDiscount(orderData.get("mealPrice")*int(orderData.get("mealQuantity")))*discountStudent #Calculation regarding student discount
    tax = total* 0.13 #Calculation of the tax
    if b == True: #condition of the delivery fees and tips.
        if total <= 30:
            deliveryFee = 5.00
        elif total > 30:
            deliveryFee = 0.00
        if c == "1":
            tip = total*0.10
            tip2 = "10%"
        if c == "2":
            tip = total*0.15
            tip2 = "15%"
        if c == "3":
            tip = total*0.20
            tip2 = "20%"
    else:
        tip = 0.00
        deliveryFee = 0.00
        tip2 = ""
    return  tax, total, tip, deliveryFee, tip2 #this function will return a lot of variables that will be stored in orderData dictionary

print ("{0:^60s}".format("Welcome to Arnold's Amazing Eats II! This program will help you fill" + "\n"
     + "all the customer's information, then it will store the customer's order, and then it will print a receipt.")) #This is the welcome message

while True: #First while loop, in case the user wants to start order again

    name = list(map(str, input("Please enter the customer's full name: ").split(" "))) #Input for customer's name, which stores first name and last name in different variables
    customerData["firstName"] = name[0]
    customerData["lastName"] = name[-1]
    customerData["address"] = input("Please enter the customer's full delivery address (include unit number if applicable): ") #This and the following inputs are inputs for customer's information
    customerData["city"] = input("Please enter the customer's city: ")
    customerData["province"] = input("Please enter the customer's province: ")
    customerData["postalCode"] = input("Please enter the customer's postal code: ")
    customerData["phoneNumber"] = str(input("Please enter the customer's phone number: "))
    
    while True: #Second while loop, in case the user wants to restart meal choosing
    
        print("Thank you for that information! Now, which meal would", customerData["firstName"], " like to have today? ") #Message displaying the two available options in the menu
        print(" ")
        for key in meals.keys():
            print("{}. {} : ${}".format(key, meals.get(key, {}).get("Name"), meals.get(key, {}).get("Price")))
            
        orderData["mealNumber"] = str(input("Select option: ")) #Input for selecting which meal the customer wants
        while not((int(orderData["mealNumber"]) >= 1) and (int(orderData["mealNumber"]) <= 6)): #This is done just in case the user types something different from 1 or 2
                orderData["mealNumber"] = str(input("Please select a valid option:")) 
        orderData["mealQuantity"] = input("Amazing! And how many of those does {} want? ".format(customerData["firstName"])) #input for choosing the amount of meals
        confirmation = str(input("Alright! Just to confirm the order is {} {}, right? [y/n]: " .format(orderData["mealQuantity"], meals.get(orderData["mealNumber"], {}).get("Name")))) #confirmation message input
        while not((confirmation.strip().upper() == "Y") or (confirmation.strip().upper() == "N")): #this while loop will repeat if the user inputs something different from y or n
            confirmation = input("Sorry, that was not a valid answer. Just to confirm, the order is {} {}, right? [y/n]: " .format(orderData["mealQuantity"], meals.get(orderData["mealNumber"], {}).get("Name")))       
        if confirmation.strip().upper() == "N": #first condition, if the user selects No
            print ("What do you want to do?: ") #this messages displays two options: Start all over again or modify just the meals
            print (" ")
            print ("1. Start order from beginning")
            print ("2. Modify meals")
            print (" ")
            orderAgain = str(input("Please select one [1 or 2]:"))
            while not((orderAgain.strip() == "1") or (orderAgain.strip() == "2")): #Again, this is done just in case the user types something different from 1 or 2
                orderAgain = str(input("Please select one [1 or 2]:")) 
            
            if orderAgain.strip().upper() == "1": #Second condition, if the user selects to start from beginning. 'l' variable will be 1, so second while loop will be broken, but first will remain
                break
            elif orderAgain.strip().upper() == "2": #Third condition, if the user selects to modify meals, second loop will continue.
                continue
        elif confirmation.strip().upper() == "Y": #Last condition, if the user confirms the order, both loops will be broken and program will continue.
                break
    break

orderData["mealPrice"] = meals.get(orderData["mealNumber"], {}).get("Price") #This lines store meal information in orderData dictionary
orderData["mealName"] = meals.get(orderData["mealNumber"], {}).get("Name")
percentage, discount = discountPercentage(orderData.get("mealPrice")*int(orderData.get("mealQuantity")))

print(("ITEM" + "\t").expandtabs(30) + ("PRICE"+ "\t" + "QUANTITY" + "\t" + "SUBTOTAL").expandtabs(10)) #The following lines will print the order summary, including discount details and order details.
print(("{}" + "\t").format(orderData["mealName"]).expandtabs(30) + ("${:.2f}" + "\t" +  "{}" + "\t" + "${:.2f}").format(float(orderData["mealPrice"]), orderData["mealQuantity"], orderData.get("mealPrice")*int(orderData.get("mealQuantity"))).expandtabs(10))
print("{0:-^60s}".format('')) 
print("TOTAL: " , "${:.2f}".format(orderData.get("mealPrice")*int(orderData.get("mealQuantity"))))
print("DISCOUNT: ", percentage, "-" ,"${:.2f}".format(discount))
print("{0:-^60s}".format('')) 
print("GRAND TOTAL: ", "${:.2f}".format(subtotalWithDiscount(orderData.get("mealPrice")*int(orderData.get("mealQuantity")))))
    
confirmationStudent = str(input("Perfect! Now, is the customer a student? [y/n]:")) #This input will ask if the customer is a student
while not((confirmationStudent.strip().upper() == ("Y")) or (confirmationStudent.strip().upper() == ("N"))): #Once again, just in case the user types something different from y or n
    confirmationStudent = input("Sorry, that was not a valid answer. Is the customer a student? [y/n]:")
if confirmationStudent.strip().upper() == "Y": 
    orderData["isStudent"] = True
print ("Thanks! Now, is this order for: ") #Input for choosing pick up or delivery
print ("") 
print ("1. Pick up")
print ("2. Delivery")
print ("")
confirmationDelivery = str(input("Select one [1/2]: ")) #This input will ask if the customer is a student
while not((confirmationDelivery.strip() == ("1")) or (confirmationDelivery.strip() == ("2"))): #Once again, just in case the user types something different from y or n
    confirmationDelivery = str(input("Sorry, that is not a valid answer. Select one [1/2]: "))
if confirmationDelivery.strip() == "2":
    orderData["delivery"] = True
    customerData["instructions"] = str(input("Please enter special instructions (i. e. leave at door): "))
    print ("Now, please select your tipping amount: ")
    print ("")
    print ("1. 10%")
    print ("2. 15%")
    print ("3. 20%")
    orderData["Tip"] = input("Please select your tip [1/2/3]: ")
    while not((int(orderData["Tip"]) >= 1) and (int(orderData["Tip"]) <= 3)): #Input checker
        orderData["Tip"] = str(input("Please select a valid option: [1/2/3]:")) 
orderData["HST"], orderData["total"], orderData["Tip"], orderData["deliveryFee"], orderData["Tip%"] = discountStudent(orderData["isStudent"], orderData["delivery"], orderData["Tip"])        
print ("") #Finally, the following lines will print the receipt
print ("{0: ^60s}".format(customerData["firstName"] + " " +(customerData["lastName"] if (customerData["lastName"] != customerData["firstName"]) else "")))
if orderData["delivery"] == True: #This information will display the customer address only if they picked delivery
    print ("{0: ^60s}".format(customerData["address"]))   
    print ("{0: ^60s}".format(("{}").format(customerData["city"] +" "+ customerData["province"] +" "+ customerData["postalCode"])))
print ("{0: ^60s}".format(customerData["phoneNumber"]))
if orderData["delivery"] == True:
    print (("{0: ^60s}").format("Special instructions: " + customerData["instructions"]))
print (" ")
print ("{0:-^80s}".format(''))
print(("ORDER" + "\t").expandtabs(40) + ("AMOUNT"+ "\t" + "PRICE" + "\t" + "TOTAL").expandtabs(15))
print (("{}" + "\t").format("----------").expandtabs(40) + ("{}" + "\t" +  "{}" + "\t" + "{}").format("------", "-----", "-----").expandtabs(15))
print (("{}" + "\t").format(orderData.get("mealName")).expandtabs(40) + ("{}" + "\t" +  "${:.2f}" + "\t" + "${:.2f}").format(orderData.get("mealQuantity"), orderData.get("mealPrice"), orderData.get("mealPrice")*int(orderData.get("mealQuantity"))).expandtabs(15))
print (("{}" + " ({})" + "\t").format("Discount for big purchase", percentage).expandtabs(25) + ("\t" + "-${:.2f}").format(discount).expandtabs(20))
if orderData.get("isStudent") == True:
    print (("{}" + "\t").format("10% Student Savings").expandtabs(40) + ("\t" + "-${:.2f}").format(orderData.get("mealPrice")*int(orderData.get("mealQuantity"))*0.1).expandtabs(30))
print(("" + "\t").expandtabs(50) + ("Subtotal" + "\t" + "${:.2f}").expandtabs(20).format(orderData["total"]))
print(("" + "\t").expandtabs(50) + ("Tax (13%)" + "\t" + "${:.2f}").expandtabs(20).format(orderData["HST"]))
if orderData["deliveryFee"] == 5.00: 
    print(("" + "\t").expandtabs(50) + ("Delivery fee " + "\t" + "${:.2f}").expandtabs(20).format(orderData["deliveryFee"]))
if (orderData["deliveryFee"] == 0.00) and (orderData["delivery"] == True):
    print("" + "\t").expandtabs(40) + ("Delivery fee (waived) " + "\t" + "${:.2f}").expandtabs(10).format(orderData["deliveryFee"])
if orderData["delivery"] == True:
    print(("" + "\t").expandtabs(50) + ("Tip " + "{}" + "\t" + "${:.2f}").expandtabs(20).format(orderData["Tip%"], orderData["Tip"]))
print ("{0:-^80s}".format(''))
print(("" + "\t").expandtabs(50) + ("TOTAL" + "\t" + "${:.2f}").expandtabs(20).format(float(orderData["total"])+float(orderData["HST"])+float(orderData["Tip"])+float(orderData["deliveryFee"])))


