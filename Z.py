n = int(input())

# Проверяем исключения для чисел 11, 12, 13, 14
if 11 <= n % 100 <= 14:
    print(n, "bochek")
else:
    last_digit = n % 10
    if last_digit == 1:
        print(n, "bochka")
    elif 2 <= last_digit <= 4:
        print(n, "bochki")
    else:
        print(n, "bochek")