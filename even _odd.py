# from concurrent.futures.process import _chain_from_iterable_of_lists


# company will give bonus on following criteria  
# Time spent in company              Bonus 
#       greater than 10 years          10%

#       More than 6 and less 
#             than 10                   8%
#             less than 6               5%

#  ask the salary and time spent from the User 
#  print the netbonus amount accordingly        

salary = int(input("enter salary : "))
year_of_service = int(input("enter year of service :"))

if year_of_service >=10:
    netbonus=salary*10%100

print("salary")

# galat haai isko banana hai