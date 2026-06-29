'''
ამოცანა 1:
დაწერეთ პითონის ფუნქცია, რომელიც იღებს პარამეტრად ერთიდაიგივე ზომის სიას (list) და zip ფუნქციის გამოყენებით დააჯგუფეთ სიების ელემენტები.
params: [1, 2, 3], ['a', 'b', 'c']  
outputs: ["(1, 'a')", "(2, 'b')", "(3, 'c')"]

'''

def group_list(*lists):
    return [str(t) for  t in zip(*lists)]

example = group_list([1, 2, 3], ['a', 'b', 'c'])
print(example)

'''
ამოცანა 2:
დაწერეთ პითონის ფუნქცია, რომელიც პარამეტრად იღებს რიცხვების სიას და აბრუნებს ელემენტების ნამრავლს.
ფუნქციაში გაითვალისწინეთ გამონაკლისები (Exceptions), თუ მიიღეთ არასწორი ტიპის პარამეტრს (TypeError).
ფუქნციის დასაწერად გამოიყენეთ lambda და  functools-ის reduce მეთოდი.  
params:[1, 2, 3, 4, 5]
output: 120
'''

from functools import reduce

def multiply_list(numbers):
    try:
        return reduce(lambda x, y : x * y, numbers)
    except TypeError:
        print("შეცდომა: სიაში ყველა ელემენტი უნდა იყოს რიცხვი")
        return None
    
print(multiply_list([1,2,3,4,5]))

'''
ამოცანა 3:
დაწერეთ lambda ფუნქცია რომელიც იღებს მთელი რიცხვების სიას (list) და აბრუნებს მხოლოდ სიის კენტ ელემენტებს.

params: [1, 2, 3, 4, 5, 6, 7]
outputs: [1, 3, 5, 7]
'''

get_odds = lambda numbers:list(filter(lambda x: x % 2 != 0, numbers))

print(get_odds([1,2,3,4,5,6,7]))

'''
ამოცანა 4:
დაწერეთ პითნის ფუნქცია, რომელიც იღებს ორ პარამეტრს, სტრიქონების სიასა და სტრიქონს (ending).
დააბრუნეთ მხოლოდ სიის ის ელემენტები რომელიც მთავრდება, მეორე პარამეტრად მიწოდებული სტრიქონით. გამოიყენეთ lambda და filter ფუნქცია.
გაითვალისწინეთ გამონაკლისები (TypeError), თუ სხვა გამონაკლისიც აღმოჩნდა ისიც გაითვალისწინეთ.
მინიშნება: გადაავლეთ თვალი string მეთოდებს, მონახეთ ისეთი მეთოდი, რომელიც აბრუნებს სიტყვას, რომელიც მთავრდება რაღაც სიმბოლოებით...

params: ['hello', 'world', 'coding', 'nod'], 'ing'  
outputs: ['coding']
'''

def filter_by_ending(words, ending):
    try:
        return list(filter(lambda word: word.endswith(ending), words))
    except TypeError:
        print("შეცდომა: სიის ელემენტები სიტყვები უნდა იყოს")
        return None
    except Exception as e:
        print(f"შეცდომა: {e}")
        return None
    
print(filter_by_ending(['hello', 'world', 'coding', 'nod'], 'ing' ))
