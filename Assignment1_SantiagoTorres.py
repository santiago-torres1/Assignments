# -*- coding: utf-8 -*-
"""
Name: Assignment1.py
Author: Santiago Torres
Date created: 10/08/2022
Date last modified: 10/10/2022
This program is designed to work for Arnold's  restaurant, and the user should be one of the employees. This program will
    ask customer information, then which and how many meals, then apply respective discounts and finally print the receipt.
"""
global l #Declaring global variables that will be used in the While loops later.
global i
i=0
l=0
def subtotal(): #Defining Subtotal function which will calculate the multiplication between the number of orders and the price of them
    total = price*numberOfItems
    return total
    
def subtotalWithDiscount(): #Defining subtotalWithDiscount function which will calculate the discount depending on how much the final price is
    global percentage #Declaring global variables that will store the value of the percentage of the discount and the value of the discount in dollars.
    global discount
    if subtotal() < 100:  #First condition of this funcion, if the subtotal is less than $100, then the discount is 5%
        total = subtotal()*0.95
        percentage = "5%"
        discount = subtotal()*0.05
        return total

    elif subtotal() >= 100 and subtotal() < 500: #Second condition of this funcion, if the subtotal is less than $500 but more than $100, then the discount is 10%
        total = subtotal()*0.9
        percentage = "10%"
        discount = subtotal()*0.10
        return total

    else: #last condition of this funcion, if the subtotal is greater than $500, then the discount is 15%
        total = subtotal()*0.85
        percentage = "15%"
        discount = subtotal()*0.15
        return total
    
print ("{0:^60s}".format("Welcome to Arnold's Amazing Eats II! This program will help you fill" + "\n"
     + "all the customer's information, then it will store the customer's order, and then it will print a receipt.")) #This is the welcome message
while i==0: #First while loop, in case the user wants to start order again
    i=0 #It is important to restart the loop variables so the loop can restart normally.
    l=0
    name = list(map(str, input("Please enter the customer's full name: ").split(" "))) #Input for customer's name, which stores first name and last name in different variables
    firstName = name[0]
    lastName = name[-1]
    address = input("Please enter the customer's full delivery address (include unit number if applicable): ") #This and the following inputs are inputs for customer's information
    city = input("Please enter the customer's city: ")
    province = input("Please enter the customer's province: ")
    postalCode = input("Please enter the customer's postal code: ")
    instructions = input("Please enter any special instructions (e.g., Leave at door): ")
    phoneNumber = str(input("Please enter the customer's phone number: "))
    while l==0: #Second while loop, in case the user wants to restart meal choosing
        l=0
        print("Thank you for that information! Now, which meal would", firstName, " like to have today? ") #Message displaying the two available options in the menu
        print(" ")
        print("1. Double cheeseburger")
        print("2. Grilled Chicken Burrito")
        orderNumber = str(input("Select option [1 or 2]: ")) #Input for selecting which meal the customer wants
        while not((orderNumber.strip() == "1") or (orderNumber.strip() == "2")): #This is done just in case the user types something different from 1 or 2
                orderNumber = str(input("Please select one [1 or 2]:")) 
        orderNumber = int(orderNumber)
        print ("")
        print("Amazing! And how many of those does", firstName , "want?") #Message asking about the amount of meals
        numberOfItems = int(input()) #input for choosing the amount of meals
        order = ["", "Double cheeseburger" , "Grilled Chicken Burrito"] #This list stores the written meal options. 
        confirmation = str(input("Alrighty! Just to confirm the order is {} {}, right? [y/n]: " .format(numberOfItems, order[orderNumber]))) #confirmation message input
        while not((confirmation.strip().upper() == "Y") or (confirmation.strip().upper() == "N")): #this while loop will repeat if the user inputs something different from y or n
            confirmation = input("Sorry, that was not a valid answer. Just to confirm, the order is {} {}, right? [y/n]: " .format(numberOfItems, order[orderNumber]))
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
                l=1
            elif orderAgain.strip().upper() == "2": #Third condition, if the user selects to modify meals, second loop will continue.
                continue
        elif confirmation.strip().upper() == "Y": #Last condition, if the user confirms the order, both loops will be broken and program will continue.
            i=1
            l=1
price = float(input("Okay! Now, what's the price of that meal? ")) #Input asking for the price of the meal

subtotalWithDiscount() #Calling function for calculating the subtotal with the discount

print(("ITEM" + "\t").expandtabs(30) + ("PRICE"+ "\t" + "QUANTITY" + "\t" + "SUBTOTAL").expandtabs(10)) #The following lines will print the order summary, including discount details and order details.
print(("{}" + "\t").format(order[orderNumber]).expandtabs(30) + ("${:.2f}" + "\t" +  "{}" + "\t" + "${:.2f}").format(price, numberOfItems, subtotal()).expandtabs(10))
print("{0:-^60s}".format('')) 
print("TOTAL: " , "${:.2f}".format(subtotal()))
print("DISCOUNT: ", percentage, "-" ,"${:.2f}".format(discount))
print("{0:-^60s}".format('')) 
print("GRAND TOTAL: ", "${:.2f}".format(subtotalWithDiscount()))
    
confirmationStudent = str(input("Perfect! Now, is the customer a student? [y/n]:")) #This input will ask if the customer is a student
while not((confirmationStudent.strip().upper() == ("Y")) or (confirmationStudent.strip().upper() == ("N"))): #Once again, just in case the user types something different from y or n
    confirmationStudent = input("Sorry, that was not a valid answer. Is the customer a student? [y/n]:")
if confirmationStudent.strip().upper() == "Y": #Another condition, if the customer is a student, 10% will apply
    discountStudent = 0.9
else: #If the customer is not a student, no discount will apply
    discountStudent = 1
totalWithStudentDiscount = subtotalWithDiscount()*discountStudent #Calculation regarding student discount
totalWithTax = totalWithStudentDiscount * 1.13 #Calculation regarding total with tax
Tax = totalWithStudentDiscount* 0.13 #Calculation of the tax
if lastName == firstName: #These two conditionals are just in case the user types only one name instead of the full name
    name = str(firstName)
else:
    name = str(firstName) + " " + str(lastName)
print ("") #Finally, the following lines will print the receipt
print ("{0: ^60s}".format(name))
print ("{0: ^60s}".format(address))   
print ("{0: ^60s}".format((" {}" + " {}" + " {}").format(city, province, postalCode)))
print ("{0: ^60s}".format(phoneNumber))
print (("{0: ^60s}").format("Special instructions: " + instructions))
print (" ")
print ("{0:-^60s}".format(''))
print(("ORDER" + "\t").expandtabs(30) + ("AMOUNT"+ "\t" + "PRICE" + "\t" + "Total").expandtabs(10))
print (("{}" + "\t").format("----------").expandtabs(30) + ("{}" + "\t" +  "{}" + "\t" + "{}").format("------", "-----", "-----").expandtabs(10))
print (("{}" + "\t").format(order[orderNumber]).expandtabs(30) + ("{}" + "\t" +  "${:.2f}" + "\t" + "${:.2f}").format(numberOfItems, price, subtotal()).expandtabs(10))
if discountStudent == 1: #This condition will apply if the customer is not a student. In that case, no information regarding student discount will be shown in the receipt
    print (("{}" + " ({})" + "\t").format("Discount for big purchase", percentage).expandtabs(20) + ("\t" + "-${:.2f}").format(discount).expandtabs(10))
    print(("" + "\t").expandtabs(40) + ("Subtotal" + "\t" + "${:.2f}").expandtabs(10).format(totalWithStudentDiscount))
    print(("" + "\t").expandtabs(40) + ("Tax (13%)" + "\t" + "${:.2f}").expandtabs(10).format(Tax))
    print(("" + "\t").expandtabs(40) + ("TOTAL" + "\t" + "${:.2f}").expandtabs(10).format(totalWithTax))
else: #This condition will apply if the customer is a student, and it will show the information regarding student savings.
    print (("{}" + " ({})" + "\t").format("Discount for big purchase", percentage).expandtabs(20) + ("\t" + "-${:.2f}").format(discount).expandtabs(10))
    print (("{}" + "\t").format("10% Student Savings").expandtabs(40) + ("\t" + "-${:.2f}").format(subtotal()*0.1).expandtabs(10))
    print(("" + "\t").expandtabs(40) + ("Subtotal" + "\t" + "${:.2f}").expandtabs(10).format(totalWithStudentDiscount))
    print(("" + "\t").expandtabs(40) + ("Tax (13%)" + "\t" + "${:.2f}").expandtabs(10).format(Tax))
    print(("" + "\t").expandtabs(40) + ("TOTAL" + "\t" + "${:.2f}").expandtabs(10).format(totalWithTax))