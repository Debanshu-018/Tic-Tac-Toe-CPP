# Find the largest among 100 numbers

largest = float('-inf')

for i in range(100):
    num = float(input(f"Enter number {i + 1}: "))
    if num > largest:
        largest = num

print("The largest number is:", largest)
