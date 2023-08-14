# # Trying to make a quotation program for a business
from tabulate import tabulate
# Business infor
busisness_infor = input("Enter your Business name, address, phone number, email and VAT number\nAll saparated by commas: ")
for i in busisness_infor:
    your_business = busisness_infor.split(",")

# customer infor
customer_details = input("Enter customer name, address, phone number, email and VAT number\nAll saparated by commas: ")
for j in customer_details:
    customer = customer_details.split(",")

# Date, customer_ID and quote number 
date = input("Enter date: ")
CustomerID = input("Enter customer_ID: ")
quote = input("Enter Quotation number: ")

#Items, qantity, price

num_items = int(input("How many items does the customer want? "))
items = []
for k in range(num_items):
    item = input("Item: ")
    quantity = int(input("Quantity: "))
    price = int(input("Price: "))
    items.append([item,quantity,price])
print(items)
