# Reverse an array.
arr = [10, 20, 30, 40, 50]

start = 0
end = len(arr) - 1

while start < end:
    arr[start], arr[end] = arr[end], arr[start]
    start += 1
    end -= 1

print("Reversed Array:", arr)

# Find the smallest element in an array.
arr = [25, 10, 45, 5, 30]

smallest = arr[0]

for i in arr:
    if i < smallest:
        smallest = i

print("Smallest element:", smallest)
