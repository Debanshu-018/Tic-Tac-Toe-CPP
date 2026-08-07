# Q1.Check if a String is a Palindrome
s = input("Enter a string: ")

if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
    
#Q2.Reverse a String
 s = input("Enter a string: ")

print("Reversed String:", s[::-1])

#Q3.Count Vowels and Consonants
s = input("Enter a string: ").lower()

vowels = "aeiou"
vowel_count = 0
consonant_count = 0

for ch in s:
    if ch.isalpha():
        if ch in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print("Vowels:", vowel_count)
print("Consonants:", consonant_count)

#Q4.Longest Common Prefix
strings = input("Enter strings separated by space: ").split()

prefix = strings[0]

for word in strings[1:]:
    while not word.startswith(prefix):
        prefix = prefix[:-1]
        if not prefix:
            break

print("Longest Common Prefix:", prefix)

#Q5.String Compression
s = input("Enter a string: ")

compressed = ""
count = 1

for i in range(len(s)):
    if i < len(s) - 1 and s[i] == s[i + 1]:
        count += 1
    else:
        compressed += s[i] + str(count)
        count = 1

print("Compressed String:", compressed)
