def palindrome(s):
    return s == s[::-1]

out = palindrome(input("Write something, let's see if it's a palindrome:"))
if out:
    print("It is a palindrome!")
else:
    print("It is not a palindrome :(")