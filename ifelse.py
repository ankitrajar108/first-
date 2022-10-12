from multiprocessing.sharedctypes import Value


a=5
b=10

if b < a:
    print("yes")

else:
    print("no")

# take x and y  two variables and assign them value 
# if x is less than y, print YAYY
# else print NAYY

x=20
y=12

if x < y:
    print("YAYY")

else:
    print("NAYY")

# take values of length and breadth from user
# print if it is a square  or not

breadth = input("Enter breadth : ")
length = input("Enter length : ")

if length==breadth:
    print("square")

else:
    print("not")
 