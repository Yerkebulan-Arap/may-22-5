user_input = str(input("Введите слово:"))
letter1 = user_input[:1]
letterLast = user_input[-1:]
censore = "*"*len(user_input[1:-1]) 
result = letter1+censore+letterLast
print("Результат:", result)