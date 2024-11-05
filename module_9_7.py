def is_prime(func):
    def wrapper(*args, **kwargs):
        num = func(*args, **kwargs)
        if num <= 1:
            print("Составное")
            return num
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                print("Составное")
                return num
        print("Простое")
        return num
    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c

result = sum_three(2, 3, 6)
print(result)
