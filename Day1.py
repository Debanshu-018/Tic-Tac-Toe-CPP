# 1. Print 1 to 10
# Write a for loop that prints numbers from 1 to 10, one per line
for i in range(1,11):
    print(i)

# 2. Sum of a list
# Given nums = [3, 7, 2, 9, 4], use a for loop to calculate the sum. Print the final total.
nums =[3, 7, 2, 9, 4]
total = 0
for i in nums:
    total += i
    print(total)

# 3. Even numbers only
# Loop through numbers 1 to 20 and print only the even ones.
for i in  range(1,21):
    if i %2 == 0:
        print(i)

# 4. Reverse a string
# Given word = "python", use a for loop to print each character in reverse order, one per li
word ="python"
for char in word[::-1]:
    print(char)


# 5. Multiplication table
# Print the 5× multiplication table from 5×1 to 5×10.
for i in range (1,11):
    print("5 *",i,"=",5*i)
