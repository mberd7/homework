'''
ამოცანა 1:
კონსოლიდან შეიტანეთ მიმდევრობა. დაბეჭდეთ უნიკალური მონაცემებიანი სიმრავლე (set).
'''

s = input("შეიყვანეთ მიმდევრობა: ")

items = [item.strip() for item in s.split(",")]

unique_list = set(items)

print(unique_list)

'''
ამოცანა 2:
პირობა იგივეა, რაც პირველ დავალებაში, ოღონდ დაბეჭდეთ უნიკალური მონაცემებიანი სიმრავლე, 
რომლის შეცვლაც შეუძლებელი იქნება (frozenset).
'''

s = input("შეიყვანეთ მიმდევრობა: ")

items = [item.strip() for item in s.split(",")]

unique_list = frozenset(items)

print(", ".join(unique_list))

'''
ამოცანა 3: 
აიღეთ set ტიპის ორი მონაცემი. ელემენტები თავად განსაზღვრეთ. დაბეჭდეთ გაერთიანებული მონაცემები კორტეჟის სახით (tuple).
'''

set1 = {2, 3, 123, 23, 43, 12}
set2 = {3, 12, 32, 143, 223, 123}

gaertianebuli = set1 | set2

print(tuple(gaertianebuli))


'''
ამოცანა 4:
 კონსოლიდან შევიტანოთ რიცხვების მიმდევრობა როგორც კორტეჟი (tuple). დავბეჭდოთ მხოლოდ უნიკალური ელემენტები სიის სახით (list).
'''

s = input("შეიყვანეთ რიცხვები: ")

items = [int(item.strip()) for item in s.split(',')]

t = tuple(items)

unique_list = list(set(t))

print(unique_list)


'''
ამოცანა 5:
მოცემულია სია, რომლის ელემენტები წარმოადგენენ კორტეჟს:
[("Gega", 24), ("Gaga", 21), ("Goga", 19), ("Giga", 27), ("Gagi", 11)]

დაბეჭდეთ შემდეგი ფორმატით:

Name: Gega, Age: 24
Name: Gaga, Age: 21
Name: Goga, Age: 19
Name: Giga, Age: 27
Name: Gagi, Age: 11

'''

t = [("Gega", 24), ("Gaga", 21), ("Goga", 19), ("Giga", 27), ("Gagi", 11)]

for name, age in t:
    print(f"Name: {name}, Age: {age}")

'''
ამოცანა 6:
მოცემულია მომხმარებლების სია: ["Irakli", "Giorgi", "Nona", "Oto"].
ასევე გვაქვს სხვა მომხმარებლებიც: ["Kato", "Levani", "Nino", "Dato", "Irakli", "Nemo"]
დავბეჭდოთ თანხვედრა.
'''

list1 = ["Irakli", "Giorgi", "Nona", "Oto"]

list2 = ["Kato", "Levani", "Nino", "Dato", "Irakli", "Nemo"]

print(set(list1) & set(list2))
