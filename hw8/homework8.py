'''
ამოცანა 1:
დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს პარამეტრად n, და გამოიტანს ფიბონაჩის n რაოდენობის მიმდევრობას.
'''

def fibonacci(n):
    if n<= 0:
        return []
    elif n==1:
        return [0]
    
    sequence = [0, 1]
    for i in range(2,n):
        sequence.append(sequence[-1] + sequence[-2])

    return sequence

print(fibonacci(int(input("დაწერეთ მთელი რიცხვი: "))))


'''
ამოცანა 2:
დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს პარამეტრად ორ სტრიქონს და შეამოწმებს არის თუ არა სტრიქონები ანაგრამები (ანაგრამი არის სიტყვა ან შესიტყვება,
რომელიც წარმოიქმნება სხვა სიტყვის ან შესიტყვების ასოების გადაადგილებით). მაგ.: race და care ანაგრამებია.
'''

def is_anagram(s1, s2):
   s1 = s1.replace(" ","").lower()
   s2 = s2.replace(" ","").lower()

   if len(s1) != len(s2):
        return False
   
   count = {}
   for char in s1:
      count[char] = count.get(char,0) + 1
    
   for char in s2:
      count[char] = count.get(char, 0) - 1

   return all(v == 0 for v in count.values())

print(is_anagram(input("ჩაწერეთ პირველი სტრინგი: "), input("ჩაწერეთ მეორე სტრინგი: ")))


'''
ამოცანა 3:
დაწერეთ პითონის ფუნქცია რომელიც მიიღებს n რიცხვს და დააბრუნებს მის ფაქტორიალს.
'''

def factorial(n):
    if n < 0:
        return "ფაქტორიალი არ არსებობს უარყოფითი რიცვისთვის"
    elif n == 0 or n ==1:
        return 1
    else:
        result = 1
        for i in range(2, n+1):
          result *= i

    return result

print(factorial(int(input("ჩაწერეთ მთელი რიცხვი: "))))

'''
ამოცანა 4:
დაწერეთ პითნის ფუნქცია რომელიც მიიღებს  ორ პარამეტრს, პირველს სტრიქონს და მეორეს სიმბოლოს. 
ფუნქციამ უნდა მოძებნოს სტრიქონში რამდენჯერ მეორდება პარამეტრად მიღებული სიმბოლო და დააბრუნოს  მისი რაოდენობა.
'''

def count_char(string, char):
    count = 0
    for c in string:
        if c == char:
            count += 1
    return count

s = input("ჩაწერეთ სტრიქონი: ")
ch = input("აირჩიეთ სიმბოლო: ")

print(f"{s} სტრიქონში {ch} სიმბოლო გვხვდება {count_char(s.lower(), ch.lower())}")
