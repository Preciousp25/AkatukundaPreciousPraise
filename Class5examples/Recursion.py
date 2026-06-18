def factorial(n):
    #basecase
    if n <= 1:
        return 1
    #recursive case
    else:
        return n * factorial(n - 1)
print(factorial(5))