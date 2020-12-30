##Variable Assignment and Printing
#Strings

#Quotes
'single quotes' #Generally used for regular expressions such as dict keys or SQL
"Double quotes" #Used for representing Strings

#Printing
x = "Hello World!" # Assigns statement/String "Hello World!" to var x
print(x) # Prints current value of instantiated var

#format()
x = "Hello"
y = "World!"
print("{} {}".format(x,y))#Curly braces are used to fill up the data based on the sequence

x = "Hello"
y = "World!"
print("{one} {two}".format(two = y,one = x))#Curly braces with identifiers are filled with data that's both identified and assigned with pointer
