str = input("Enter the name:")
str1 = str.casefold()
rev = reversed(str)
if list(str) == list(rev):
    print("this is palindrome")
else:
    print("this string is not a palindrome")