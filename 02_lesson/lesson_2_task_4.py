# кратные 3 → Fizz, 5 → Buzz, 3 и 5 → FizzBuzz
# определим функцию, которая выводит числа от 1 до n, заменяя:
#    - числа, делящиеся на 3, на 'Fizz'
#    - числа, делящиеся на 5, на 'Buzz'  
#    - числа, делящиеся на 3 и 5, на 'FizzBuzz'

def fizz_buzz(n):

    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

# Тестируем функцию
print("fizz_buzz(17) →")
fizz_buzz(17)