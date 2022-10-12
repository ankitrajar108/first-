 # a company decided to give bonus of 1000Rs 
    # to employee if his service is more than 5 years
    # ask user their salary and year of service and print
    # the net bonous amount

salary = int(input("Enter salary : "))
year_of_service = int(input("Enter year of service : "))

if year_of_service > 5:
   netbonus=salary+1000
else:
    netbonus=salary
print("The netbonus is",netbonus)


