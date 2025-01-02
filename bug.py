def function(x):
    if x == 0:
        return 0
    else:
        return function(x - 1) + x

print(function(5)) # This will work correctly
print(function(1000)) # This will cause a RecursionError