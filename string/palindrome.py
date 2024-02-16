word=input("enetr the string")
count=len(word)
str=""
for i in range(count-1,-1,-1):
    str+=word[i]

print("palindrome" if word==str else "not palindrome")
