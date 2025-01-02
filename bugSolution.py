def function_iterative(x):
    result = 0
    for i in range(1, x + 1):
        result += i
    return result

print(function_iterative(5))
print(function_iterative(1000))