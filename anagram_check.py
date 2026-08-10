str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if len(str1) != len(str2):
    print("Not Anagram")
else:
    if sorted(str1) == sorted(str2):
        print("Anagram")
    else:
        print("Not Anagram")