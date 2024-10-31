def caching_fibonacci():

    # Створюємо порожній словник для кешування обчислених значень
    cache = {}

    # Внутрішня функція, яка обчислює n-те число Фібоначчі
    def fibonacci(n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache:
            return cache[n]
        
        # Якщо значення немає в кеші
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]
        
    return fibonacci

# Отримуємо функцію fibonacci
fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))  
print(fib(15))  