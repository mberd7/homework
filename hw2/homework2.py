#ამოცანა 1
num_list=[44, 23, 11, 8, 20, 56, 33, 55]
a=int(input("Enter a number:"))
if a in num_list:
    print("The number  in list")
else:
    print("The number not in list ")


#ამოცანა 2
a = eval(input("Enter an integer"))

if a%2==0:
    print("The number is even")
else:
    print("The number is odd")

#ამოცანა 3
st1 = input("What's first string? ")
st2 = input("What's second string? ")

if st1 is st2:
    print("Same object")
else:
    print("Different object")

#ამოცანა 4
num_list = [44, 23, 11, 8, 20, 56, 33, 55]
num = eval(input("What's number? "))
if num > num_list[2] and num < num_list[-1]:
    print("More than list elements")
elif num == num_list[5]:
    print("Equal")
else:
    print("None of the conditions were met")
