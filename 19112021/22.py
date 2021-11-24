#Get a string from an input string where all occurrences of first character replaced with ‘$’, except first character.
list1 = []
str1 = input("Enter a string:")
print("Origial String:", str1)
f = str1[0]
list1 = [str1.replace(i, '$') for i in str1 if i == f]
list1[0] = f
print(list1)


