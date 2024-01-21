#Use the len function to print the length of the string.
x = "Hello World"
print(len(x))

#Get the first character of the string txt.
txt = "Hello World"
x = txt[0]
#H

#Get the characters from index 2 to index 4 (llo).
txt = "Hello World"
x = txt[2:5]
#llo

#Return the string without any whitespace at the beginning or the end.
txt = " Hello World "
x = txt.strip()

#Hello World

#Convert the value of txt to upper case.
txt = "Hello World"
txt = txt.upper()
#HELLO WORLD

#Convert the value of txt to lower case.
txt = "Hello World"
txt = txt.lower()
#hello world

#Replace the character H with a J.
txt = "Hello World"
txt = txt.replace("H","J")
#Jello World

#Insert the correct syntax to add a placeholder for the age parameter.
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
#My name is John, and I am 36