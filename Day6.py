# q1.Reverse an array.
arr = [10, 20, 30, 40, 50]

start = 0
end = len(arr) - 1

while start < end:
    arr[start], arr[end] = arr[end], arr[start]
    start += 1
    end -= 1

print("Reversed Array:", arr)

#Q2.Find the smallest element in an array.
arr = [25, 10, 45, 5, 30]

smallest = arr[0]

for i in arr:
    if i < smallest:
        smallest = i

print("Smallest element:", smallest)

# Q3.Find the frequency of each element.
arr = [1, 2, 2, 3, 1, 4, 2]

frequency = {}

for i in arr:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1

for key, value in frequency.items():
    print(key, "->", value)
