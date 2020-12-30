##Data Structure
#List: Mutable, meaning data can be manipulated

#List instantiation with specific values
my_list = [1,2,3]

#Nested List instantiation
my_list = [1,2,[3,4]]
print('Before appending anything:',my_list)

#Appending list value
my_list.append(5)
print('After appending \'5\' to the list:',my_list)

#Retrieving specific value from a list
my_list[0]#Retrieves first value:1
my_list[3]#Retrieves fourth index value:5

#Dictionaries: Almost the same Structure as JSON file but with sets of method
d = {'k1' : 'val1', 'k2' : 'val2'}

#Retrieving Value of dictionary
d['k1']#Keys are used to retrieved values:val1

#Tuple:Immutable, meaning data cannot be changed/manipulated.

#Tuple instantiation with specific values
my_tuple = (1,2,3)

#Retrieving value from a tuple
my_tuple[0]

#Attempting to change value of a tuple will cause an error
# my_tuple[0] = 'someValue'

#Set: Can expand on data of the variable but removes duplicates and cannot replace index existing values

#Set instantiation with specific values
my_set = {1,2,2,2,2,2,3}

print(my_set)#1,2,3
