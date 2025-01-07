def print_pyramid(n):
    for i in range(n):
        print(f"{" " * (i)}{"*" * (n - i)}")
        
print_pyramid(5)